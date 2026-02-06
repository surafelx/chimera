# Project Chimera - Skills Directory

**Version:** 1.0.0  
**Date:** 2025-02-04

This directory contains the **Runtime Skills** that the Chimera Agent can call during operation. Each skill is a self-contained capability package with defined Input/Output contracts.

## Skill Index

| Skill | Status | Description |
|-------|--------|-------------|
| [skill_fetch_trends](./skill_fetch_trends/) | Ready for Impl | Fetch trending topics from platforms |
| [skill_download_video](./skill_download_video/) | Ready for Impl | Download video content |
| [skill_transcribe_audio](./skill_transcribe_audio/) | Ready for Impl | Transcribe audio to text |
| [skill_generate_caption](./skill_generate_caption/) | Ready for Impl | Generate social media captions |
| [skill_post_content](./skill_post_content/) | Ready for Impl | Post content to platforms |
| [skill_safety_check](./skill_safety_check/) | Ready for Impl | Safety and policy compliance |

---

## Skill Template Structure

Each skill directory follows this structure:

```
skill_xxx/
├── __init__.py          # Package initialization
├── main.py              # Main skill implementation
├── config.py            # Skill configuration
└── README.md            # This file
```

---

## How to Use a Skill

### Example: Using skill_fetch_trends

```python
from skills.skill_fetch_trends import FetchTrendsSkill

# Initialize skill
skill = FetchTrendsSkill(config={
    "api_keys": {
        "tiktok": os.getenv("TIKTOK_API_KEY"),
        "youtube": os.getenv("YOUTUBE_API_KEY")
    }
})

# Execute skill
result = skill.execute(input_data={
    "platforms": ["tiktok", "youtube"],
    "category": "entertainment",
    "limit": 10,
    "time_range": "24h"
})

# Handle result
if result["status"] == "success":
    trends = result["trends"]
    for trend in trends:
        print(f"{trend['title']} - {trend['engagement_score']}")
```

---

## Skill Contracts Reference

### Input Validation

All skills validate input against their contract before execution. Invalid input returns:

```python
{
    "status": "error",
    "error_code": "INVALID_INPUT",
    "message": "Description of validation error",
    "validation_errors": [...]
}
```

### Error Handling

All skills return consistent error format:

```python
{
    "status": "error",
    "error_code": "ERROR_CODE",
    "message": "Human-readable error message",
    "details": {...}
}
```

---

## Adding a New Skill

1. Create new directory: `skill_xxx/`
2. Copy template files from `skill_template/`
3. Update `config.py` with skill-specific configuration
4. Implement `main.py` with skill logic
5. Update this README.md with skill description
6. Add tests in `tests/test_skills_interface.py`

---

## See Also

- [tooling_strategy.md](../research/tooling_strategy.md) - Full tooling documentation
- [specs/technical.md](../specs/technical.md) - Technical specifications
- [specs/functional.md](../specs/functional.md) - User stories
