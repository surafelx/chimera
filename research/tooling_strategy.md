# Project Chimera - Tooling Strategy

**Version:** 1.0.0  
**Date:** 2025-02-04

## Overview

This document outlines the tooling strategy for Project Chimera, distinguishing between:
- **Developer Tools (MCP Servers)**: Tools that help YOU develop
- **Agent Skills (Runtime)**: Capabilities the Chimera Agent uses at runtime

---

## Part A: Developer Tools (MCP Servers)

MCP (Model Context Protocol) servers are developer tools integrated into the IDE to enhance development experience.

### MCP Servers Installed

| MCP Server | Purpose | Configuration |
|------------|---------|---------------|
| **git-mcp** | Version control operations | Connected via Tenx MCP Sense |
| **filesystem-mcp** | File editing and management | Connected via Tenx MCP Sense |
| **tenx-mcp-sense** | Telemetry and "black box" recording | Always active |

### MCP Connection Status
See: [mcp_sense_connection_log.md](./mcp_sense_connection_log.md)

### Future MCP Servers to Consider

| MCP Server | Purpose | Priority |
|------------|---------|----------|
| docker-mcp | Docker container management | High |
| database-mcp | Database schema inspection | Medium |
| github-mcp | GitHub API integration | Medium |

---

## Part B: Agent Skills (Runtime)

Skills are reusable capability packages the Chimera Agent calls during operation. Each skill has a defined Input/Output contract.

### Skill Directory Structure

```
skills/
├── skill_fetch_trends/
│   ├── __init__.py
│   ├── main.py          # Main skill implementation
│   ├── config.py        # Skill configuration
│   └── README.md        # Skill documentation
├── skill_download_video/
│   ├── __init__.py
│   ├── main.py
│   ├── config.py
│   └── README.md
├── skill_transcribe_audio/
│   ├── __init__.py
│   ├── main.py
│   ├── config.py
│   └── README.md
├── skill_generate_caption/
│   ├── __init__.py
│   ├── main.py
│   ├── config.py
│   └── README.md
├── skill_post_content/
│   ├── __init__.py
│   ├── main.py
│   ├── config.py
│   └── README.md
└── skill_safety_check/
    ├── __init__.py
    ├── main.py
    ├── config.py
    └── README.md
```

### Skill Specifications

#### 1. skill_fetch_trends
**Purpose:** Fetch trending topics from social media platforms

**Input Contract:**
```python
{
    "platforms": List[str],  # ["tiktok", "youtube", "twitter"]
    "category": str,          # e.g., "entertainment"
    "limit": int,            # Number of trends to fetch
    "time_range": str        # e.g., "24h", "7d"
}
```

**Output Contract:**
```python
{
    "status": str,          # "success", "error"
    "trends": List[Trend],
    "timestamp": str        # ISO 8601
}

Trend = {
    "id": str,
    "title": str,
    "platform": str,
    "engagement_score": float,
    "volume": int,
    "metadata": dict
}
```

#### 2. skill_download_video
**Purpose:** Download video content from platform URLs

**Input Contract:**
```python
{
    "url": str,             # Video URL
    "platform": str,        # Platform identifier
    "output_path": str      # Local path to save
}
```

**Output Contract:**
```python
{
    "status": str,
    "filepath": str,
    "metadata": {
        "duration": float,
        "resolution": str,
        "size": int
    }
}
```

#### 3. skill_transcribe_audio
**Purpose:** Transcribe audio to text using speech recognition

**Input Contract:**
```python
{
    "filepath": str,        # Path to audio/video file
    "language": str,        # e.g., "en-US"
    "model": str           # Whisper model size: "base", "small", "medium", "large"
}
```

**Output Contract:**
```python
{
    "status": str,
    "transcript": str,
    "duration": float,
    "language": str
}
```

#### 4. skill_generate_caption
**Purpose:** Generate social media captions based on content

**Input Contract:**
```python
{
    "transcript": str,      # Content to base caption on
    "persona": str,        # Persona style: "funny", "professional", "casual"
    "platform": str,       # Target platform
    "include_hashtags": bool,
    "variations": int      # Number of variations
}
```

**Output Contract:**
```python
{
    "status": str,
    "captions": List[Caption],
    "best_choice": int     # Index of best caption
}

Caption = {
    "text": str,
    "hashtags": List[str],
    "safety_score": float
}
```

#### 5. skill_post_content
**Purpose:** Post content to social media platforms

**Input Contract:**
```python
{
    "content": {
        "text": str,
        "media": List[str],       # File paths
        "hashtags": List[str]
    },
    "platform": str,
    "schedule": Optional[str]     # ISO 8601 timestamp
}
```

**Output Contract:**
```python
{
    "status": str,
    "post_id": str,
    "url": str,
    "published_at": str
}
```

#### 6. skill_safety_check
**Purpose:** Evaluate content for safety and policy compliance

**Input Contract:**
```python
{
    "content": str,
    "context": dict,        # Additional context
    "check_types": List[str]  # ["toxicity", "spam", "policy"]
}
```

**Output Contract:**
```python
{
    "status": str,
    "scores": dict,         # Scores per check type
    "is_safe": bool,
    "flags": List[str]      # Any policy violations
}
```

---

## Skill Implementation Guidelines

### Common Interface
All skills implement a base interface:

```python
class BaseSkill:
    def __init__(self, config: dict):
        self.config = config
    
    def validate_input(self, input_data: dict) -> bool:
        """Validate input against contract"""
        pass
    
    def execute(self, input_data: dict) -> dict:
        """Execute skill logic"""
        pass
    
    def validate_output(self, output_data: dict) -> bool:
        """Validate output against contract"""
        pass
```

### Error Handling
- All skills return consistent error format
- Errors logged to telemetry
- Graceful degradation when dependencies fail

---

## Development Tools vs. Runtime Skills

| Aspect | Developer Tools (MCP) | Agent Skills (Runtime) |
|--------|------------------------|-------------------------|
| User | Developer | Chimera Agent |
| Location | IDE integration | skills/ directory |
| Called by | Human developer | Agent orchestrator |
| Purpose | Improve DX | Runtime capabilities |
| Example | git-mcp | skill_fetch_trends |
