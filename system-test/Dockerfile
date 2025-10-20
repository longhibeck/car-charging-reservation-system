FROM python:3.12-slim

WORKDIR /workspace

# Install uv and curl
RUN pip install uv && apt-get update && apt-get install -y curl && rm -rf /var/lib/apt/lists/*

# Copy test project files
COPY pyproject.toml ./
COPY conftest.py ./
COPY tests/ ./tests/

# Install test dependencies
RUN uv sync --frozen

CMD ["uv", "run", "pytest", "-v"]