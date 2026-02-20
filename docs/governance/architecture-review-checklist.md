# Architecture Review Checklist

Use this checklist before accepting architecture changes.

## Security

- [ ] Trust boundaries identified and diagrammed
- [ ] Authentication and authorization paths reviewed
- [ ] Secrets management and rotation approach documented

## Data

- [ ] Data classification defined
- [ ] PII handling and masking strategy documented
- [ ] Data lineage and ownership identified

## Latency and Performance

- [ ] End-to-end latency budget defined
- [ ] Throughput assumptions documented
- [ ] Degradation and fallback behavior specified

## Compliance

- [ ] Regulatory constraints identified
- [ ] Residency requirements addressed
- [ ] Audit evidence generation planned

## Observability

- [ ] Metrics and alerts defined
- [ ] Correlation IDs and tracing model documented
- [ ] Incident triage workflow linked

## Rollback and Resilience

- [ ] Rollback triggers and procedure documented
- [ ] Failure modes and blast radius assessed
- [ ] Runbook owners and SLAs assigned
