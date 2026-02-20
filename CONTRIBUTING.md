# Contributing

Thanks for contributing to the Salesforce AI Architecture Kit.

## Contribution Standards

- Keep artifacts practical and reusable for enterprise teams.
- Follow naming and schema contracts documented in `README.md`.
- Keep architecture rationale explicit and testable.
- Avoid tool-vendor lock-in language where possible.

## Pull Request Process

1. Open an issue first for major additions.
2. Keep each PR focused on one architecture topic.
3. Run `python3 tools/validate_docs.py` before opening PR.
4. Complete the architecture review checklist in the PR template.

## ADR Conventions

- Use `docs/adr/templates/ADR-TEMPLATE.md` as the source template.
- Keep status lifecycle clear: `proposed`, `accepted`, `superseded`, `deprecated`.
- Link related diagrams and patterns.

## Pattern Conventions

Each pattern file must include:

- `Problem`
- `When to Use`
- `When Not to Use`
- `Tradeoffs`
- `Diagram`
- `Controls`

## Diagram Conventions

- Store Mermaid source in `docs/diagrams/*.mmd`.
- Use naming format: `<domain>-<scenario>-v1.mmd`.
- Keep diagrams scoped; split large flows into focused files.
