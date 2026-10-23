# Install and use ATLAS

ATLAS is currently a **skills-only** plugin; it does not require hosting a service.

## Option 1 — compatible ChatGPT plugin importer

1. Download a published release ZIP (or build one using `python scripts/package_plugin.py`).
2. Use the plugin import/upload feature *if your account or workspace provides it*.
3. Review imported skills and permissions. There is no remote MCP connection in this package.
4. Try `ATLAS, review the requirements for this feature...` or the everyday-language examples in the README.

Installation controls vary by account/workspace, product surface, and current plugin policies. An imported ZIP does not grant repository, browser, terminal, or deployment access; those require separate tools and authorization.

## Option 2 — browse or adapt the skills

Each `skills/<name>/SKILL.md` describes a reusable specialist workflow. Compatible agent hosts may have their own manual skills setup. Follow the host's documentation rather than assuming the plugin ZIP is directly installable everywhere.

## Build and validate locally

Python 3.10+ is recommended. Both helper scripts use the standard library only.

```bash
python scripts/validate_plugin.py
python scripts/package_plugin.py
```

Output: `dist/atlas-engineering-intelligence-v1.0.0.zip` with a single enclosing folder and a valid root `plugin.json` inside it.

## Expected limitations

- No integrated execution environment is bundled.
- Quality depends on the underlying language model, available context, tools, and user permissions.
- Security guidance is advisory, not a certification.
- Deployment, source modifications, and externally visible changes require applicable permissions and authorizations.

## ChatGPT public distribution

GitHub source visibility and ChatGPT's plugin-distribution process are separate. Publication to ChatGPT's public plugin directory may require listing details, a license/compliance review, eligible accounts, developer verification, and platform review. Do not advertise the repository as an official public ChatGPT listing until that process is completed.
