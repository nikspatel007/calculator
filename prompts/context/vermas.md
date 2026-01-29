# VerMAS Project Context

## Project Name

**VerMAS** (Verification Multi-Agent System) - A platform for orchestrating AI coding agents that hold each other accountable.

## Problem Statement

Solo AI coding agents make mistakes, hallucinate, and don't catch their own errors. Code review by humans is slow and doesn't scale. We need a system where multiple AI agents review and challenge each other, producing better outcomes than any single agent.

## Current State

**Working prototype with core functionality:**
- Unified worker (Temporal + Agent Router)
- Dev-QA workflow with auto-merge
- Parallel task execution with dependency enforcement
- Dashboard for monitoring workflows
- Hierarchical task management

**In progress:**
- Package system for domain bundles
- Human approval gates
- Executive planning workflow

## Target Users

1. **Solo developers** who want AI assistance with built-in quality checks
2. **Small teams** who can't afford dedicated QA but need code quality
3. **AI-first development shops** building with agents at the core

## Key Assumptions

- Multiple agents reviewing each other catch more errors than one agent alone
- Developers will trust and adopt AI-generated code if there's a verification layer
- The overhead of multi-agent coordination is worth the quality improvement
- Temporal provides the durability we need without rebuilding it

## Constraints

- Must work with existing AI models (Claude, Codex, GPT)
- Must integrate with standard dev tools (git, tmux, CLI)
- Single developer building this (Nik)
- No dedicated infrastructure budget initially

## Success Criteria

- AI-generated code passes human review with minimal changes
- Developers trust the system enough to merge without manual review
- Catch errors that a single agent would have missed
- Reduce time from task to merged code

## Open Questions

- What's the right balance between agent autonomy and human oversight?
- How do we measure "quality" of AI-generated code objectively?
- What domains benefit most from multi-agent verification?
- How do we handle disagreement between agents?
- What's the pricing model for different user segments?

---

## For the Team

Each executive should read this and apply their lens:

- **Strategist:** Is "agents reviewing agents" the right north star? What's the 5-year vision?
- **Product:** Which user segment should we focus on first? What's their workflow today?
- **Business:** Who else is doing this? What's the market size for AI dev tools?
- **Growth:** Where do developers hang out? How do we get early adopters?
- **Critic:** What if agents just agree with each other? What if the overhead kills productivity?
