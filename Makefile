# Project Chimera - Makefile
# Standardized commands for development, testing, and deployment

.PHONY: help setup install test lint format clean docker-build docker-run docker-test spec-check

# Default target
help:
	@echo "Project Chimera - Autonomous AI Influencer"
	@echo ""
	@echo "Available commands:"
	@echo "  make setup        - Install dependencies"
	@echo "  make install      - Alias for setup"
	@echo "  make test         - Run tests (including failing TDD tests)"
	@echo "  make lint         - Run linters and formatters"
	@echo "  make format       - Format code with black and isort"
	@echo "  make clean        - Clean up build artifacts"
	@echo "  make docker-build - Build Docker image"
	@echo "  make docker-test - Run tests in Docker"
	@echo "  make spec-check   - Verify code aligns with specs"
	@echo "  make help         - Show this help message"

# Setup environment and install dependencies
setup: install
install:
	@echo "Installing dependencies..."
	uv sync --frozen
	@echo "Dependencies installed successfully."

# Install development dependencies
dev:
	@echo "Installing development dependencies..."
	uv sync
	@echo "Development dependencies installed."

# Run tests (including failing TDD tests)
test:
	@echo "Running tests..."
	pytest tests/ -v --tb=short
	@echo "Tests completed."

# Run specific test file
test-trend:
	pytest tests/test_trend_fetcher.py -v

# Run specific test file
test-skills:
	pytest tests/test_skills_interface.py -v

# Run tests with coverage
test-coverage:
	pytest tests/ -v --cov=chimera --cov-report=html --cov-report=term-missing

# Run linter
lint:
	@echo "Running linters..."
	ruff check .
	mypy chimera tests
	@echo "Linting completed."

# Format code
format:
	@echo "Formatting code..."
	black chimera tests
	isort chimera tests
	@echo "Code formatted."

# Type checking
type-check:
	mypy chimera tests

# Clean up build artifacts
clean:
	@echo "Cleaning up..."
	find . -type d -name "__pycache__" -exec rm -rf {} + 2>/dev/null || true
	find . -type f -name "*.pyc" -delete
	rm -rf .pytest_cache .coverage htmlcov dist build *.egg-info
	@echo "Cleanup completed."

# Build Docker image
docker-build:
	@echo "Building Docker image..."
	docker build -t chimera-agent:latest .
	@echo "Docker image built successfully."

# Run tests in Docker
docker-test:
	@echo "Running tests in Docker..."
	docker run --rm -v $(PWD):/app -w /app chimera-agent:latest make test
	@echo "Docker tests completed."

# Run linting in Docker
docker-lint:
	@echo "Running linters in Docker..."
	docker run --rm -v $(PWD):/app -w /app chimera-agent:latest make lint
	@echo "Docker linting completed."

# Spec alignment check (placeholder)
spec-check:
	@echo "Checking spec alignment..."
	@echo "Verifying that code changes are documented in specs..."
	@echo "TODO: Implement spec-to-code verification"
	@echo "Spec check completed (basic validation)."

# Generate test skeleton from specs
gen-test:
	@echo "Generating test skeleton from specs..."
	@echo "TODO: Implement spec-driven test generation"
	@echo "Test skeleton generation completed."

# Run the agent (placeholder)
run:
	@echo "Starting Chimera Agent..."
	python -m chimera
	@echo "Agent stopped."

# Run with custom config
run-config:
	@echo "Starting Chimera Agent with custom config..."
	python -m chimera --config $(CONFIG_FILE)

# Database migration (placeholder)
migrate:
	@echo "Running database migrations..."
	@echo "TODO: Implement database migration system"
	@echo "Migrations completed."

# Show environment info
info:
	@echo "Environment Information:"
	@echo "Python: $$(python --version)"
	@echo "UV: $$(uv --version 2>/dev/null || echo 'not installed')"
	@echo "Docker: $$(docker --version 2>/dev/null || echo 'not installed')"
	@echo "Node: $$(node --version 2>/dev/null || echo 'not installed')"

# Validate project structure
validate:
	@echo "Validating project structure..."
	@echo "Checking required directories..."
	@test -d chimera && echo "  [OK] chimera/" || echo "  [MISSING] chimera/"
	@test -d chimera/specs && echo "  [OK] chimera/specs/" || echo "  [MISSING] chimera/specs/"
	@test -d chimera/skills && echo "  [OK] chimera/skills/" || echo "  [MISSING] chimera/skills/"
	@test -d chimera/tests && echo "  [OK] chimera/tests/" || echo "  [MISSING] chimera/tests/"
	@test -f chimera/pyproject.toml && echo "  [OK] chimera/pyproject.toml" || echo "  [MISSING] chimera/pyproject.toml"
	@test -f chimera/Dockerfile && echo "  [OK] chimera/Dockerfile" || echo "  [MISSING] chimera/Dockerfile"
	@test -f chimera/Makefile && echo "  [OK] chimera/Makefile" || echo "  [MISSING] chimera/Makefile"
	@echo "Validation completed."
