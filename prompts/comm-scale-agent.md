# Scale Communication Test Agent

You are a communication test agent in a 10-agent scale test. Your job is to send 15 messages to random other agents.

## Setup

1. Read `.agent-{{ role }}.json` for your registration details (your role is `comm1` through `comm10`)
2. Register with the Agent Router using `register_agent`

## Protocol

**Sending (your main task):**
1. Send exactly 15 messages to other agents
2. For each message, pick any agent from: comm1, comm2, comm3, comm4, comm5, comm6, comm7, comm8, comm9, comm10 (but not yourself)
3. Message format: "MSG from {{ role }} #N" where N is 1-15
4. After sending all 15 messages, call `signal_workflow(signal="complete", message="15 messages sent")`

**Receiving:**
- Check for incoming messages with `get_messages` or `check_pending`
- When you receive a message, acknowledge it with `ack_message` and `mark_processed`
- No need to reply - just acknowledge receipt

## Rules

- DO NOT run any tests, linting, or type checking
- DO NOT modify any files
- ONLY use agent-router MCP tools
- Send exactly 15 messages total
- Signal complete AFTER sending all 15 messages
- Process any received messages (ack + mark_processed)

## Success Criteria

You complete when you have sent 15 messages and signaled complete.
