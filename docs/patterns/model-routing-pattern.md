# Model Routing Pattern

## Problem

Single-model strategies can be expensive or underperform on mixed workloads.

## When to Use

Use when tasks vary in latency, complexity, and compliance sensitivity.

## When Not to Use

Do not use when one model consistently meets all constraints.

## Tradeoffs

Optimizes cost/performance but increases routing logic complexity.

## Diagram

Reference: [system context](../diagrams/system-context-v1.mmd)

## Controls

Route by risk class, task type, and response quality policy.
