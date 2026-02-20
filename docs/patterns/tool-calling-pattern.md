# Tool-Calling Orchestration Pattern

## Problem

Unbounded tool invocation can cause side effects and policy breaches.

## When to Use

Use for tasks requiring deterministic actions against systems of record.

## When Not to Use

Do not use for read-only informational responses.

## Tradeoffs

Improves reliability but increases contract design complexity.

## Diagram

Reference: [integration event flow](../diagrams/integration-event-driven-flow-v1.mmd)

## Controls

Define strict input schemas, auth scopes, and idempotency.
