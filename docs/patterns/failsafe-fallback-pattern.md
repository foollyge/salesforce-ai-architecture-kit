# Fail-Safe Fallback Pattern

## Problem

Failures without fallback create poor user experience and operational risk.

## When to Use

Use where high availability and graceful degradation are required.

## When Not to Use

Do not use where hard-fail is legally required.

## Tradeoffs

Reduces outage impact but can hide root causes if overused.

## Diagram

Reference: [incident response flow](../diagrams/ops-incident-response-flow-v1.mmd)

## Controls

Add confidence thresholds, escalation paths, and fallback observability.
