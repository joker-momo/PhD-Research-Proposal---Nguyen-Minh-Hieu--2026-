"""Generate and audit the technical-survey tables and figure inputs."""
import argparse
import csv
import re
from collections import Counter
from pathlib import Path

HERE = Path(__file__).resolve().parent
SYNTHESIS = HERE.parent.parent / "restart_2026_11_26" / "synthesis/final_46"
DIMENSIONS = {
    "topology": {
        "peer": "Intra-swarm peers", "cluster": "Cluster or head--worker",
        "tier": "Air--edge or air--edge--cloud",
    },
    "unit": {
        "layer": "Sequential stages", "spatial": "Tiles, shards or tensor transport",
        "branch": "Graph or early exit", "adaptive": "Model or representation adaptation",
        "request": "Expert, request or state dispatch",
    },
    "optimizer": {
        "math": "Mathematical optimization", "heuristic": "Heuristic or auction",
        "rl": "Learning-led", "hybrid": "Hybrid solver",
        "rule": "System rule or descriptive model",
    },
    "resilience": {
        "analytic": "Modeled reliability or stress", "proactive": "Planned reassignment",
        "link": "Link disruption or fallback", "bench": "Controlled disconnect",
        "node": "Node unavailability", "none": "No eligible recovery test or mechanism",
    },
    "family": {
        "cnn": "CNN classifiers", "detector": "Detection models",
        "language": "Language models or MoE", "mixed": "Mixed model families",
        "other": "Other named models", "generic": "Generic or reference workload",
    },
    "evaluation": {
        "analytical": "Analytical", "sim": "Simulation or software",
        "trace": "Trace/profile-backed simulation", "bench": "Bench, emulation or hardware-in-loop",
        "flight": "Outdoor multi-UAV system",
    },
}
DOMAINS = (
    "System model", "Assumptions and constraints", "Reproducible configuration",
    "Baseline comparability", "Metric alignment", "Variability and sensitivity",
    "Network and mobility realism", "Claim bounds", "Artifact availability",
    "Limitations and declarations",
)
ESCAPES = {"&": r"\&", "%": r"\%", "#": r"\#", "_": r"\_", "$": r"\$"}
ROW_END = " " + chr(92) * 2


def read_rows(path, delimiter=","):
    with path.open(encoding="utf-8", newline="") as stream:
        return list(csv.DictReader(stream, delimiter=delimiter))


def tex(text):
    return "".join(ESCAPES.get(char, char) for char in text).replace("/", r"\allowbreak{}/")


def row(*cells):
    return " & ".join(cells) + ROW_END


def long_table(title, label, widths, headings, body):
    columns = "@{}" + "".join(r"Y{" + str(width) + r"\linewidth}" for width in widths) + "@{}"
    return "\n".join([
        r"\begingroup\fontsize{8}{10}\selectfont\setlength{\tabcolsep}{2.5pt}\renewcommand{\arraystretch}{1.17}",
        r"\begin{longtable}{" + columns + "}",
        r"\caption{" + title + r"}\label{" + label + "}" + ROW_END,
        r"\toprule", row(*headings), r"\midrule", r"\endfirsthead",
        r"\toprule", row(*headings), r"\midrule", r"\endhead",
        r"\midrule", r"\endfoot", r"\bottomrule", r"\endlastfoot",
        *body,
        r"\end{longtable}\endgroup",
        "",
    ])


def render():
    source = {r["report_id"]: r for r in read_rows(SYNTHESIS / "study_characteristics.csv")}
    coding = read_rows(HERE / "technical_coding.psv", "|")
    ids = [r["id"] for r in coding]
    if len(source) != 46 or len(ids) != len(set(ids)) or set(ids) != set(source):
        raise ValueError("Expected the 46 distinct included report IDs in the reconciled corpus")
    bib = (HERE / "references.bib").read_text()
    kinds = {key: kind for kind, key in re.findall(r"^@(\w+)\{(R\d+),", bib, re.M)}
    if set(kinds) != set(ids) or set(kinds.values()) - {"article", "inproceedings"}:
        raise ValueError("Bibliography and corpus differ")

    groups = {}
    macros = []
    for dimension, labels in DIMENSIONS.items():
        if set(r[dimension] for r in coding) - labels.keys():
            raise ValueError("Invalid category in " + dimension)
        groups[dimension] = {
            key: sorted(r["id"] for r in coding if r[dimension] == key) for key in labels
        }
        for key, members in groups[dimension].items():
            citation = r"\cite{" + ",".join(members) + "}" if members else ""
            macros.append(r"\expandafter\def\csname grp" + dimension + key + r"\endcsname{" +
                          f"{len(members)}/46" + ("~" + citation if citation else "") + "}")
            macros.append(r"\expandafter\def\csname num" + dimension + key + r"\endcsname{" +
                          str(len(members)) + "}")

    def ref(report_id):
        return r"\cite{" + report_id + r"}\newline\mbox{(" + source[report_id]["citation_year"] + ")}"

    sorted_rows = sorted(coding, key=lambda r: (
        list(DIMENSIONS["topology"]).index(r["topology"]), source[r["id"]]["citation_year"], r["id"]))
    architecture = long_table(
        "Architecture, workload, partitioning, and optimization across all 46 included studies. "
        "Rows follow primary topology and year. DP means dynamic programming.",
        "tab:architecture", [.075, .111, .169, .145, .151, .125, .139],
        ["Ref.", "Topology", "DNN / task", "Partition / dispatch", "Decisions",
         "Objective", "Solver"],
        [row(ref(r["id"]), tex(DIMENSIONS["topology"][r["topology"]]),
             *(tex(r[k]) for k in ("workload", "partition", "decisions", "objective", "solver")))
         for r in sorted_rows],
    )

    summary = read_rows(SYNTHESIS / "appraisal_summary.csv")
    code = {}
    for entry in summary:
        if entry["domain"] == "D09":
            for report_id in re.findall(r"R\d{4}", entry["included_report_ids"]):
                code[report_id] = entry["judgment"]
    if set(code) != set(ids):
        raise ValueError("Expected an artifact judgment for each report")
    short = {"YES": "Yes", "PARTIAL": "Partial", "NOT_REPORTED": "NR", "NO": "No",
             "NOT_APPLICABLE": "N/A"}

    modality = {"analytical": "Analytical", "sim": "Simulation", "trace": "Trace or profile sim.",
                "bench": "Bench or emulation", "flight": "Outdoor flight"}
    evaluation = long_table(
        "Evaluation modality, network and mobility, resilience, and artifact reporting for all "
        "46 studies. Artifact status records the D09 judgment. NR denotes not reported in the accepted evidence.",
        "tab:evaluation", [.075, .116, .170, .163, .156, .153, .077],
        ["Ref.", "Modality", "Hardware / simulator", "Network / mobility",
         "Disruption / failure", "Continuity action", "Code / data"],
        [row(ref(r["id"]), tex(modality[r["evaluation"]]),
             *(tex(r[k]) for k in ("platform", "channel_mobility", "disruption", "action")),
             short[code[r["id"]]])
         for r in sorted_rows],
    )

    appraisal = []
    bars = []
    statuses = ("YES", "PARTIAL", "NOT_REPORTED", "NO")
    for index, name in enumerate(DOMAINS, 1):
        counts = {line["judgment"]: int(line["numerator"])
                  for line in summary if line["domain"] == f"D{index:02}"}
        if sum(counts.get(status, 0) for status in statuses) != 46:
            raise ValueError("Appraisal denominator or status differs for " + name)
        values = [counts.get(status, 0) for status in statuses]
        appraisal.append(row(name, *(str(v) for v in values), f"{100 * values[0] / 46:.1f}"))
        bars.append(r"\appraisalbar{" + "}{".join([str(index), name, *(str(v) for v in values)]) + "}")

    venues = Counter((source[i]["citation_year"], kinds[i]) for i in ids)
    for year in range(2021, 2027):
        macros.append(r"\expandafter\def\csname yearJournal" + str(year) + r"\endcsname{" +
                      str(venues[str(year), "article"]) + "}")
        macros.append(r"\expandafter\def\csname yearConference" + str(year) + r"\endcsname{" +
                      str(venues[str(year), "inproceedings"]) + "}")

    manuscript = (HERE / "main.tex").read_text()
    analysis = manuscript.split(r"\section{Architectures, Partitioning, and Optimization}")[1]
    analysis = analysis.split(r"\section{Discussion, Open Challenges, and Future Research Agenda}")[0]
    mentions = set(re.findall(r"R\d{4}", " ".join(re.findall(r"\\cite\{([^}]+)\}", analysis))))
    for dimension, key in re.findall(r"\\groupcite\{(\w+)\}\{(\w+)\}", analysis):
        mentions.update(groups[dimension][key])
    for table in (architecture, evaluation):
        table_ids = re.findall(r"\\cite\{(R\d{4})\}", table)
        if len(table_ids) != 46 or set(table_ids) != set(ids):
            raise ValueError("A corpus table does not cite each study exactly once")
    if set(ids) - mentions:
        raise ValueError("Uncited in sections 4--5: " + str(sorted(set(ids) - mentions)))
    return {
        "technical_macros.tex": "\n".join(macros) + "\n",
        "technical_architecture.tex": architecture,
        "technical_evaluation.tex": evaluation,
        "technical_appraisal.tex": r"\newcommand{\technicalappraisalrows}{%" + "\n" + "\n".join(appraisal) + "}\n",
        "technical_appraisal_bars.tex": "\n".join(bars) + "\n",
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true", help="Fail if committed generated inputs differ")
    args = parser.parse_args()
    for name, content in render().items():
        path = HERE / name
        if args.check:
            if not path.exists() or path.read_text() != content:
                parser.exit(1, "Stale generated input: " + name + "\n")
        else:
            path.write_text(content)
    print("PASS: 46/46 studies in Tables 3 and 4 and sections 4--5. Ten appraisal domains.")


if __name__ == "__main__":
    main()
