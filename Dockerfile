# Project Chimera - Docker Environment
# This Dockerfile encapsulates the development and runtime environment

# Use Python 3.11 slim for production
FROM python:3.11-slim

# Labels for container metadata
LABEL maintainer="FDE Trainee - Project Chimera"
LABEL version="1.0.0"
LABEL description="Autonomous AI Influencer Agent Environment"

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
ENV PIP_NO_CACHE_DIR=1
ENV PIP_DISABLE_PIP_VERSION_CHECK=1

# Set working directory
WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y --no-install-recommends \
    curl \
    git \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

# Install uv for fast Python package management
RUN curl -LsSf https://astral.sh/uv/install.sh | sh
ENV PATH="/root/.local/bin:$PATH"

# Copy only dependency files first for better caching
COPY pyproject.toml .

# Install Python dependencies using uv
RUN uv sync --frozen --no-dev

# Copy the rest of the application
COPY . .

# Create necessary directories
RUN mkdir -p /app/logs /app/data /app/skills

# Set default environment variables
ENV PYTHONPATH=/app
ENV CHIMERA_ENV=production

# Expose ports (if running web services)
EXPOSE 8000 8080

# Health check
HEALTHCHECK --interval=30s --timeout=10s --start-period=5s --retries=3 \
    CMD python -c "import sys; sys.exit(0)" || exit 1

# Default command
CMD ["python", "-m", "chimera"]
