# Cache Strategy Pattern

## Problem

Repeated requests increase latency and infrastructure cost.

## When to Use

Use for frequent read-heavy prompts with acceptable staleness windows.

## When Not to Use

Do not use for high-volatility or strongly consistent outputs.

## Tradeoffs

Improves speed/cost at risk of stale outputs.

## Diagram

Reference: [multi-environment promotion](../diagrams/platform-multi-environment-promotion-v1.mmd)

## Controls

Use TTL, cache key governance, and invalidation playbooks.
