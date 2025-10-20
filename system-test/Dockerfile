FROM ghcr.io/astral-sh/uv:python3.13-trixie-slim

WORKDIR /workspace

# Install curl for testing
RUN apt-get update && \
    apt-get install -y curl && \
    rm -rf /var/lib/apt/lists/*

# Copy test project files
COPY pyproject.toml uv.lock ./
COPY conftest.py ./
COPY tests/ ./tests/

# Install test dependencies
RUN uv sync --frozen

CMD ["uv", "run", "pytest", "-v"]