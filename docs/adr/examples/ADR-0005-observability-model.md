---
id: ADR-0005
title: Define unified observability model for AI-assisted Salesforce workflows
status: accepted
date: 2026-02-18
owners:
  - sre-architecture
context: |
  Teams need consistent telemetry for quality, latency, and incident triage.
decision: |
  Instrument request lifecycle with shared trace identifiers, quality metrics, and alert thresholds.
consequences: |
  Faster triage and measurable reliability, with additional telemetry storage and governance work.
---

# ADR-0005: Define unified observability model for AI-assisted Salesforce workflows

## Context
Limited cross-system observability slows root-cause analysis.

## Decision
Adopt a common telemetry schema and alerting model.

## Consequences
Better operations posture and clearer SLO ownership.
