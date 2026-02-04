# Project Chimera - Autonomous AI Influencer System

## Overview
Project Chimera represents a pioneering initiative in building Autonomous AI Influencers—digital entities capable of researching trends, generating content, and managing engagement without human intervention.

## Mission
To create a robust, spec-driven engineering environment where Intent (Specs) is the source of truth, and Infrastructure (CI/CD, Tests, Docker) ensures reliability.

## Core Philosophies

### Spec-Driven Development (SDD)
We do not write implementation code until the Specification is ratified. We use the GitHub Spec Kit framework to ensure precision and eliminate ambiguity.

### Agentic Orchestration
- **Skills**: Reusable functions/scripts the agent calls (e.g., `download_video`, `transcribe_audio`)
- **MCP Servers**: External bridges for connectivity (e.g., Database connectors, API gateways)

### Traceability (MCP)
The Tenx MCP Sense server maintains a continuous "Black Box" flight recorder of all development activities.

## Project Structure

```
chimera/
├── specs/              # GitHub Spec Kit documents
│   ├── _meta.md       # High-level vision and constraints
│   ├── functional.md  # User stories and requirements
│   ├── technical.md   # API contracts, database schema
│   └── openclaw_integration.md
├── skills/            # Agent runtime skills
│   ├── skill_download_youtube/
│   ├── skill_transcribe_audio/
│   └── skill_generate_content/
├── tests/             # TDD test suite
│   ├── test_trend_fetcher.py
│   └── test_skills_interface.py
├── research/          # Research and architecture strategy
├── Dockerfile         # Containerization
├── Makefile          # Automation commands
├── .github/
│   └── workflows/    # CI/CD pipelines
└── .cursor/
    └── rules         # IDE agent context rules
```

## Quick Start

```bash
# Install dependencies
make setup

# Run tests
make test

# Verify spec alignment
make spec-check
```

## Documentation
- [SRS Document](./research/SRS.md)
- [Architecture Strategy](./research/architecture_strategy.md)
- [Tooling Strategy](./research/tooling_strategy.md)

## Team
- **Lead Architect**: FDE Trainee
- **Governance**: AI Review Policy (CodeRabbit)
- **Traceability**: Tenx MCP Sense

---
*Generated: 2026-02-04*
