# Task: {task_id}

## Task Description

{task}

## Your Environment

- **Working Directory**: {worktree_path}
- **Agents**: {agents}
- **Roles**: {agent_roles}
- **Workflow ID**: {workflow_id}

## Important Rules

**ONE TASK AT A TIME:**
- Work ONLY on the task described above
- After signaling completion, WAIT

**WORKFLOW RULES:**
- Do NOT create marker files (DONE.md, QA_APPROVED.md, etc.)
- Use ONLY `signal_workflow` to indicate completion
- Follow your role-specific prompt instructions
