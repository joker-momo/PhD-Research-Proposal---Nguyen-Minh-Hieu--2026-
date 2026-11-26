"""Behavior tests for the advisory prompt-to-skill router."""
import json
from pathlib import Path
import subprocess
import tempfile
import unittest

import skill_router


SKILL_NAMES = (
    "academic-pipeline",
    "academic-research-skills:academic-pipeline",
    "academic-research-skills:deep-research",
    "deep-research",
    "debugging-and-error-recovery",
    "git-workflow-and-versioning",
    "imagegen",
    "lawful-paper-pdf-retriever",
    "literature-review",
    "nature-downloader",
    "paper-lookup",
    "planning-and-task-breakdown",
    "scientific-writing",
    "systematic-debugging",
    "test-driven-development",
)


class SkillRouterTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory(prefix="skill-router-test-")
        self.root = Path(self.temp.name)
        self.catalog = {}
        for name in SKILL_NAMES:
            path = self.root / name.replace(":", "_") / "SKILL.md"
            path.parent.mkdir(parents=True)
            path.write_text(f"---\nname: {name}\n---\n# {name}\n")
            self.catalog[name] = path
        self.addCleanup(self.temp.cleanup)

    def route(self, prompt):
        return skill_router.route_prompt(prompt, self.catalog)

    @staticmethod
    def names(route):
        selected = ([route.primary] if route.primary else []) + route.supporting
        return [skill.name for skill in selected]

    def assert_valid_selection(self, route):
        names = self.names(route)
        self.assertLessEqual(len(names), 3)
        self.assertEqual(len(names), len(set(names)))
        families = [skill_router.skill_family(name) for name in names]
        constrained = [family for family in families if family is not None]
        self.assertEqual(len(constrained), len(set(constrained)))

    def test_explicit_installed_skill_has_highest_priority(self):
        route = self.route(
            "Dùng $scientific-writing để chỉnh bài và tìm nguồn nghiên cứu."
        )

        self.assertEqual("scientific-writing", route.primary.name)
        self.assert_valid_selection(route)

    def test_unknown_explicit_skill_is_reported_without_blocking_inference(self):
        route = self.route("Dùng $khong-ton-tai để debug lỗi này.")

        self.assertEqual(["khong-ton-tai"], route.unknown_explicit)
        self.assertEqual("systematic-debugging", route.primary.name)
        self.assertTrue(route.advisory_only)

    def test_academic_pipeline_excludes_equivalent_pipelines(self):
        route = self.route(
            "Dùng $academic-pipeline và "
            "$academic-research-skills:academic-pipeline cho toàn bộ bài báo."
        )

        self.assertEqual(["academic-pipeline"], self.names(route))
        self.assertIn(
            "academic-research-skills:academic-pipeline", route.skipped_overlap
        )

    def test_research_prompt_is_owned_by_gemini(self):
        route = self.route(
            "Research và xác minh nguồn cho systematic literature review."
        )

        self.assertEqual("GEMINI_RESEARCH", route.owner)
        self.assertIn(route.primary.name, {"literature-review", "deep-research"})
        self.assert_valid_selection(route)

    def test_writing_prompt_is_owned_by_codex(self):
        route = self.route("Viết và chỉnh sửa phần Discussion của manuscript.")

        self.assertEqual("CODEX_WRITING", route.owner)
        self.assertEqual("scientific-writing", route.primary.name)

    def test_paper_retrieval_uses_lawful_priority_chain(self):
        route = self.route("Tải PDF toàn văn các bài báo theo danh sách DOI.")

        self.assertEqual(
            [
                "paper-lookup",
                "lawful-paper-pdf-retriever",
                "nature-downloader",
            ],
            self.names(route),
        )
        self.assertNotIn("paper-downloader", self.names(route))
        self.assertEqual("GEMINI_RESEARCH", route.owner)

    def test_debugging_selects_debugger_then_tdd(self):
        route = self.route("Debug lỗi failing test và sửa bug trong hook.")

        self.assertEqual(
            ["systematic-debugging", "test-driven-development"], self.names(route)
        )

    def test_image_request_selects_imagegen(self):
        route = self.route("Tạo một hình minh họa mới cho bài thuyết trình.")

        self.assertEqual(["imagegen"], self.names(route))

    def test_trivial_prompt_returns_none_with_reason(self):
        route = self.route("Xin chào")
        rendered = skill_router.render_route(route)

        self.assertIsNone(route.primary)
        self.assertIn("SKILLS: none —", rendered)
        self.assertTrue(route.reason)

    def test_multi_goal_prompt_splits_research_and_writing_ownership(self):
        route = self.route(
            "Tìm và xác minh nguồn, sau đó viết lại phần Related Work."
        )

        self.assertEqual(
            "SPLIT: RESEARCH=GEMINI_RESEARCH; WRITING=CODEX_WRITING", route.owner
        )
        self.assertIn("scientific-writing", self.names(route))
        self.assert_valid_selection(route)

    def test_duplicate_function_skills_are_suppressed(self):
        route = self.route(
            "Dùng $deep-research và $academic-research-skills:deep-research "
            "để tìm nguồn."
        )

        self.assertEqual(["deep-research"], self.names(route))
        self.assertIn(
            "academic-research-skills:deep-research", route.skipped_overlap
        )

    def test_alternative_debug_pipelines_are_not_loaded_together(self):
        route = self.route(
            "Dùng $systematic-debugging và $debugging-and-error-recovery."
        )

        self.assertEqual(
            ["systematic-debugging", "test-driven-development"], self.names(route)
        )
        self.assertIn("debugging-and-error-recovery", route.skipped_overlap)

    def test_selected_skill_paths_exist_and_require_full_read(self):
        route = self.route("Tải full-text PDF bài báo theo DOI.")
        rendered = skill_router.render_route(route)

        for selected in [route.primary, *route.supporting]:
            self.assertTrue(selected.path.is_file())
            self.assertIn(f"READ_FULL_SKILL_MD: {selected.path}", rendered)

    def test_explicit_skill_cap_is_one_primary_and_two_supporting(self):
        route = self.route(
            "Dùng $scientific-writing, $git-workflow-and-versioning, "
            "$planning-and-task-breakdown và $imagegen."
        )

        self.assertEqual(3, len(self.names(route)))
        self.assertIn("imagegen", route.skipped_cap)

    def test_malformed_payload_process_exits_zero_and_stays_advisory(self):
        script = Path(skill_router.__file__)
        result = subprocess.run(
            ["/usr/bin/python3", str(script)],
            input="not-json",
            text=True,
            capture_output=True,
            check=False,
        )

        self.assertEqual(0, result.returncode)
        self.assertIn("ADVISORY_ONLY: true", result.stdout)
        self.assertIn("SKILLS: none —", result.stdout)
        self.assertEqual(1, result.stdout.count("CODE_FIRST_DECISION: "))

    def test_payload_prompt_extraction(self):
        payload = {"hook_event_name": "UserPromptSubmit", "prompt": "Xin chào"}

        self.assertEqual("Xin chào", skill_router.extract_prompt(payload))
        self.assertEqual("", skill_router.extract_prompt({"prompt": 42}))

    def test_every_route_renders_one_code_first_decision(self):
        prompts = (
            "Xin chào",
            "Giải thích systematic review là gì.",
            "Chạy test hiện có và báo kết quả.",
            "Viết script kiểm tra hàng loạt DOI bị trùng.",
            "Tìm nguồn cho systematic review.",
            "Viết lại một đoạn kết luận ngắn.",
            "Dùng API hiện có để tra cứu metadata.",
            "Tạo hook tái sử dụng để kiểm tra timestamp.",
            "Xác nhận thủ công thông tin tác giả với tôi.",
            "Biên dịch bản LaTeX bằng build script của dự án.",
        )

        for prompt in prompts:
            with self.subTest(prompt=prompt):
                rendered = skill_router.render_route(self.route(prompt))
                decision_lines = [
                    line
                    for line in rendered.splitlines()
                    if line.startswith("CODE_FIRST_DECISION: ")
                ]
                self.assertEqual(1, len(decision_lines))
                self.assertRegex(
                    decision_lines[0],
                    r"^CODE_FIRST_DECISION: "
                    r"(REUSE_EXISTING|WRITE_SCRIPT|MANUAL) — .+$",
                )

    def test_existing_project_tool_is_reused(self):
        route = self.route("Chạy test hiện có và báo kết quả.")

        self.assertEqual("REUSE_EXISTING", route.code_first_mode)

    def test_existing_api_is_reused(self):
        route = self.route("Dùng API hiện có để tra cứu metadata DOI.")

        self.assertEqual("REUSE_EXISTING", route.code_first_mode)

    def test_existing_build_script_is_reused(self):
        route = self.route("Biên dịch LaTeX bằng build script của dự án.")

        self.assertEqual("REUSE_EXISTING", route.code_first_mode)

    def test_repeated_batch_validation_prefers_script(self):
        route = self.route("Kiểm tra hàng loạt 200 DOI và loại bản ghi trùng.")

        self.assertEqual("WRITE_SCRIPT", route.code_first_mode)

    def test_reusable_hook_request_prefers_script(self):
        route = self.route("Tạo hook tái sử dụng để kiểm tra timestamp.")

        self.assertEqual("WRITE_SCRIPT", route.code_first_mode)

    def test_structured_file_transformation_prefers_script(self):
        route = self.route("Parse các file CSV rồi chuẩn hóa và xuất JSON.")

        self.assertEqual("WRITE_SCRIPT", route.code_first_mode)

    def test_explanation_stays_manual(self):
        route = self.route("Giải thích systematic review là gì.")

        self.assertEqual("MANUAL", route.code_first_mode)

    def test_short_prose_edit_stays_manual(self):
        route = self.route("Viết lại một đoạn kết luận ngắn.")

        self.assertEqual("MANUAL", route.code_first_mode)

    def test_human_confirmation_stays_manual(self):
        route = self.route("Xác nhận thủ công thông tin tác giả với tôi.")

        self.assertEqual("MANUAL", route.code_first_mode)

    def test_script_substep_wins_over_manual_review_wording(self):
        route = self.route(
            "Rà soát rồi viết script kiểm tra tự động các DOI bị trùng."
        )

        self.assertEqual("WRITE_SCRIPT", route.code_first_mode)

    def test_catalog_prefers_direct_skill_over_nested_bundle_duplicate(self):
        root = self.root / "catalog"
        direct = root / "deep-research/SKILL.md"
        nested = root / "_bundle/deep-research/SKILL.md"
        for path in (direct, nested):
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_text("---\nname: deep-research\n---\n# Deep research\n")

        catalog = skill_router.discover_catalog((root,))

        self.assertEqual(direct.resolve(), catalog["deep-research"])


class HookConfigurationTests(unittest.TestCase):
    def test_user_prompt_submit_registers_advisory_router_after_task_gate(self):
        config_path = Path(__file__).parents[1] / "hooks.json"
        config = json.loads(config_path.read_text())
        commands = [
            hook["command"]
            for group in config["hooks"]["UserPromptSubmit"]
            for hook in group["hooks"]
        ]

        self.assertIn("task_gate.py", commands[0])
        self.assertTrue(any("skill_router.py" in command for command in commands[1:]))


if __name__ == "__main__":
    unittest.main(verbosity=2)
