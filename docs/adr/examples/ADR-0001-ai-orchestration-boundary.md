---
id: ADR-0001
title: Define AI orchestration boundary between Salesforce and external services
status: accepted
date: 2026-02-18
owners:
  - enterprise-architecture
context: |
  Teams need consistent orchestration boundaries for prompts, tool-calling, and policy controls across Salesforce workloads.
decision: |
  Keep orchestration policy, routing, and identity context enforcement in a dedicated orchestration layer. Salesforce handles business records and transaction workflows.
consequences: |
  Improves separation of concerns and auditability. Adds one extra hop and operational dependency.
---

# ADR-0001: Define AI orchestration boundary between Salesforce and external services

## Context
Business workflows require a repeatable control point for model routing, prompt policy, and tool invocation.

## Decision
Adopt a thin orchestration layer with strict contracts to Salesforce data and event interfaces.

## Consequences
Higher governance quality and traceability, with moderate latency overhead.
