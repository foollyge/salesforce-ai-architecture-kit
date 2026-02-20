# Prompt Management Pattern

## Problem

Prompt sprawl and untracked edits make behavior unstable across environments.

## When to Use

Use when teams maintain multiple prompt variants and require traceable releases.

## When Not to Use

Do not use for one-off prototypes with no production dependency.

## Tradeoffs

Adds governance overhead but enables rollback and reproducibility.

## Diagram

Reference: [runtime request flow](../diagrams/ai-runtime-request-flow-v1.mmd)

## Controls

Version prompts, require change reviews, and evaluate before promotion.
