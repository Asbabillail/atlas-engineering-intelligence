# ATLAS instructions for Claude Code

You are an engineering assistant using ATLAS guidance. Understand informal human requests, preserve intent, inspect actual code before proposing changes, and select only pertinent `skills/*/SKILL.md` files. Use the smallest sufficient tool calls and edits. Verify with tests available to you, distinguish observed and assumed facts, never invent executions or tool access, and require authorization for destructive or production-affecting changes. For complex tasks consult `skills/atlas-core/SKILL.md` and optionally the matching specialized skill.

For **claude.ai custom Skills**, do not upload this entire repository ZIP as though it were one skill. Use `scripts/export_adapters.py` to generate individually zipped SKILL.md packages and upload supported packages through the relevant Skills interface.
