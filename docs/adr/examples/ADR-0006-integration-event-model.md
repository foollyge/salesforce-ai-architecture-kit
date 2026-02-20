---
id: ADR-0006
title: Standardize integration and event contracts for AI workflows
status: accepted
date: 2026-02-18
owners:
  - integration-architecture
context: |
  AI capabilities depend on dependable interfaces with external systems and internal event streams.
decision: |
  Use contract-first API and event schemas with versioning, idempotency, and explicit ownership.
consequences: |
  Reduces integration fragility; requires stronger schema governance.
---

# ADR-0006: Standardize integration and event contracts for AI workflows

## Context
Contract drift causes failed automations and unpredictable behavior.

## Decision
Publish versioned interface contracts and event ownership model.

## Consequences
Higher reliability and clearer accountability.
