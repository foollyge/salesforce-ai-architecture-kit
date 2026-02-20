# Salesforce AI Architecture Kit

A public, tool-agnostic architecture template repository for Salesforce and AI ecosystems.

## What This Repository Provides

- Architecture Decision Record (ADR) framework and examples
- Reusable architecture pattern catalog
- Mermaid diagram blueprint pack
- Governance templates for architecture reviews and risk tracking
- CI validation for ADR contracts, links, Mermaid files, and docs style

## Audience

This repository is designed for architects, technical leads, and platform engineering teams.

## Quick Start

```bash
git clone https://github.com/<your-org>/salesforce-ai-architecture-kit.git
cd salesforce-ai-architecture-kit
python3 tools/validate_docs.py
```

## MVP Blueprint Pack

- 8 ADR examples under `docs/adr/examples/`
- 10 architecture patterns under `docs/patterns/`
- 12 Mermaid diagrams under `docs/diagrams/`
- Architecture review checklist and risk register template under `docs/governance/`

## Repository Layout

```text
.
├── docs/
│   ├── adr/
│   │   ├── templates/ADR-TEMPLATE.md
│   │   └── examples/ADR-*.md
│   ├── patterns/*.md
│   ├── diagrams/*.mmd
│   └── governance/
├── tools/validate_docs.py
└── .github/
    ├── PULL_REQUEST_TEMPLATE.md
    ├── ISSUE_TEMPLATE/
    └── workflows/validate-docs.yml
```

## How Teams Use This

1. Copy `docs/adr/templates/ADR-TEMPLATE.md` to create project decisions.
2. Start from relevant diagrams in `docs/diagrams/` and customize context.
3. Select patterns from `docs/patterns/` and adapt controls to your org.
4. Run `docs/governance/architecture-review-checklist.md` before merge.
5. Track decisions over time by updating ADR statuses.

## Validation Rules Enforced

- ADR files must use required frontmatter fields:
  `id`, `title`, `status`, `date`, `owners`, `context`, `decision`, `consequences`
- ADR filenames must follow: `ADR-XXXX-short-title.md`
- Pattern files must include sections:
  `Problem`, `When to Use`, `When Not to Use`, `Tradeoffs`, `Diagram`, `Controls`
- Mermaid files must be parseable by structural checks and naming convention:
  `<domain>-<scenario>-v1.mmd`
- Markdown links and anchors must resolve
- Docs style checks for tabs and trailing whitespace

## Contribution Flow

See `CONTRIBUTING.md` for contribution standards and review process.
