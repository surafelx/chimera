# Chimera Agents

Place agent persona files (`SOUL.md`) under `chimera/agents/<role>/SOUL.md`. Each agent instance must include a `SOUL.md` file containing the YAML persona metadata required by the SRS (see `.cursor/srs_alignment_prompt.md`).

Requirements
- `name`: Human-readable agent name
- `id`: Unique agent identifier (UUID recommended)
- `voice_traits`: Array of tone/voice descriptors
- `directives`: List of hard constraints and behavioral directives
- `backstory`: Multiline narrative describing persona

Example roles
- planner — long-term strategist
- worker — stateless executor
- judge — gatekeeper and safety reviewer
