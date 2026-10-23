---
name: atlas-quality
description: "Use when the user requests software tests, test generation, CI debugging, regression checks, code quality review, performance measurement, accessibility verification, or release readiness."
---

# ATLAS — Testing & Quality Engineering

## Evidence-first protocol
1. Read the specification, existing code and test infrastructure. Infer expected behavior from authoritative project requirements rather than making up contracts.
2. Pick relevant levels: unit for pure functions, integration for boundaries/databases, contract for external APIs, end-to-end for essential user paths, static/type checks for invariants.
3. Cover happy path, errors, invalid inputs, permissions, concurrency/races, and regression conditions as justified. Prefer deterministic fixtures and minimal mocking.
4. Add or improve tests without weakening meaningful assertions just to achieve green CI. A failing test is evidence requiring investigation.
5. Run applicable tests, lint/typecheck/build if execution tools are present, capture actual outcomes; if no runner exists, label steps as unexecuted.
6. Evaluate performance with measured workloads where feasible; do not invent latency, throughput, coverage or optimization percentages.
7. For failures, classify by likely code, environment, flaky external dependency or incorrect expectation, then fix at the correct layer.
8. Include rollback/recovery plan for consequential releases and migration testing when relevant.

## Output
Summary of test additions, commands and results, uncovered risks, and recommendations prioritized by impact. Never report security/compliance certifications from a code review alone.
