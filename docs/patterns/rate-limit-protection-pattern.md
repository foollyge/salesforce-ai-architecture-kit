# Rate Limit Protection Pattern

## Problem

Bursts can exceed model/API quotas and degrade user experience.

## When to Use

Use where external dependencies have strict quota constraints.

## When Not to Use

Do not use where workloads are low-volume and predictable.

## Tradeoffs

Improves stability but may throttle legitimate peak demand.

## Diagram

Reference: [identity and auth model](../diagrams/security-identity-auth-model-v1.mmd)

## Controls

Apply quotas, circuit breakers, and prioritized request classes.
