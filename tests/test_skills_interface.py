"""
Test Skills Interface - Skill Contract Validation

This test validates that all skills in the skills/ directory adhere to the
defined Input/Output contracts.

These tests SHOULD FAIL when first run. They define the "empty slots" 
the AI agent must fill.

Reference: specs/technical.md#4-skill-contracts
"""

import pytest
from typing import Dict, Any, List


# ============================================================================
# Base Skill Interface Tests
# ============================================================================

class TestSkillInterface:
    """Test that all skills implement the base skill interface."""
    
    def test_fetch_trends_has_required_methods(self):
        """
        Test that skill_fetch_trends implements the required interface.
        
        Required methods:
        - __init__(config: dict)
        - validate_input(input_data: dict) -> bool
        - execute(input_data: dict) -> dict
        - validate_output(output_data: dict) -> bool
        """
        from skills.skill_fetch_trends import FetchTrendsSkill
        
        skill = FetchTrendsSkill(config={})
        
        assert hasattr(skill, 'validate_input')
        assert callable(skill.validate_input)
        assert hasattr(skill, 'execute')
        assert callable(skill.execute)
        assert hasattr(skill, 'validate_output')
        assert callable(skill.validate_output)
    
    def test_download_video_has_required_methods(self):
        """Test that skill_download_video implements the required interface."""
        from skills.skill_download_video import DownloadVideoSkill
        
        skill = DownloadVideoSkill(config={})
        
        assert hasattr(skill, 'validate_input')
        assert hasattr(skill, 'execute')
        assert hasattr(skill, 'validate_output')
    
    def test_transcribe_audio_has_required_methods(self):
        """Test that skill_transcribe_audio implements the required interface."""
        from skills.skill_transcribe_audio import TranscribeAudioSkill
        
        skill = TranscribeAudioSkill(config={})
        
        assert hasattr(skill, 'validate_input')
        assert hasattr(skill, 'execute')
        assert hasattr(skill, 'validate_output')
    
    def test_generate_caption_has_required_methods(self):
        """Test that skill_generate_caption implements the required interface."""
        from skills.skill_generate_caption import GenerateCaptionSkill
        
        skill = GenerateCaptionSkill(config={})
        
        assert hasattr(skill, 'validate_input')
        assert hasattr(skill, 'execute')
        assert hasattr(skill, 'validate_output')
    
    def test_post_content_has_required_methods(self):
        """Test that skill_post_content implements the required interface."""
        from skills.skill_post_content import PostContentSkill
        
        skill = PostContentSkill(config={})
        
        assert hasattr(skill, 'validate_input')
        assert hasattr(skill, 'execute')
        assert hasattr(skill, 'validate_output')
    
    def test_safety_check_has_required_methods(self):
        """Test that skill_safety_check implements the required interface."""
        from skills.skill_safety_check import SafetyCheckSkill
        
        skill = SafetyCheckSkill(config={})
        
        assert hasattr(skill, 'validate_input')
        assert hasattr(skill, 'execute')
        assert hasattr(skill, 'validate_output')


# ============================================================================
# Skill Input Contract Tests
# ============================================================================

class TestSkillInputContracts:
    """Test that skills validate input against their contracts."""
    
    def test_fetch_trends_input_contract(self):
        """
        Test skill_fetch_trends input contract.
        
        Input:
        {
            "platforms": List[str],
            "category": str,
            "limit": int,
            "time_range": str
        }
        """
        from skills.skill_fetch_trends import FetchTrendsSkill
        
        skill = FetchTrendsSkill(config={})
        
        valid_input = {
            "platforms": ["tiktok", "youtube"],
            "category": "entertainment",
            "limit": 10,
            "time_range": "24h"
        }
        
        assert skill.validate_input(valid_input) is True
    
    def test_download_video_input_contract(self):
        """
        Test skill_download_video input contract.
        
        Input:
        {
            "url": str,
            "platform": str,
            "output_path": str
        }
        """
        from skills.skill_download_video import DownloadVideoSkill
        
        skill = DownloadVideoSkill(config={})
        
        valid_input = {
            "url": "https://tiktok.com/@user/video/123",
            "platform": "tiktok",
            "output_path": "/tmp/video.mp4"
        }
        
        assert skill.validate_input(valid_input) is True
    
    def test_transcribe_audio_input_contract(self):
        """
        Test skill_transcribe_audio input contract.
        
        Input:
        {
            "filepath": str,
            "language": str,
            "model": str
        }
        """
        from skills.skill_transcribe_audio import TranscribeAudioSkill
        
        skill = TranscribeAudioSkill(config={})
        
        valid_input = {
            "filepath": "/tmp/video.mp4",
            "language": "en-US",
            "model": "base"
        }
        
        assert skill.validate_input(valid_input) is True
    
    def test_generate_caption_input_contract(self):
        """
        Test skill_generate_caption input contract.
        
        Input:
        {
            "transcript": str,
            "persona": str,
            "platform": str,
            "include_hashtags": bool,
            "variations": int
        }
        """
        from skills.skill_generate_caption import GenerateCaptionSkill
        
        skill = GenerateCaptionSkill(config={})
        
        valid_input = {
            "transcript": "This is the video transcript...",
            "persona": "funny",
            "platform": "tiktok",
            "include_hashtags": True,
            "variations": 3
        }
        
        assert skill.validate_input(valid_input) is True
    
    def test_post_content_input_contract(self):
        """
        Test skill_post_content input contract.
        
        Input:
        {
            "content": {...},
            "platform": str,
            "schedule": Optional[str]
        }
        """
        from skills.skill_post_content import PostContentSkill
        
        skill = PostContentSkill(config={})
        
        valid_input = {
            "content": {
                "text": "Check out my new video!",
                "media": ["/tmp/video.mp4"],
                "hashtags": ["#trending"]
            },
            "platform": "tiktok",
            "schedule": None
        }
        
        assert skill.validate_input(valid_input) is True
    
    def test_safety_check_input_contract(self):
        """
        Test skill_safety_check input contract.
        
        Input:
        {
            "content": str,
            "context": dict,
            "check_types": List[str]
        }
        """
        from skills.skill_safety_check import SafetyCheckSkill
        
        skill = SafetyCheckSkill(config={})
        
        valid_input = {
            "content": "This is some content to check",
            "context": {"user_id": "123"},
            "check_types": ["toxicity", "spam", "policy"]
        }
        
        assert skill.validate_input(valid_input) is True


# ============================================================================
# Skill Output Contract Tests
# ============================================================================

class TestSkillOutputContracts:
    """Test that skills produce output matching their contracts."""
    
    def test_fetch_trends_output_contract(self):
        """
        Test skill_fetch_trends output contract.
        
        Output:
        {
            "status": str,
            "trends": List[Trend],
            "timestamp": str
        }
        """
        from skills.skill_fetch_trends import FetchTrendsSkill
        
        skill = FetchTrendsSkill(config={})
        
        output = skill.execute(input_data={
            "platforms": ["tiktok"],
            "category": "entertainment",
            "limit": 5,
            "time_range": "24h"
        })
        
        assert "status" in output
        assert output["status"] in ["success", "error"]
        assert "trends" in output
        assert isinstance(output["trends"], list)
        assert "timestamp" in output
    
    def test_download_video_output_contract(self):
        """
        Test skill_download_video output contract.
        
        Output:
        {
            "status": str,
            "filepath": str,
            "metadata": {...}
        }
        """
        from skills.skill_download_video import DownloadVideoSkill
        
        skill = DownloadVideoSkill(config={})
        
        output = skill.execute(input_data={
            "url": "https://tiktok.com/video/123",
            "platform": "tiktok",
            "output_path": "/tmp/video.mp4"
        })
        
        assert "status" in output
        assert "filepath" in output
        assert "metadata" in output
    
    def test_transcribe_audio_output_contract(self):
        """
        Test skill_transcribe_audio output contract.
        
        Output:
        {
            "status": str,
            "transcript": str,
            "duration": float,
            "language": str
        }
        """
        from skills.skill_transcribe_audio import TranscribeAudioSkill
        
        skill = TranscribeAudioSkill(config={})
        
        output = skill.execute(input_data={
            "filepath": "/tmp/video.mp4",
            "language": "en-US",
            "model": "base"
        })
        
        assert "status" in output
        assert "transcript" in output
        assert "duration" in output
        assert "language" in output
    
    def test_generate_caption_output_contract(self):
        """
        Test skill_generate_caption output contract.
        
        Output:
        {
            "status": str,
            "captions": List[Caption],
            "best_choice": int
        }
        """
        from skills.skill_generate_caption import GenerateCaptionSkill
        
        skill = GenerateCaptionSkill(config={})
        
        output = skill.execute(input_data={
            "transcript": "Video transcript...",
            "persona": "funny",
            "platform": "tiktok",
            "include_hashtags": True,
            "variations": 3
        })
        
        assert "status" in output
        assert "captions" in output
        assert isinstance(output["captions"], list)
        assert "best_choice" in output
    
    def test_post_content_output_contract(self):
        """
        Test skill_post_content output contract.
        
        Output:
        {
            "status": str,
            "post_id": str,
            "url": str,
            "published_at": str
        }
        """
        from skills.skill_post_content import PostContentSkill
        
        skill = PostContentSkill(config={})
        
        output = skill.execute(input_data={
            "content": {
                "text": "Check out my new video!",
                "media": ["/tmp/video.mp4"],
                "hashtags": ["#trending"]
            },
            "platform": "tiktok",
            "schedule": None
        })
        
        assert "status" in output
        assert "post_id" in output
        assert "url" in output
    
    def test_safety_check_output_contract(self):
        """
        Test skill_safety_check output contract.
        
        Output:
        {
            "status": str,
            "scores": dict,
            "is_safe": bool,
            "flags": List[str]
        }
        """
        from skills.skill_safety_check import SafetyCheckSkill
        
        skill = SafetyCheckSkill(config={})
        
        output = skill.execute(input_data={
            "content": "Content to check",
            "context": {},
            "check_types": ["toxicity"]
        })
        
        assert "status" in output
        assert "scores" in output
        assert isinstance(output["scores"], dict)
        assert "is_safe" in output
        assert isinstance(output["is_safe"], bool)
        assert "flags" in output


# ============================================================================
# Error Handling Tests
# ============================================================================

class TestSkillErrorHandling:
    """Test that skills handle errors gracefully."""
    
    def test_invalid_input_returns_error(self):
        """Test that invalid input returns an error response."""
        from skills.skill_fetch_trends import FetchTrendsSkill
        
        skill = FetchTrendsSkill(config={})
        
        invalid_input = {
            "platforms": [],  # Empty platforms
            "category": "entertainment",
            "limit": -1,  # Negative limit
            "time_range": "invalid"
        }
        
        result = skill.execute(input_data=invalid_input)
        
        assert result["status"] == "error"
        assert "error_code" in result
        assert "message" in result
    
    def test_missing_required_fields(self):
        """Test that missing required fields are detected."""
        from skills.skill_fetch_trends import FetchTrendsSkill
        
        skill = FetchTrendsSkill(config={})
        
        # Missing 'platforms' field
        incomplete_input = {
            "category": "entertainment",
            "limit": 10
        }
        
        assert skill.validate_input(incomplete_input) is False


# ============================================================================
# Failing Tests (These demonstrate what the implementation MUST provide)
# ============================================================================

@pytest.mark.failing
class TestSkillsFailing:
    """These tests will FAIL until all skills are fully implemented."""
    
    def test_all_skills_execute_successfully(self):
        """
        FAILING TEST: All skills should execute without errors.
        
        This test chains multiple skills together to simulate
        a real-world workflow:
        1. Fetch trends
        2. Generate caption
        3. Safety check
        4. Post content
        """
        from skills.skill_fetch_trends import FetchTrendsSkill
        from skills.skill_generate_caption import GenerateCaptionSkill
        from skills.skill_safety_check import SafetyCheckSkill
        from skills.skill_post_content import PostContentSkill
        
        # Step 1: Fetch trends
        trends_skill = FetchTrendsSkill(config={})
        trends_result = trends_skill.execute(input_data={
            "platforms": ["tiktok"],
            "category": "entertainment",
            "limit": 1,
            "time_range": "24h"
        })
        
        assert trends_result["status"] == "success"
        
        # Step 2: Generate caption
        caption_skill = GenerateCaptionSkill(config={})
        caption_result = caption_skill.execute(input_data={
            "transcript": "Test video content",
            "persona": "funny",
            "platform": "tiktok",
            "include_hashtags": True,
            "variations": 1
        })
        
        assert caption_result["status"] == "success"
        
        # Step 3: Safety check
        safety_skill = SafetyCheckSkill(config={})
        safety_result = safety_skill.execute(input_data={
            "content": caption_result["captions"][0]["text"],
            "context": {},
            "check_types": ["toxicity", "spam"]
        })
        
        assert safety_result["status"] == "success"
        assert safety_result["is_safe"] is True
        
        # Step 4: Post content (would actually post - skip for test)
        post_skill = PostContentSkill(config={})
        post_result = post_skill.execute(input_data={
            "content": {
                "text": caption_result["captions"][0]["text"],
                "media": [],
                "hashtags": caption_result["captions"][0]["hashtags"]
            },
            "platform": "tiktok",
            "schedule": None
        })
        
        assert post_result["status"] == "success"
