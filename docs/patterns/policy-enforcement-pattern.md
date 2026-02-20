# Policy Enforcement Gateway Pattern

## Problem

Inconsistent policy checks across teams produce compliance drift.

## When to Use

Use when multiple AI entry points share governance rules.

## When Not to Use

Do not use for isolated internal experiments with no production data.

## Tradeoffs

Centralized controls improve consistency but add dependency on gateway uptime.

## Diagram

Reference: [trust boundary map](../diagrams/security-trust-boundary-map-v1.mmd)

## Controls

Apply pre/post checks, denial logging, and policy version tracking.
