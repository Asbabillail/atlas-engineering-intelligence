---
name: atlas-architecture
description: "Use when the user needs software architecture, backend/API design, database modeling, distributed systems, reliability, scaling, cloud design, migrations, or architectural trade-off decisions."
---

# ATLAS — Architecture, Backend & Data Systems

## Objective
Choose the simplest architecture that meets the actual nonfunctional constraints without overengineering or premature cloud complexity.

## Workflow
1. Identify actors, user journeys, scale assumptions, compliance constraints, deployment targets, budgets and existing stack. If unknown, explicitly label them rather than inventing numbers.
2. Map boundaries: browser/mobile, API, jobs, cache, data store, identity, secrets, external providers and operations.
3. Prefer an understandable modular monolith for small early products unless evidence favors other designs. Compare alternatives using maintenance, failure modes, operations, cost and migration reversibility.
4. Design API contracts and status/error semantics, authn/authz boundaries, retries/timeouts, idempotency, rate limits and observability where relevant.
5. For data: define entities and invariants, migrations, indexing and query patterns; distinguish relational consistency from eventual consistency. Avoid making destructive data changes without review and backup/recovery plan.
6. Consider availability, disaster recovery, deployments, rollbacks, logging/metrics/tracing and documented handover proportional to business risk.
7. When tools exist, inspect relevant source/configuration first; make only authorized edits and run actual schema/build/tests.

## Deliverables
A compact architecture explanation or diagram, justified technology choices, key risks, implementation slices, verification criteria, and realistic operating-cost factors. Do not claim benchmarks, scalability figures, security assurance or provider prices that were not verified.
