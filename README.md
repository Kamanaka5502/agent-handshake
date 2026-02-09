# agent-handshake

Preflight authority and intent gate before LLM reasoning.

Most agent failures happen because the model is asked to decide too much:

- Is this request valid?
- Is the user allowed to do this?
- What is the user trying to accomplish?

This project demonstrates a simple pattern:

Nothing reaches the LLM until authority and intent are deterministically resolved.

User → Handshake → Authority Check → Intent Resolution → LLM

## Core Idea

The model should never decide:
- whether a request is allowed
- what the user is trying to do

It should only decide how to respond after those are known.

## Why this exists

Typical agent flow:

User → LLM → Tools

This creates:
- hallucinated tool use
- unauthorized actions
- unclear intent
- brittle behavior

This pattern introduces a handshake layer that resolves:

- Who is the user?
- What are they allowed to do?
- What is their intent?

Before the model is ever involved.

## Philosophy

Authority decides if  
Intent decides what  
LLM decides how

Boring. Deterministic. Production-safe.
