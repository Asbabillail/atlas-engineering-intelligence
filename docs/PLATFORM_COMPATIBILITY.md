# ATLAS v1.1.0 — Cross-platform compatibility

ATLAS contains portable *instruction skills*, not a universal executable plugin. There is no single ZIP that installs automatically into every consumer chatbot. Each platform defines its own skill/configuration workflow and eligibility.

| Platform | ATLAS entrypoint | How to use | What it does NOT grant |
| --- | --- | --- | --- |
| ChatGPT / Codex Plugins | `plugin.json` + `skills/*/SKILL.md` | Install a compatible plugin release where available, or use the already-owned private plugin | No GitHub, terminal or deployment permission unless separately connected |
| ChatGPT legacy Custom GPT | `adapters/chatgpt/INSTRUCTIONS.md` | Copy into an eligible existing GPT's Instructions | Doesn't create a new GPT or enable new tools; new personal GPT creation may be unavailable |
| Claude.ai | `dist/claude-skills/*.zip` built with export script | Import individual skill ZIPs through supported Claude Skills controls, subject to plan/features | Does not instantly install whole ATLAS plugin or connect data sources |
| Claude Code | `CLAUDE.md` / `skills/` | Use repo-level CLAUDE.md; for automatic skills place copies of chosen `skills/<name>/` in `.claude/skills/` (or `~/.claude/skills/`) | Does not grant MCP or shell privileges by itself |
| Gemini Gem | `adapters/gemini/GEM_INSTRUCTIONS.md` | Paste into a Gem's Instructions; relevant docs can be uploaded as knowledge | Not a Gemini CLI extension or server |
| Gemini CLI | `gemini-extension.json` + `GEMINI.md` | Install the GitHub repository as an extension per CLI docs, or use GEMINI.md as project context | Does not automatically enable external credentials |
| GitHub Copilot | `.github/copilot-instructions.md` | Copy to a *target software project* to influence repository-context Copilot work | Does not install ATLAS as GitHub App |
| Codex and supporting coding agents | `AGENTS.md` | Copy into the *target project* or consume with compatible agents | Applicability depends on host discovery mechanisms |

## Installation notes

- You can download the GitHub source and review every instruction before using it.
- Generate per-skill Claude packages: `python scripts/export_adapters.py`. Use the individual ZIP files created in `dist/claude-skills/`.
- Do not point a whole-project-wide GEMINI.md/CLAUDE.md at untrusted repositories and expect it to override user/platform safety rules.
- Model behavior is probabilistic. Prompts do not automatically make a model a professional programmer, grant access to private data, or guarantee correct code.

## Documentation references

- [ChatGPT Plugins documentation](https://learn.chatgpt.com/docs/skills-and-plugins)
- [OpenAI GPT availability and migration](https://help.openai.com/en/articles/8554397-creating-and-editing-gpts)
- [Claude Agent Skills](https://platform.claude.com/docs/en/agents-and-tools/agent-skills/overview)
- [Gemini Gems instructions](https://support.google.com/gemini/answer/15235603?hl=en)
- [Gemini CLI extensions](https://geminicli.com/docs/extensions/)
- [Gemini CLI GEMINI.md](https://geminicli.com/docs/cli/gemini-md/)
- [GitHub Copilot repository instructions](https://docs.github.com/en/copilot/concepts/prompting/response-customization)

Always check the latest host docs before relying on installation steps: features and eligibility change.
