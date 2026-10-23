# ATLAS Developer — Universal Software Engineering Intelligence

**v1.1.0 · Open source · MIT License**

ATLAS converts everyday human requests into scoped engineering plans and useful work. Instead of one bloated "god developer" prompt, it delivers **nine modular engineering skills** plus platform-specific adapters for major AI assistants and coding agents.

> ATLAS is a **skills/instructions framework**, not an autonomous programming runtime or a universal one-click install. Code execution, data access and deployment depend on the host and your permissions. Structural tests have passed; cross-model behavior is not yet benchmarked.

## What ATLAS can help with

- Understand slang, typos, informal questions and incomplete requirements without demanding professionally written prompts.
- Review and improve frontend/backend code, APIs and database architecture.
- Debug defects and verify fixes with available tests.
- Evaluate product scope, operating costs and long-term maintainability.
- Review defensive security and privacy risks without unsupported guarantees.
- Plan AI-agent workflows, RAG, model/tool use and evaluation.
- Select tools and context deliberately: **useful output per token**, not empty verbosity.

## Nine skills

| Skill | Responsibilities |
| --- | --- |
| `atlas-core` | Natural-language intent interpreter, orchestration, safe execution |
| `atlas-build-debug` | Implementation, debugging and regressions |
| `atlas-frontend` | UI/UX design, accessibility, performance |
| `atlas-security` | Defensive security and source-first auditing |
| `atlas-toolchain` | Tool selection, API/research discipline, cost-conscious workflows |
| `atlas-business` | MVP/product strategy, ROI, budget and viability |
| `atlas-architecture` | Backend, APIs, data modeling, cloud and migration design |
| `atlas-quality` | Test strategy, CI and evidence-based release checks |
| `atlas-agentic` | LLM applications, RAG, tool-calling agents and evaluations |

## Use with your favorite assistant

| Platform | Supported adapter |
| --- | --- |
| ChatGPT / Codex Plugins | `plugin.json` + `skills/` |
| Existing eligible ChatGPT Custom GPT | `adapters/chatgpt/INSTRUCTIONS.md` |
| Claude.ai custom Skills | individual ZIP exports from `scripts/export_adapters.py` |
| Claude Code | `CLAUDE.md` and skill source directories |
| Gemini Gem | `adapters/gemini/GEM_INSTRUCTIONS.md` |
| Gemini CLI | `gemini-extension.json` + `GEMINI.md` |
| GitHub Copilot | `.github/copilot-instructions.md` |
| Codex/AGENTS.md-capable agents | `AGENTS.md` |

**Read [platform compatibility and installation instructions](docs/PLATFORM_COMPATIBILITY.md).** Each product has its own eligibility, permissions, installation UI and execution capabilities. Publishing on GitHub does not make ATLAS automatically available inside every chatbot.

## Build and verify

Requires Python 3.10+; scripts use the standard library.

```bash
python scripts/validate_plugin.py
python scripts/package_plugin.py
python scripts/export_adapters.py
```

See [architecture](docs/ARCHITECTURE.md), [installation](docs/INSTALL.md), [manual acceptance scenarios](tests/CROSS_PLATFORM_ACCEPTANCE.md), and [contributing](CONTRIBUTING.md).

## License and contributing

ATLAS is distributed under the [MIT License](LICENSE). Review [security reporting](SECURITY.md) and [contribution guidelines](CONTRIBUTING.md) before opening issues or pull requests. This is community-authored guidance, not an official OpenAI, Google, Anthropic or GitHub product.
