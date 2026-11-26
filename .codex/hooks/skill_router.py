#!/usr/bin/env python3
"""Advisory prompt router for selecting a small, non-overlapping skill set.

This hook never blocks a prompt. It prints a recommendation; the acting agent
still owns the decision and must read every selected SKILL.md in full.
"""
from dataclasses import dataclass, field
import json
import os
from pathlib import Path
import re
import sys
from typing import Dict, Iterable, List, Mapping, Optional, Sequence, Tuple


MAX_SKILLS = 3
DEFAULT_SKILL_ROOTS = (
    Path.home() / ".codex/skills",
    Path.home() / ".agents/skills",
    Path.home() / ".codex/plugins/cache",
)
PIPELINE_EQUIVALENTS = {
    "academic-pipeline",
    "academic-research-skills:academic-pipeline",
}
PIPELINES_ORCHESTRATED_BY_ACADEMIC = PIPELINE_EQUIVALENTS | {
    "deep-research",
    "academic-research-skills:deep-research",
}
FAMILY_BY_NAME = {
    "academic-pipeline": "academic-pipeline",
    "academic-research-skills:academic-pipeline": "academic-pipeline",
    "deep-research": "deep-research",
    "academic-research-skills:deep-research": "deep-research",
    "academic-paper": "academic-writing",
    "academic-research-skills:academic-paper": "academic-writing",
    "scientific-writing": "academic-writing",
    "academic-paper-reviewer": "academic-review",
    "academic-research-skills:academic-paper-reviewer": "academic-review",
    "systematic-debugging": "debugging-pipeline",
    "debugging-and-error-recovery": "debugging-pipeline",
    "compound-engineering:ce-debug": "debugging-pipeline",
    "planning-and-task-breakdown": "planning",
    "writing-plans": "planning",
    "compound-engineering:ce-plan": "planning",
    "code-review-and-quality": "code-review",
    "compound-engineering:ce-code-review": "code-review",
}


@dataclass(frozen=True)
class Skill:
    name: str
    path: Path


@dataclass
class Route:
    owner: str
    code_first_mode: str = "MANUAL"
    code_first_reason: str = "no safe reusable automation was identified"
    primary: Optional[Skill] = None
    supporting: List[Skill] = field(default_factory=list)
    unknown_explicit: List[str] = field(default_factory=list)
    skipped_overlap: List[str] = field(default_factory=list)
    skipped_cap: List[str] = field(default_factory=list)
    reason: str = ""
    advisory_only: bool = True


def skill_family(name: str) -> Optional[str]:
    """Return a constrained family only for skills that must not co-load."""
    return FAMILY_BY_NAME.get(name)


def _frontmatter_name(path: Path) -> Optional[str]:
    try:
        with path.open(encoding="utf-8", errors="replace") as handle:
            first = handle.readline().strip()
            if first != "---":
                return None
            for line in handle:
                stripped = line.strip()
                if stripped == "---":
                    return None
                match = re.match(r"name\s*:\s*['\"]?([^'\"]+?)['\"]?\s*$", stripped)
                if match:
                    return match.group(1).strip()
    except OSError:
        return None
    return None


def discover_catalog(roots: Optional[Sequence[Path]] = None) -> Dict[str, Path]:
    """Discover installed skills, preserving root priority for duplicate names."""
    configured = os.environ.get("CODEX_SKILL_ROOTS")
    if roots is None and configured:
        roots = tuple(Path(value).expanduser() for value in configured.split(os.pathsep))
    search_roots = tuple(roots or DEFAULT_SKILL_ROOTS)
    catalog: Dict[str, Path] = {}
    for root in search_roots:
        if not root.is_dir():
            continue
        try:
            paths = sorted(
                root.rglob("SKILL.md"),
                key=lambda path: (len(path.relative_to(root).parts), str(path)),
            )
        except OSError:
            continue
        for path in paths:
            name = _frontmatter_name(path)
            if name and name not in catalog:
                catalog[name] = path.resolve()
    return catalog


def extract_prompt(payload: Mapping[str, object]) -> str:
    """Extract prompt text from supported hook payload shapes."""
    for key in ("prompt", "user_prompt", "message"):
        value = payload.get(key)
        if isinstance(value, str):
            return value
    tool_input = payload.get("tool_input")
    if isinstance(tool_input, Mapping):
        for key in ("prompt", "message", "text"):
            value = tool_input.get(key)
            if isinstance(value, str):
                return value
    return ""


def _explicit_mentions(prompt: str, catalog: Mapping[str, Path]) -> Tuple[List[str], List[str]]:
    mentions: List[Tuple[int, str, bool]] = []
    token_pattern = r"[A-Za-z0-9_:-]+(?:\.[A-Za-z0-9_:-]+)*"
    for match in re.finditer(rf"\$({token_pattern})", prompt):
        mentions.append((match.start(), match.group(1), True))
    for match in re.finditer(rf"(?i)\bskill\s+[`'\"]?({token_pattern})", prompt):
        mentions.append((match.start(1), match.group(1), True))
    for match in re.finditer(rf"`({token_pattern})`", prompt):
        mentions.append((match.start(), match.group(1), False))
    for name in catalog:
        match = re.search(rf"(?<![A-Za-z0-9_.:-]){re.escape(name)}(?![A-Za-z0-9_.:-])", prompt)
        if match:
            mentions.append((match.start(), name, False))

    known: List[str] = []
    unknown: List[str] = []
    seen = set()
    for _, name, report_unknown in sorted(mentions, key=lambda item: item[0]):
        if name in seen:
            continue
        seen.add(name)
        if name in catalog:
            known.append(name)
        elif report_unknown:
            unknown.append(name)
    return known, unknown


def _contains(prompt: str, patterns: Iterable[str]) -> bool:
    return any(re.search(pattern, prompt, flags=re.IGNORECASE) for pattern in patterns)


def _infer_candidates(prompt: str) -> List[str]:
    candidates: List[str] = []
    paper_retrieval = _contains(prompt, (
        r"tải.{0,24}(pdf|bài báo|toàn văn|full.?text)",
        r"download.{0,24}(paper|pdf|full.?text)",
        r"full.?text.{0,24}(paper|pdf|bài báo)",
        r"(pdf|bài báo).{0,24}(doi|toàn văn)",
    ))
    if paper_retrieval:
        candidates.extend((
            "paper-lookup",
            "lawful-paper-pdf-retriever",
            "nature-downloader",
        ))

    if _contains(prompt, (r"toàn bộ.{0,20}(pipeline|bài báo)", r"full academic pipeline")):
        candidates.append("academic-pipeline")
    if _contains(prompt, (r"debug", r"sửa lỗi", r"\bbug\b", r"failing test", r"lỗi.{0,20}hook")):
        candidates.extend(("systematic-debugging", "test-driven-development"))
    if _contains(prompt, (r"tạo.{0,20}(hình|ảnh|image)", r"generate.{0,20}image", r"chỉnh sửa ảnh")):
        candidates.append("imagegen")

    literature = _contains(prompt, (
        r"systematic.{0,12}(review|literature)",
        r"literature review",
        r"tổng quan.{0,12}(hệ thống|tài liệu)",
        r"\bprisma\b",
    ))
    research = literature or _contains(prompt, (
        r"\bresearch\b",
        r"tìm.{0,20}(nguồn|tài liệu|bài báo)",
        r"xác minh.{0,20}(nguồn|thông tin|sự kiện)",
        r"source discovery",
        r"tổng hợp thông tin",
    ))
    if research and not paper_retrieval:
        candidates.append("literature-review" if literature else "deep-research")

    if _contains(prompt, (
        r"\bviết\b",
        r"viết lại",
        r"chỉnh sửa.{0,20}(bài|phần|manuscript|text)",
        r"\b(edit|draft|rewrite)\b",
        r"manuscript",
        r"discussion|related work|abstract|introduction",
    )):
        candidates.append("scientific-writing")
    if _contains(prompt, (r"lập kế hoạch", r"task breakdown", r"\bplan\b")):
        candidates.append("planning-and-task-breakdown")
    if _contains(prompt, (r"\bgit\b", r"\bcommit\b", r"\bbranch\b", r"worktree")):
        candidates.append("git-workflow-and-versioning")
    return candidates


def _owner_for(prompt: str) -> str:
    research = _contains(prompt, (
        r"\bresearch\b",
        r"tìm.{0,20}(nguồn|tài liệu|bài báo)",
        r"xác minh",
        r"tổng hợp thông tin",
        r"literature review",
        r"systematic review",
        r"\bprisma\b",
        r"tải.{0,24}(pdf|bài báo|toàn văn|full.?text)",
        r"download.{0,24}(paper|pdf|full.?text)",
        r"full.?text",
    ))
    writing = _contains(prompt, (
        r"\bviết\b",
        r"viết lại",
        r"chỉnh sửa",
        r"\b(edit|draft|rewrite)\b",
        r"manuscript",
        r"discussion|related work|abstract|introduction",
    ))
    if research and writing:
        return "SPLIT: RESEARCH=GEMINI_RESEARCH; WRITING=CODEX_WRITING"
    if research:
        return "GEMINI_RESEARCH"
    return "CODEX_WRITING"


def _code_first_decision(prompt: str) -> Tuple[str, str]:
    """Recommend the cheapest safe reusable execution mode for a prompt."""
    if not prompt.strip():
        return "MANUAL", "empty or unreadable prompt cannot justify automation"

    create_automation = _contains(prompt, (
        r"\b(write|create|implement)\b.{0,24}\b(script|hook|tool|cli)\b",
        r"\b(viết|tạo|xây dựng|cài đặt)\b.{0,24}\b(script|hook|tool|cli|công cụ)\b",
        r"tái sử dụng.{0,24}(script|hook|tool|công cụ)",
        r"reus(?:e|able).{0,24}(script|hook|tool|cli)",
    ))
    repeatable_data_work = _contains(prompt, (
        r"\b(batch|bulk)\b",
        r"hàng loạt|lặp lại|nhiều lần",
        r"\b(parse|transform|normalize|deduplicat|validate|reconcile)\w*\b.{0,40}"
        r"\b(csv|json|xml|yaml|doi|record|file|data)\w*\b",
        r"\b(csv|json|xml|yaml|doi|record|file|data)\w*\b.{0,40}"
        r"\b(parse|transform|normalize|deduplicat|validate|reconcile)\w*\b",
        r"(kiểm tra|xác thực|đối soát|chuẩn hóa|loại).{0,35}"
        r"(hàng loạt|nhiều|toàn bộ|doi|bản ghi|file|dữ liệu|trùng)",
    ))
    if create_automation or repeatable_data_work:
        return (
            "WRITE_SCRIPT",
            "task has deterministic reusable steps that should be scripted and tested",
        )

    existing_automation = _contains(prompt, (
        r"\b(existing|available|project)\b.{0,24}\b(script|tool|api|cli|test|build)\b",
        r"\b(script|tool|api|cli|test|build)\b.{0,24}\b(existing|available|project)\b",
        r"(hiện có|có sẵn|của dự án).{0,24}(script|tool|api|cli|test|build|công cụ)",
        r"(script|tool|api|cli|test|build|công cụ).{0,24}(hiện có|có sẵn|của dự án)",
        r"\b(run|execute|compile|build|lint|format|test)\b",
        r"\b(chạy|thực thi|biên dịch)\b.{0,24}(test|script|tool|build|latex|công cụ)",
        r"\b(api|cli)\b",
        r"\b(research|lookup|download|search)\b",
        r"tìm.{0,20}(nguồn|tài liệu|bài báo)|tra cứu|tải.{0,20}(pdf|bài báo)",
    ))
    if existing_automation:
        return (
            "REUSE_EXISTING",
            "an existing tool, script, API, or command should be verified and reused first",
        )

    return (
        "MANUAL",
        "task primarily requires human judgment, communication, or one-off prose work",
    )


def route_prompt(prompt: str, catalog: Mapping[str, Path]) -> Route:
    """Select an advisory route with one primary and at most two supports."""
    explicit, unknown = _explicit_mentions(prompt, catalog)
    candidates = explicit + _infer_candidates(prompt)
    selected: List[Skill] = []
    selected_names = set()
    selected_families = set()
    skipped_overlap: List[str] = []
    skipped_cap: List[str] = []

    for name in candidates:
        path = catalog.get(name)
        if path is None or name in selected_names:
            continue
        family = skill_family(name)
        pipeline_loaded = any(skill.name in PIPELINE_EQUIVALENTS for skill in selected)
        overlaps_pipeline = (
            pipeline_loaded and name in PIPELINES_ORCHESTRATED_BY_ACADEMIC
        )
        if overlaps_pipeline or (family is not None and family in selected_families):
            if name not in skipped_overlap:
                skipped_overlap.append(name)
            continue
        if len(selected) >= MAX_SKILLS:
            if name not in skipped_cap:
                skipped_cap.append(name)
            continue
        selected.append(Skill(name=name, path=Path(path)))
        selected_names.add(name)
        if family is not None:
            selected_families.add(family)

    reason = ""
    if not selected:
        if not prompt.strip():
            reason = "empty or unreadable prompt; no classification performed"
        elif unknown:
            reason = "named skill is not installed and no matching task skill was found"
        else:
            reason = "task does not require a specialized installed skill"
    code_first_mode, code_first_reason = _code_first_decision(prompt)
    return Route(
        owner=_owner_for(prompt),
        code_first_mode=code_first_mode,
        code_first_reason=code_first_reason,
        primary=selected[0] if selected else None,
        supporting=selected[1:],
        unknown_explicit=unknown,
        skipped_overlap=skipped_overlap,
        skipped_cap=skipped_cap,
        reason=reason,
    )


def render_route(route: Route) -> str:
    lines = [
        "ADVISORY_ONLY: true",
        f"OWNER: {route.owner}",
        f"CODE_FIRST_DECISION: {route.code_first_mode} — {route.code_first_reason}",
    ]
    if route.unknown_explicit:
        lines.append("UNKNOWN_EXPLICIT_SKILLS: " + ", ".join(route.unknown_explicit))
    if route.primary is None:
        lines.append("SKILLS: none — " + route.reason)
    else:
        lines.append("PRIMARY_SKILL: " + route.primary.name)
        supports = ", ".join(skill.name for skill in route.supporting) or "none"
        lines.append("SUPPORTING_SKILLS: " + supports)
        selected = [route.primary, *route.supporting]
        lines.append("SKILLS: " + ", ".join(skill.name for skill in selected))
        for skill in selected:
            lines.append(f"READ_FULL_SKILL_MD: {skill.path} before action")
    if route.skipped_overlap:
        lines.append("SKIPPED_OVERLAP: " + ", ".join(route.skipped_overlap))
    if route.skipped_cap:
        lines.append("SKIPPED_CAP: " + ", ".join(route.skipped_cap))
    lines.append("NOTE: suggestion only; classification uncertainty never blocks the task")
    return "\n".join(lines)


def main() -> int:
    try:
        payload = json.load(sys.stdin)
        if not isinstance(payload, Mapping):
            payload = {}
        prompt = extract_prompt(payload)
        route = route_prompt(prompt, discover_catalog())
    except Exception as error:  # The advisory hook must never block user work.
        route = Route(
            owner="CODEX_WRITING",
            reason=f"router could not classify prompt ({type(error).__name__})",
        )
    print(render_route(route))
    return 0


if __name__ == "__main__":
    sys.exit(main())
