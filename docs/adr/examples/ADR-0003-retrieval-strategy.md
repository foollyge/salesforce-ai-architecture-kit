---
id: ADR-0003
title: Adopt retrieval strategy with metadata filtering and freshness policy
status: accepted
date: 2026-02-18
owners:
  - platform-architecture
context: |
  AI responses require grounded enterprise data with controlled access and freshness guarantees.
decision: |
  Use retrieval with metadata filters, source ranking, and freshness windows tied to data classification.
consequences: |
  Improves factuality and governance; increases indexing and data pipeline responsibilities.
---

# ADR-0003: Adopt retrieval strategy with metadata filtering and freshness policy

## Context
Ungrounded responses reduce trust in AI-assisted workflows.

## Decision
Use a retrieval-first pattern for enterprise knowledge use cases.

## Consequences
Higher reliability with added data ops requirements.
