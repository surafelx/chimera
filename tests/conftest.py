"""
pytest configuration for Project Chimera.

This file configures pytest to:
- Look for tests in tests/ directory
- Use the tests mark for failing tests
- Generate coverage reports
"""

import sys
import os

# Add the chimera directory to the path
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# pytest configuration
pytest_plugins = ['pytest_asyncio']

# Test marks
markers = [
    "failing: Tests that are expected to fail (TDD)",
    "integration: Integration tests",
    "unit: Unit tests",
    "slow: Slow running tests",
]

# Configuration
def pytest_configure(config):
    config.addinivalue_line("markers", "failing: Tests that are expected to fail (TDD)")
    config.addinivalue_line("markers", "integration: Integration tests")
    config.addinivalue_line("markers", "unit: Unit tests")


# Ignore tests in __pycache__ and .pyc files
collect_ignore_glob = ["**/__pycache__/**", "**/*.pyc"]
