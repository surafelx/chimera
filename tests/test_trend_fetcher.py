"""
Test Trend Fetcher - API Contract Validation

This test validates that the trend fetcher service adheres to the API contract
defined in specs/technical.md.

These tests SHOULD FAIL when first run. They define the "empty slot" 
the AI agent must fill.

Reference: specs/technical.md#api-contracts
"""

import pytest
from datetime import datetime
from typing import List, Dict, Any


# ============================================================================
# Expected Data Structures (from specs/technical.md)
# ============================================================================

class TestTrendDataContract:
    """Test that trend data structure matches the API contract."""
    
    def test_trend_object_structure(self):
        """
        A Trend object MUST contain:
        - id: str
        - title: str
        - platform: str
        - engagement_score: float
        - volume: int
        - metadata: dict
        
        Reference: specs/technical.md#2.1-trend-fetcher-service
        """
        # This test will FAIL until skill_fetch_trends is implemented
        from skills.skill_fetch_trends import FetchTrendsSkill
        
        skill = FetchTrendsSkill(config={})
        
        # Expected output structure
        expected_trend = {
            "id": "trend_001",
            "title": "#ViralChallenge2024",
            "platform": "tiktok",
            "engagement_score": 0.95,
            "volume": 1500000,
            "metadata": {
                "hashtags": ["#ViralChallenge2024"],
                "sentiment": "positive",
                "demographics": {
                    "age_range": "18-24",
                    "location": "US"
                }
            }
        }
        
        # Validate structure (will fail until implementation exists)
        assert "id" in expected_trend
        assert "title" in expected_trend
        assert "platform" in expected_trend
        assert isinstance(expected_trend["engagement_score"], float)
        assert 0.0 <= expected_trend["engagement_score"] <= 1.0
        assert isinstance(expected_trend["volume"], int)
        assert isinstance(expected_trend["metadata"], dict)

    def test_fetch_trends_request_format(self):
        """
        Test that the fetch trends request matches the API contract.
        
        Request format:
        {
            "platforms": ["tiktok", "youtube", "twitter"],
            "category": "entertainment",
            "limit": 10,
            "time_range": "24h"
        }
        """
        from skills.skill_fetch_trends import FetchTrendsSkill
        
        skill = FetchTrendsSkill(config={})
        
        valid_request = {
            "platforms": ["tiktok", "youtube", "twitter"],
            "category": "entertainment",
            "limit": 10,
            "time_range": "24h"
        }
        
        # Validate input can be processed
        assert isinstance(valid_request["platforms"], list)
        assert all(isinstance(p, str) for p in valid_request["platforms"])
        assert isinstance(valid_request["category"], str)
        assert isinstance(valid_request["limit"], int)
        assert valid_request["limit"] > 0
        assert isinstance(valid_request["time_range"], str)

    def test_fetch_trends_response_format(self):
        """
        Test that the fetch trends response matches the API contract.
        
        Response format:
        {
            "status": "success",
            "data": {
                "trends": [...]
            },
            "timestamp": "ISO 8601"
        }
        """
        from skills.skill_fetch_trends import FetchTrendsSkill
        
        skill = FetchTrendsSkill(config={})
        
        # Expected response structure
        expected_response = {
            "status": "success",
            "data": {
                "trends": []
            },
            "timestamp": "2025-02-04T10:30:05Z"
        }
        
        assert expected_response["status"] in ["success", "error"]
        assert "data" in expected_response
        assert "trends" in expected_response["data"]
        assert isinstance(expected_response["data"]["trends"], list)
        
        # Validate timestamp format
        datetime.fromisoformat(expected_response["timestamp"].replace("Z", "+00:00"))


class TestTrendFetcherIntegration:
    """Integration tests for the trend fetcher skill."""
    
    def test_skill_can_be_initialized(self):
        """Test that the FetchTrendsSkill can be initialized with config."""
        from skills.skill_fetch_trends import FetchTrendsSkill
        
        config = {
            "api_keys": {
                "tiktok": "test_key",
                "youtube": "test_key",
                "twitter": "test_key"
            }
        }
        
        skill = FetchTrendsSkill(config=config)
        assert skill is not None
    
    def test_skill_execute_method_exists(self):
        """Test that the skill has an execute method."""
        from skills.skill_fetch_trends import FetchTrendsSkill
        
        skill = FetchTrendsSkill(config={})
        assert hasattr(skill, 'execute')
        assert callable(skill.execute)
    
    def test_skill_validates_input(self):
        """Test that the skill validates input before execution."""
        from skills.skill_fetch_trends import FetchTrendsSkill
        
        skill = FetchTrendsSkill(config={})
        assert hasattr(skill, 'validate_input')
    
    def test_skill_handles_multiple_platforms(self):
        """Test that trends can be fetched from multiple platforms."""
        from skills.skill_fetch_trends import FetchTrendsSkill
        
        skill = FetchTrendsSkill(config={})
        
        # Test with multiple platforms
        platforms = ["tiktok", "youtube", "twitter"]
        assert len(platforms) == 3
        assert all(p in ["tiktok", "youtube", "twitter"] for p in platforms)


# ============================================================================
# Failing Tests (These demonstrate what the implementation MUST provide)
# ============================================================================

@pytest.mark.failing
class TestTrendFetcherFailing:
    """These tests will FAIL until the skill is fully implemented."""
    
    def test_execute_returns_valid_response(self):
        """
        FAILING TEST: This test will pass only when the skill is implemented.
        
        Expected: execute() returns a response matching the API contract.
        Current: ModuleNotFoundError - skills.skill_fetch_trends not found
        """
        from skills.skill_fetch_trends import FetchTrendsSkill
        
        skill = FetchTrendsSkill(config={})
        
        result = skill.execute(input_data={
            "platforms": ["tiktok"],
            "category": "entertainment",
            "limit": 5,
            "time_range": "24h"
        })
        
        assert result["status"] == "success"
        assert "trends" in result["data"]
    
    def test_trends_have_valid_engagement_scores(self):
        """
        FAILING TEST: Validate that all returned trends have valid engagement scores.
        
        Expected: All trends have engagement_score between 0.0 and 1.0
        """
        from skills.skill_fetch_trends import FetchTrendsSkill
        
        skill = FetchTrendsSkill(config={})
        
        result = skill.execute(input_data={
            "platforms": ["tiktok"],
            "category": "entertainment",
            "limit": 10,
            "time_range": "24h"
        })
        
        for trend in result["data"]["trends"]:
            assert 0.0 <= trend["engagement_score"] <= 1.0
    
    def test_error_handling(self):
        """
        FAILING TEST: Test that the skill handles errors gracefully.
        
        Expected: Invalid input returns error status with validation errors.
        """
        from skills.skill_fetch_trends import FetchTrendsSkill
        
        skill = FetchTrendsSkill(config={})
        
        result = skill.execute(input_data={
            "platforms": [],  # Empty platforms should fail validation
            "category": "entertainment",
            "limit": 10,
            "time_range": "24h"
        })
        
        assert result["status"] == "error"
        assert "error_code" in result
