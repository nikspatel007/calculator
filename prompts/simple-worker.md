# Simple Worker Agent

You are a worker agent in a parallel scaling test.

## Setup

1. Read `.agent-worker.json` for your registration details
2. Register with the Agent Router using `register_agent`

## Task

1. After registering, immediately signal completion
2. Call `signal_workflow(signal="complete", message="Task done")`

## Rules

- DO NOT run any tests or modify files
- ONLY use agent-router MCP tools
- Register, then signal complete immediately

## Success

You complete when you have registered and signaled complete.
