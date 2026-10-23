---
name: atlas-security
description: "Use when the user requests defensive secure-code review, vulnerability analysis, threat modeling, repository security audit, or remediation of exposed secrets, authorization flaws, and risky application configurations."
---

# ATLAS — Defensive Security & Source Evidence

## Scope and operating modes

For ordinary development tasks, apply secure-by-default judgment without turning every task into an exhaustive penetration test. For focused security questions, perform focused read-only review. For explicit comprehensive repo audits, offer a scoped evidence-led audit using code/config and supported sandboxed checks.

Never treat a flashy security tool, a GitHub star count, or the output "0 findings" as proof of safety. The video refers to Cloudflare's `security-audit-skill`, an example of a source-first review workflow; the ATLAS plugin does not bundle, install, or run that external tool automatically.

## Threat boundary reasoning

A credible finding connects evidence to a real trust boundary:

- Lower-trust actor or input.
- Entry point and relevant code path.
- Missing or bypassed security control.
- Affected resource or identity.
- Concrete harmful behavior or demonstrable risk.

Do not mislabel a best-practice preference as a confirmed exploit. Clearly distinguish **confirmed**, **needs validation**, **informational**, and **not reproduced**. Severity must reflect demonstrated impact, not alarming language.

## Audit workflow

1. Determine user's authorized scope and systems in scope.
2. Review relevant source and configuration without exposing credentials.
3. Map inputs, authentication, authorization, secrets, API boundaries, storage and dependencies.
4. Prioritize likely high-impact paths. Inspect risky flows, not every file blindly.
5. Verify findings conservatively with bounded local tests only when safe isolation is available. Never test someone else's live systems or use production data.
6. Recommend the smallest trustworthy fix and focused regression tests.
7. Report affected files/lines, evidence, severity rationale, uncertainty, and validation gaps.

### Common review points

Server-side authorization and tenant isolation; auth/session boundaries; injection paths; untrusted deserialization; secrets exposure; API keys in client bundles; SSRF patterns; unsafe file uploads; CSRF and XSS protections where relevant; dependency vulnerabilities; logging/privacy exposure; access control for admin routes; rate limiting and misconfigurations.

Never copy live credentials into reports. Prefer dummy values and explicit redaction. When local sandbox controls cannot be established, use static review and mark dynamic validation unavailable rather than executing untrusted repository scripts.

## Reporting template

**Finding:** title, status, priority if confirmed, affected code/config, evidence, trust boundary, smallest effective fix, regression check. Include coverage limitations; "no confirmed findings in inspected files" is not "no vulnerabilities exist".

Do not claim that the plugin contains a vulnerability scanner or background monitor. It is an instruction-based review skill using only actually available tools.
