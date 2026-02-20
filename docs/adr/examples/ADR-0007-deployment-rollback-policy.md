---
id: ADR-0007
title: Enforce deployment and rollback policy for AI-enabled releases
status: accepted
date: 2026-02-18
owners:
  - release-architecture
context: |
  AI and workflow updates can have broad impact and require rapid rollback capability.
decision: |
  Require dry-run validation, staged promotion, and pre-defined rollback triggers for production releases.
consequences: |
  Reduces blast radius and MTTR; adds release process rigor.
---

# ADR-0007: Enforce deployment and rollback policy for AI-enabled releases

## Context
Uncontrolled rollout of AI changes can affect mission-critical processes.

## Decision
Apply release gates with mandatory rollback planning.

## Consequences
Safer releases and faster incident recovery.
