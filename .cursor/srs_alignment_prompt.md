# Project Chimera - SRS Alignment Prompt

**Version:** 1.0.0  
**Date:** 2025-02-04

This prompt is used by the IDE Agent (Cursor/Claude) to ensure all code aligns with the SRS requirements.

---

## System Context

You are working on **Project Chimera**, an Autonomous AI Influencer system. The system implements the FastRender Swarm Architecture with Planner, Worker, and Judge roles for autonomous behavior.

**Core Architectural Patterns:**
- **FastRender Swarm**: Hierarchical coordination with Planner (strategist), Worker (executor), Judge (gatekeeper)
- **MCP (Model Context Protocol)**: Universal connectivity to external APIs and data sources
- **Agentic Commerce**: Coinbase AgentKit integration for non-custodial wallets
- **Human-in-the-Loop (HITL)**: Confidence-based escalation with dynamic thresholds

---

## SRS Alignment Instructions

### 1. FastRender Architecture Compliance

When implementing agent components, you MUST follow the FastRender pattern:

**Planner Agent (The Strategist)**
- Maintains "Big Picture" state of campaigns
- Decomposes high-level goals into executable task DAGs
- Implements dynamic re-planning on context changes
- Spawns Sub-Planners for complex domains

**Worker Agent (The Executor)**
- Stateless, ephemeral agents for atomic tasks
- Pull single tasks from TaskQueue
- Execute using available MCP Tools
- No inter-Worker communication

**Judge Agent (The Gatekeeper)**
- Reviews every Worker output
- Implements Optimistic Concurrency Control (OCC)
- Has authority to: Approve, Reject, Escalate to HITL
- Validates against persona constraints and safety guidelines

**Reference:** SRS Section 3.1

### 2. MCP Integration Compliance

All external interactions MUST use MCP protocol:

**MCP Resources (Data Ingestion)**
- Pattern: `platform://resource/path`
- Examples: `twitter://mentions/recent`, `news://ethiopia/fashion/trends`
- Perception System polls resources for updates

**MCP Tools (Actions)**
- Pattern: `tool_name(args)`
- Examples: `generate_image()`, `send_transaction()`, `post_tweet()`
- Standardized across platforms

**MCP Prompts (Reasoning)**
- Reusable templates for internal reasoning
- Examples: `analyze_sentiment`, `extract_topics`

**Reference:** SRS Section 3.2

### 3. Persona Management (SOUL.md)

Every agent MUST have a SOUL.md file containing:

```yaml
---
name: Agent Name
id: agent_uuid
voice_traits:
  - Witty
  - Empathetic
  - Gen-Z Slang
directives:
  - Never discuss politics
  - Sustainability-focused
backstory: |
  Comprehensive narrative history...
```

**Reference:** SRS Section 4.1, FR 1.0

### 4. Hierarchical Memory System

Implement memory retrieval in this order:

1. **Short-Term (Redis)** - Last 1 hour of conversation/action
2. **Long-Term (Weaviate)** - Semantic queries against vector database
3. **Context Construction** - Assemble SOUL.md + Short-Term + Long-Term

**Reference:** SRS Section 4.1, FR 1.1

### 5. Human-in-the-Loop (HITL) Compliance

Implement confidence-based routing:

| Confidence Score | Action |
|------------------|--------|
| > 0.90 | Auto-Approve (no human needed) |
| 0.70 - 0.90 | Async Approval (human must approve) |
| < 0.70 | Reject/Retry (refine strategy) |

**Mandatory HITL Triggers:**
- Politics, Health Advice, Financial Advice, Legal Claims
- Any content triggering "Sensitive" topic filters

**Reference:** SRS Section 5.1, NFR 1.0-1.2

### 6. Agentic Commerce (Coinbase AgentKit)

Each agent MUST have:

**Non-Custodial Wallet**
- Private keys secured via encrypted secrets manager
- Injected at runtime, never logged

**Budget Governance (CFO Sub-Agent)**
- Enforces configurable budget limits (e.g., "$50/day")
- Rejects suspicious transactions
- Flags anomalies for human review

**Supported Actions:**
- `native_transfer`: Send ETH/USDC
- `deploy_token`: Deploy ERC-20 tokens
- `get_balance`: Check financial health

**Reference:** SRS Section 4.5, FR 5.0-5.2

### 7. Data Schema Compliance

**Task Schema (Planner → Worker)**
```json
{
  "task_id": "uuid-v4-string",
  "task_type": "generate_content | reply_comment | execute_transaction",
  "priority": "high | medium | low",
  "context": {
    "goal_description": "string",
    "persona_constraints": ["string"],
    "required_resources": ["mcp://..."]
  },
  "assigned_worker_id": "string",
  "created_at": "timestamp",
  "status": "pending | in_progress | review | complete"
}
```

**Reference:** SRS Section 6.2, Schema 1

---

## Verification Checklist

Before committing code, verify:

- [ ] Planner implements dynamic re-planning
- [ ] Workers are stateless and ephemeral
- [ ] Judge implements OCC (Optimistic Concurrency Control)
- [ ] All external APIs accessed via MCP Tools/Resources
- [ ] Persona defined in SOUL.md
- [ ] Memory retrieval follows Short-Term → Long-Term → Context order
- [ ] HITL routing matches confidence thresholds
- [ ] Financial transactions require CFO approval
- [ ] Task JSON matches Schema 1
- [ ] Code documented with docstrings
- [ ] Tests added for new functionality

---

**Cross-references**

- Refer to the detailed technical guidance in `specs/technical.md` for architecture, API contracts, deployment, and observability. Example sections:
  - Architecture overview: `specs/technical.md` — Architecture overview
  - APIs: `specs/technical.md` — APIs
  - Testing strategy: `specs/technical.md` — Testing strategy

Use these links when implementing components so the Planner/Worker/Judge roles align with the technical spec.


## Example: Correct Implementation

**Task:** Implement a content generation Worker

1. ✅ Read `specs/technical.md` → Understand Task Schema
2. ✅ Check `skills/skill_generate_caption/` → Follow skill contract
3. ✅ Verify persona in `SOUL.md` → Align tone/style
4. ✅ Check memory → Retrieve relevant past content
5. ✅ Call MCP tool → `generate_image()` or similar
6. ✅ Submit to Judge → Validate against safety guidelines
7. ✅ If confidence < 0.70 → Trigger HITL

**Wrong Approach:**
- Hardcode persona style without referencing SOUL.md
- Skip MCP layer and call APIs directly
- Skip Judge validation
- Not implement confidence scoring

---

## Questions?

If SRS is unclear:
1. Check `research/SRS.md` first
2. Reference `specs/technical.md` for implementation details
3. Ask for clarification before implementing

**Remember: Ambiguity is the enemy of AI. Clarify first, implement second.**
# Project Chimera - SRS Alignment Prompt

**Version:** 1.0.0  
**Date:** 2025-02-04

This prompt is used by the IDE Agent (Cursor/Claude) to ensure all code aligns with the SRS requirements.

---

## System Context

You are working on **Project Chimera**, an Autonomous AI Influencer system. The system implements the FastRender Swarm Architecture with Planner, Worker, and Judge roles for autonomous behavior.

**Core Architectural Patterns:**
- **FastRender Swarm**: Hierarchical coordination with Planner (strategist), Worker (executor), Judge (gatekeeper)
- **MCP (Model Context Protocol)**: Universal connectivity to external APIs and data sources
- **Agentic Commerce**: Coinbase AgentKit integration for non-custodial wallets
- **Human-in-the-Loop (HITL)**: Confidence-based escalation with dynamic thresholds

---

## SRS Alignment Instructions

### 1. FastRender Architecture Compliance

When implementing agent components, you MUST follow the FastRender pattern:

**Planner Agent (The Strategist)**
- Maintains "Big Picture" state of campaigns
- Decomposes high-level goals into executable task DAGs
- Implements dynamic re-planning on context changes
- Spawns Sub-Planners for complex domains

**Worker Agent (The Executor)**
- Stateless, ephemeral agents for atomic tasks
- Pull single tasks from TaskQueue
- Execute using available MCP Tools
- No inter-Worker communication

**Judge Agent (The Gatekeeper)**
- Reviews every Worker output
- Implements Optimistic Concurrency Control (OCC)
- Has authority to: Approve, Reject, Escalate to HITL
- Validates against persona constraints and safety guidelines

**Reference:** SRS Section 3.1

### 2. MCP Integration Compliance

All external interactions MUST use MCP protocol:

**MCP Resources (Data Ingestion)**
- Pattern: `platform://resource/path`
- Examples: `twitter://mentions/recent`, `news://ethiopia/fashion/trends`
- Perception System polls resources for updates

**MCP Tools (Actions)**
- Pattern: `tool_name(args)`
- Examples: `generate_image()`, `send_transaction()`, `post_tweet()`
- Standardized across platforms

**MCP Prompts (Reasoning)**
- Reusable templates for internal reasoning
- Examples: `analyze_sentiment`, `extract_topics`

**Reference:** SRS Section 3.2

### 3. Persona Management (SOUL.md)

Every agent MUST have a SOUL.md file containing:

```yaml
---
name: Agent Name
id: agent_uuid
voice_traits:
  - Witty
  - Empathetic
  - Gen-Z Slang
directives:
  - Never discuss politics
  - Sustainability-focused
backstory: |
  Comprehensive narrative history...
```

**Reference:** SRS Section 4.1, FR 1.0

### 4. Hierarchical Memory System

Implement memory retrieval in this order:

1. **Short-Term (Redis)** - Last 1 hour of conversation/action
2. **Long-Term (Weaviate)** - Semantic queries against vector database
3. **Context Construction** - Assemble SOUL.md + Short-Term + Long-Term

**Reference:** SRS Section 4.1, FR 1.1

### 5. Human-in-the-Loop (HITL) Compliance

Implement confidence-based routing:

| Confidence Score | Action |
|------------------|--------|
| > 0.90 | Auto-Approve (no human needed) |
| 0.70 - 0.90 | Async Approval (human must approve) |
| < 0.70 | Reject/Retry (refine strategy) |

**Mandatory HITL Triggers:**
- Politics, Health Advice, Financial Advice, Legal Claims
- Any content triggering "Sensitive" topic filters

**Reference:** SRS Section 5.1, NFR 1.0-1.2

### 6. Agentic Commerce (Coinbase AgentKit)

Each agent MUST have:

**Non-Custodial Wallet**
- Private keys secured via encrypted secrets manager
- Injected at runtime, never logged

**Budget Governance (CFO Sub-Agent)**
- Enforces configurable budget limits (e.g., "$50/day")
- Rejects suspicious transactions
- Flags anomalies for human review

**Supported Actions:**
- `native_transfer`: Send ETH/USDC
- `deploy_token`: Deploy ERC-20 tokens
- `get_balance`: Check financial health

**Reference:** SRS Section 4.5, FR 5.0-5.2

### 7. Data Schema Compliance

**Task Schema (Planner → Worker)**
```json
{
  "task_id": "uuid-v4-string",
  "task_type": "generate_content | reply_comment | execute_transaction",
  "priority": "high | medium | low",
  "context": {
    "goal_description": "string",
    "persona_constraints": ["string"],
    "required_resources": ["mcp://..."]
  },
  "assigned_worker_id": "string",
  "created_at": "timestamp",
  "status": "pending | in_progress | review | complete"
}
```

**Reference:** SRS Section 6.2, Schema 1

---

## Verification Checklist

Before committing code, verify:

- [ ] Planner implements dynamic re-planning
- [ ] Workers are stateless and ephemeral
- [ ] Judge implements OCC (Optimistic Concurrency Control)
- [ ] All external APIs accessed via MCP Tools/Resources
- [ ] Persona defined in SOUL.md
- [ ] Memory retrieval follows Short-Term → Long-Term → Context order
- [ ] HITL routing matches confidence thresholds
- [ ] Financial transactions require CFO approval
- [ ] Task JSON matches Schema 1
- [ ] Code documented with docstrings
- [ ] Tests added for new functionality

---

## Example: Correct Implementation

**Task:** Implement a content generation Worker

1. ✅ Read `specs/technical.md` → Understand Task Schema
2. ✅ Check `skills/skill_generate_caption/` → Follow skill contract
3. ✅ Verify persona in `SOUL.md` → Align tone/style
4. ✅ Check memory → Retrieve relevant past content
5. ✅ Call MCP tool → `generate_image()` or similar
6. ✅ Submit to Judge → Validate against safety guidelines
7. ✅ If confidence < 0.70 → Trigger HITL

**Wrong Approach:**
- Hardcode persona style without referencing SOUL.md
- Skip MCP layer and call APIs directly
- Skip Judge validation
- Not implement confidence scoring

---

## Questions?

If SRS is unclear:
1. Check `research/SRS.md` first
2. Reference `specs/technical.md` for implementation details
3. Ask for clarification before implementing

**Remember: Ambiguity is the enemy of AI. Clarify first, implement second.**
