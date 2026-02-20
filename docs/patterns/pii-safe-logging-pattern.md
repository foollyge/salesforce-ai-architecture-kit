# PII-Safe Logging Pattern

## Problem

Raw telemetry can expose sensitive data in logs and analytics systems.

## When to Use

Use for all AI request/response logging pipelines.

## When Not to Use

Do not use when no user/content data is captured.

## Tradeoffs

Protects compliance posture but reduces raw debugging visibility.

## Diagram

Reference: [observability pipeline](../diagrams/ops-observability-pipeline-v1.mmd)

## Controls

Tokenize/redact fields, apply retention controls, and audit access.
