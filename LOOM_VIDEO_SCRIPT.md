# Project Chimera - Loom Video Script

**Duration:** ~5 minutes  
**Objective:** Demonstrate Spec Structure, Failing Tests, and IDE Agent Context

---

## SCENE 1: Introduction (30 seconds)

**[VISUAL: Dashboard intro with yellow theme]**

**[HOST on camera]**

"Hey everyone! Today I'm going to walk you through Project Chimera — an Autonomous AI Influencer Network built with the FastRender Swarm Architecture. By the end of this video, you'll see our spec structure, running failing tests, and how our IDE agent understands the project context."

**[VISUAL: Quick shots of each tab in the dashboard]**

---

## SCENE 2: Project Overview (45 seconds)

**[VISUAL: Documentation page on dashboard]**

"Project Chimera represents a pivot to building Autonomous AI Influencers — digital entities that research trends, generate content, and manage engagement without human intervention."

**[VISUAL: Architecture diagram in docs]**

"At its core, we use the FastRender Swarm Architecture with three roles:"

- **Planner Agents** — Decompose high-level goals into executable tasks
- **Worker Agents** — Execute atomic tasks using MCP tools
- **Judge Agents** — Validate outputs with confidence scoring

**[VISUAL: Three role icons in yellow/amber theme]**

---

## SCENE 3: Spec Structure Walkthrough (1 minute)

**[VISUAL: Open specs/ directory in VS Code]**

"Let's dive into our Spec-Driven Development approach. All specifications live in the `specs/` directory."

**[CAMERA: Screen recording]**

### specs/_meta.md
"This is our master specification — the vision, constraints, and success criteria."

**[Show file content]**
```
# Project Chimera - Meta Specification

Vision: Build Autonomous AI Influencers capable of research, 
content generation, and engagement management.

Constraints:
- Spec-Driven Development (no code without specs)
- Traceability via our MCP 
- Git Hygiene (2 commits/day)
```

### specs/functional.md
"User stories written from the agent's perspective."

**[Show user stories]**
```
As an Autonomous Influencer Agent,
I need to fetch and analyze trending topics...
As a Human Operator,
I need to review and approve content...
```

### specs/technical.md
"The meat — API contracts, database schema, and skill definitions."

**[Show API contract example]**
```
POST /api/v1/trends/fetch
Request: { platforms, category, limit, time_range }
Response: { status, trends, timestamp }
```

### specs/openclaw_integration.md
"Our bridge to the Agent Social Network."

**[Show message types]**
```
availability_announcement
trend_discovery_request
collaboration_request
```

---

## SCENE 4: OpenClaw Integration Plan (45 seconds)

**[VISUAL: OpenClaw integration docs]**

"Project Chimera integrates with OpenClaw to announce availability, discover trends from other agents, and avoid duplicate work."

**[Show protocol examples]**

"Every Chimera agent publishes its identity to the network:"

```json
{
  "agent_id": "chimera-001",
  "capabilities": ["trend_research", "content_generation"],
  "availability": { "status": "online", "capacity": 100 }
}
```

"And we support collaboration requests between agents for content crossovers."

**[VISUAL: Integration architecture diagram]**

---

## SCENE 5: Failing Tests (TDD Demo) (1 minute)

**[VISUAL: Terminal with pytest running]**

"Now let's demonstrate our Test-Driven Development approach. These tests define the 'empty slots' that AI agents must fill."

**[CAMERA: Screen recording]**

**[Run tests]**

```bash
make test
```

**[Show output]**
```
tests/test_trend_fetcher.py FAILED
tests/test_skills_interface.py FAILED
```

**[Explain]**

"These tests FAIL by design — they're testing API contracts that don't exist yet. When an AI agent reads these tests, it knows exactly what to build."

**[Show test code]**

```python
def test_trend_object_structure(self):
    """
    A Trend object MUST contain:
    - id: str
    - title: str
    - engagement_score: float
    """
    # This test defines the contract
    # Implementation comes later
```

"The tests validate:
1. API contract structure
2. Input/output contracts for each skill
3. Error handling requirements"

---

## SCENE 6: IDE Agent Context Demo (45 seconds)

**[VISUAL: Cursor IDE with .cursor/rules file]**

"Let's show how our IDE agent understands the project context."

**[CAMERA: Screen recording]**

**[Open .cursor/rules]**

"This file tells the AI agent how to behave."

**[Show key sections]**

```
# Prime Directive
NEVER Generate Code Without Checking Specs First

# Skill vs Tool Distinction
Skills: Runtime capabilities (skill_fetch_trends)
MCP Servers: Developer tools (git-mcp)
```

**[Demonstrate by asking the IDE agent a question]**

**[Type in Cursor/Claude]**

> "What is the FastRender Swarm Architecture and how should I implement a Worker agent?"

**[Show agent's response]**

```
Based on .cursor/rules and specs/technical.md:

The FastRender Swarm Architecture uses three roles:

1. PLANNER (Strategist)
   - Maintains campaign state
   - Generates task DAGs
   - Reacts to context changes

2. WORKER (Executor)
   - Stateless, ephemeral agents
   - Pulls tasks from TaskQueue
   - Calls MCP Tools

3. JUDGE (Gatekeeper)
   - Validates all outputs
   - Implements OCC (Optimistic Concurrency Control)
   - Routes to HITL if confidence < 0.70

To implement a Worker agent, see specs/technical.md#3.1
```

**[Explain]**

"The agent referenced our specs and gave a contextual answer. That's the power of proper context engineering!"

---

## SCENE 7: Frontend Dashboard Demo (30 seconds)

**[VISUAL: Walk through frontend tabs]**

"Finally, let's look at our yellow-themed management dashboard."

**[Show each tab quickly]**

1. **Fleet Dashboard** — Real-time agent status and task queue
2. **Campaign Composer** — Natural language goal setting
3. **HITL Reviews** — Human-in-the-loop approval system
4. **Agent Wallets** — Coinbase AgentKit integration
5. **Analytics** — Performance metrics
6. **Documentation** — All-in-one reference

**[VISUAL: Onboarding flow]**

"We even have an onboarding wizard with questions to personalize the experience!"

---

## SCENE 8: Conclusion (15 seconds)

**[HOST on camera]**

"And that's Project Chimera! We've built a spec-driven, test-first, containerized, and fully-governed infrastructure for autonomous AI influencers."

**[VISUAL: Final shot of dashboard]**

"Key takeaways:
- Spec-Driven Development prevents hallucination
- Failing tests define the implementation contract
- Context engineering ensures AI agents stay aligned"

"Subscribe for more updates as we implement the skills!"

**[END SCREEN]**

---

## Technical Notes for Recording

### Screen Setup
- VS Code with specs/ directory visible
- Terminal ready for `make test`
- Cursor/Claude chat open
- Frontend dashboard in another tab

### Recording Tips
- Pause 2-3 seconds between scene transitions
- Use cursor highlights to draw attention
- Keep narration clear and concise
- Aim for 4:30-5:00 duration

### B-Roll to Capture
- [ ] Git commit history showing spec evolution
- [ ] MCP Sense telemetry connection
- [ ] Docker build process
- [ ] GitHub Actions CI/CD run

---

## Pre-Recording Checklist

- [ ] specs/ directory complete with 4 files
- [ ] .cursor/rules file created
- [ ] tests/ directory with failing tests
- [ ] Frontend dashboard running
- [ ] Onboarding wizard tested
- [ ] All npm dependencies installed
- [ ] Pytest configured and working
