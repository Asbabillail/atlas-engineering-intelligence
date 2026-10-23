# ATLAS architecture

## Why modular skills?

ATLAS routes to a small specialist workflow when a task needs it instead of putting an enormous instruction set into every interaction. This can reduce irrelevant instruction overhead, but actual token usage depends on the host.

```text
Natural language request
         |
         v
 atlas-core: interpret intent and authority
         |
         +--> atlas-build-debug   (code/tests)
         +--> atlas-frontend      (UI/UX)
         +--> atlas-security      (defensive review)
         +--> atlas-toolchain     (tools/research)
         +--> atlas-business      (product/CTO)
         |
         v
Available tools + permitted actions
         |
         v
Evidence-backed result + limitations
```

## Important principles

- Interpret colloquial prompts without forcing the user to specify frameworks or technical requirements.
- Read actual source before editing; avoid inventing files, errors, or tests.
- Use scoped tools appropriate to the work; do not assume GitHub, web, or deployments are connected.
- Ask before irreversible actions, public publishing, expense, or disclosure of private information.
- Run relevant tests when permitted; label unrun checks clearly.
- Be selective with extra dependencies, code rewrites, and redundant token consumption.

## Extensibility

Add new focus areas as `skills/<skill-name>/SKILL.md` with YAML frontmatter containing unique `name` and task-relevant `description`. Prefer small task-triggered references. Before distributing an expanded package, rerun the offline validator and manual acceptance tests.
