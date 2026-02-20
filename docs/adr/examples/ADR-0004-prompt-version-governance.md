---
id: ADR-0004
title: Version prompts and evaluation criteria as governed artifacts
status: accepted
date: 2026-02-18
owners:
  - ai-governance
context: |
  Prompt changes can materially alter behavior but are often untracked.
decision: |
  Treat prompts as versioned artifacts with change control, approvals, and regression evaluations.
consequences: |
  Enables reproducibility and safer rollout, but introduces review overhead.
---

# ADR-0004: Version prompts and evaluation criteria as governed artifacts

## Context
Prompt drift has caused inconsistent production behavior.

## Decision
Implement versioning, approvals, and release gates for prompt updates.

## Consequences
Improved stability and governance at the cost of slower change velocity.
