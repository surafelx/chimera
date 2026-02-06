# Project Chimera - Failing Tests

**Version:** 1.0.0  
**Date:** 2025-02-04

This directory contains **failing tests** that define the "empty slots" the AI must fill. Tests are written BEFORE implementation, following TDD principles.

## Test Files

| Test File | Purpose | Status |
|-----------|---------|--------|
| [test_trend_fetcher.py](./test_trend_fetcher.py) | Tests trend fetcher API contract | Failing |
| [test_skills_interface.py](./test_skills_interface.py) | Tests skill input/output contracts | Failing |
| [test_swarm_architecture.py](./test_swarm_architecture.py) | Tests Planner-Worker-Judge pattern | Failing |
| [test_mcp_integration.py](./test_mcp_integration.py) | Tests MCP client integration | Failing |
| [test_commerce_manager.py](./test_commerce_manager.py) | Tests Coinbase AgentKit integration | Failing |

## Running Tests

```bash
# Run all tests (they should fail)
make test

# Run specific test
pytest tests/test_trend_fetcher.py -v
```
