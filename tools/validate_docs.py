#!/usr/bin/env python3
"""
Documentation validator for Salesforce AI Architecture Kit.

Checks:
1) ADR filename and frontmatter contract
2) Pattern required sections
3) Mermaid naming and structural syntax checks
4) Markdown relative links and anchors
5) Docs style checks (no tabs, no trailing whitespace)
"""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parents[1]
ADR_EXAMPLES = ROOT / "docs" / "adr" / "examples"
PATTERNS = ROOT / "docs" / "patterns"
DIAGRAMS = ROOT / "docs" / "diagrams"

ADR_REQUIRED_KEYS = {
    "id",
    "title",
    "status",
    "date",
    "owners",
    "context",
    "decision",
    "consequences",
}

PATTERN_SECTIONS = [
    "Problem",
    "When to Use",
    "When Not to Use",
    "Tradeoffs",
    "Diagram",
    "Controls",
]

MERMAID_STARTS = (
    "flowchart",
    "graph",
    "sequenceDiagram",
    "classDiagram",
    "stateDiagram",
    "erDiagram",
    "journey",
    "gantt",
    "pie",
    "mindmap",
    "timeline",
    "quadrantChart",
    "requirementDiagram",
    "gitGraph",
)

FRONTMATTER_RE = re.compile(r"^---\n(.*?)\n---\n", re.DOTALL)
LINK_RE = re.compile(r"\[[^\]]+\]\(([^)]+)\)")
HEADING_RE = re.compile(r"^(#{1,6})\s+(.+?)\s*$", re.MULTILINE)


@dataclass
class Finding:
    path: Path
    message: str


def slugify_heading(text: str) -> str:
    slug = text.strip().lower()
    slug = re.sub(r"[^a-z0-9\s-]", "", slug)
    slug = re.sub(r"\s+", "-", slug)
    slug = re.sub(r"-+", "-", slug)
    return slug


def parse_frontmatter(text: str) -> tuple[dict[str, str], str]:
    m = FRONTMATTER_RE.match(text)
    if not m:
        return {}, text
    fm_block = m.group(1)
    body = text[m.end() :]
    data: dict[str, str] = {}
    for line in fm_block.splitlines():
        if ":" in line and not line.lstrip().startswith("-"):
            k, v = line.split(":", 1)
            data[k.strip()] = v.strip()
    return data, body


def collect_markdown_files() -> list[Path]:
    return sorted(ROOT.rglob("*.md"))


def check_style(path: Path, text: str) -> list[Finding]:
    findings: list[Finding] = []
    for i, line in enumerate(text.splitlines(), start=1):
        if "\t" in line:
            findings.append(Finding(path, f"line {i}: tab character not allowed"))
        if line.rstrip(" \n\r") != line:
            findings.append(Finding(path, f"line {i}: trailing whitespace"))
    return findings


def check_adr_contract(path: Path, text: str) -> list[Finding]:
    findings: list[Finding] = []
    if not re.match(r"^ADR-\d{4}-[a-z0-9-]+\.md$", path.name):
        findings.append(Finding(path, "ADR filename must match ADR-XXXX-short-title.md"))

    fm, body = parse_frontmatter(text)
    if not fm:
        findings.append(Finding(path, "missing YAML frontmatter"))
        return findings

    missing = ADR_REQUIRED_KEYS - set(fm.keys())
    for key in sorted(missing):
        findings.append(Finding(path, f"missing frontmatter key: {key}"))

    for section in ["Context", "Decision", "Consequences"]:
        if re.search(rf"(?m)^##\s+{re.escape(section)}\s*$", body) is None:
            findings.append(Finding(path, f"missing section: {section}"))

    return findings


def check_pattern_contract(path: Path, text: str) -> list[Finding]:
    findings: list[Finding] = []
    for section in PATTERN_SECTIONS:
        if re.search(rf"(?m)^##\s+{re.escape(section)}\s*$", text) is None:
            findings.append(Finding(path, f"missing required section: {section}"))
    return findings


def check_mermaid(path: Path, text: str) -> list[Finding]:
    findings: list[Finding] = []
    if not re.match(r"^[a-z0-9-]+-v1\.mmd$", path.name):
        findings.append(Finding(path, "filename must match <domain>-<scenario>-v1.mmd"))

    lines = [ln.strip() for ln in text.splitlines() if ln.strip()]
    if not lines:
        findings.append(Finding(path, "empty mermaid file"))
        return findings

    if not any(lines[0].startswith(prefix) for prefix in MERMAID_STARTS):
        findings.append(Finding(path, "first non-empty line must start with a Mermaid diagram keyword"))

    return findings


def headings_for(path: Path) -> set[str]:
    text = path.read_text(encoding="utf-8")
    return {slugify_heading(m.group(2)) for m in HEADING_RE.finditer(text)}


def check_links(path: Path, text: str, heading_cache: dict[Path, set[str]]) -> list[Finding]:
    findings: list[Finding] = []
    for link in LINK_RE.findall(text):
        link = link.strip()
        if not link or link.startswith(("http://", "https://", "mailto:")):
            continue
        if link.startswith("#"):
            anchor = link[1:]
            if slugify_heading(anchor) not in heading_cache[path]:
                findings.append(Finding(path, f"unresolved local anchor: {link}"))
            continue

        target, _, anchor = link.partition("#")
        target_path = (path.parent / target).resolve()
        if not target_path.exists():
            findings.append(Finding(path, f"broken relative link: {link}"))
            continue
        if anchor and target_path.suffix.lower() == ".md":
            if target_path not in heading_cache:
                heading_cache[target_path] = headings_for(target_path)
            if slugify_heading(anchor) not in heading_cache[target_path]:
                findings.append(Finding(path, f"unresolved anchor in link: {link}"))

    return findings


def main() -> int:
    findings: list[Finding] = []

    md_files = collect_markdown_files()
    heading_cache: dict[Path, set[str]] = {p.resolve(): headings_for(p.resolve()) for p in md_files}

    for path in md_files:
      resolved = path.resolve()
      text = resolved.read_text(encoding="utf-8")
      findings.extend(check_style(resolved, text))
      findings.extend(check_links(resolved, text, heading_cache))

    for path in sorted(ADR_EXAMPLES.glob("*.md")):
        text = path.read_text(encoding="utf-8")
        findings.extend(check_adr_contract(path, text))

    for path in sorted(PATTERNS.glob("*.md")):
        text = path.read_text(encoding="utf-8")
        findings.extend(check_pattern_contract(path, text))

    for path in sorted(DIAGRAMS.glob("*.mmd")):
        text = path.read_text(encoding="utf-8")
        findings.extend(check_mermaid(path, text))

    if findings:
        print("Validation failed:")
        for f in findings:
            print(f"- {f.path}: {f.message}")
        return 1

    print("Validation passed: ADR, pattern, diagram, link, and style checks are clean.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
