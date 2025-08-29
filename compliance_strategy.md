# Compliance Strategy for Code-Based Automations

## Summary
This compliance strategy maps regulatory risks for code-first automations to mitigations, and explains how to track and prove compliance over time.

### Authoritative frameworks consulted
- National Institute of Standards and Technology (NIST) Cybersecurity Framework (CSF) 2.0. (NIST provides industry-standard guidance for Identify, Protect, Detect, Respond, and Recover functions). (NIST, 2024).  
- Regulation (EU) 2016/679 — General Data Protection Regulation (GDPR), for data protection obligations where processing of personal data occurs (European Parliament & Council, 2016).

## Key compliance concerns & mitigations
| Risk | Mitigation |
|---|---|
| Sensitive data exposure in logs | Log redaction, structured logs with classification, avoid writing PII to logs; apply log scrubbing pipeline. |
| Secrets leakage | Use central secret manager; rotate secrets periodically and enforce least privilege. |
| Lack of audit trail | Enforce commit signing, immutable logs, and correlate job runs to commit hashes + deployment tags. |
| Unapproved changes | Protected branches, required code review, and change approval workflows. |

## Proving Compliance (Evidence)
- **Structured logs** with retention policy; logs include `commit_hash`, `job_id`, `actor`.
- **Git history**: use tags/releases to show what code was deployed and when.
- **Configuration snapshots**: store environment snapshots (versions of dependencies, container image digests).
- **Access records**: IAM logs and GitHub audit logs.

## In-text citations
- The NIST Cybersecurity Framework provides guidance for organizing detection and response activities which we map to our monitoring and alerting design (National Institute of Standards and Technology [NIST], 2024).
- GDPR requires data minimization and purpose limitation; logs must be designed to avoid unnecessary personal data storage and to support redaction when needed (European Parliament & Council, 2016).

---

## References (APA 7)
National Institute of Standards and Technology. (2024). *The NIST Cybersecurity Framework (CSF) 2.0* (NIST CSWP 29). U.S. Department of Commerce. https://nvlpubs.nist.gov/nistpubs/CSWP/NIST.CSWP.29.pdf

European Parliament & Council of the European Union. (2016). *Regulation (EU) 2016/679 (General Data Protection Regulation)*. https://eur-lex.europa.eu/eli/reg/2016/679/oj
