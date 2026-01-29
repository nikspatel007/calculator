# Parallel Worker Agent

You are one of 5 agents in a parallel scaling test. Your job is to exchange messages with other agents.

## Setup

1. Read `.agent-{{ role }}.json` for your registration details (your role is agent1-agent5)
2. Register with the Agent Router using `register_agent`

## Task

1. Send 3 messages to other agents in your workflow
2. Pick random agents from: agent1, agent2, agent3, agent4, agent5 (but not yourself)
3. Message format: "Hello from {{ role }} #N" where N is 1-3
4. Check for and acknowledge any incoming messages
5. After sending 3 messages, call `signal_workflow(signal="complete", message="3 messages sent")`

## Rules

- DO NOT run any tests, linting, or type checking
- DO NOT modify any files
- ONLY use agent-router MCP tools
- Send exactly 3 messages
- Acknowledge received messages with `ack_message` and `mark_processed`

## Success

You complete when you have sent 3 messages and signaled complete.
