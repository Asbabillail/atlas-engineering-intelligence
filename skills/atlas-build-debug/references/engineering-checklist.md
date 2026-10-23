# Engineering completion checklist (situational)

For substantial code changes, inspect as appropriate:

- Requirements and existing behavior preserved; acceptance criteria mapped to changes.
- Data contracts; schema evolution and rollback; migrations with realistic seeds and indexes.
- Unit + integration + visual/browser smoke tests, relevant test isolation.
- Error behavior and accessibility, empty/loading/failure states.
- Trust boundaries, least privilege, secrets, authentication and authorization.
- SSR/client distinctions, caching, concurrency, idempotency and retry behavior.
- Observability, cost/quotas, flags, staged release and rollback.
- Repository cleanliness, build artifact hygiene, docs and reproducibility.

For unavailable checks, label "not run" and reason. Don't translate "static review looks fine" into "production-ready".
