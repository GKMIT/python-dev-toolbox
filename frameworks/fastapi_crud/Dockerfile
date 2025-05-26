# Stage 1: Build
FROM python:3.11-slim AS builder

WORKDIR /app

# Set environment variables for build
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PIP_NO_CACHE_DIR=1

# Install build dependencies and curl
RUN apt-get update && apt-get install -y --no-install-recommends \
    gcc \
    curl \
    && rm -rf /var/lib/apt/lists/*

# Install uv binary (latest version)
RUN curl -LsSf https://astral.sh/uv/install.sh | sh

# Add uv to PATH (optional, since it's installed to ~/.cargo/bin or ~/.local/bin usually)
ENV PATH="/root/.cargo/bin:/root/.local/bin:${PATH}"

# Copy pyproject.toml to resolve dependencies
COPY pyproject.toml .

# Generate requirements.txt and install dependencies
RUN uv pip compile pyproject.toml -o requirements.txt
RUN uv pip install --system --no-cache-dir -r requirements.txt

# Stage 2: Runtime
FROM python:3.11-slim

WORKDIR /app

# Create non-root user
RUN useradd -m appuser && chown -R appuser:appuser /app

# Copy installed dependencies from builder
COPY --from=builder /usr/local/lib/python3.11/site-packages /usr/local/lib/python3.11/site-packages
COPY --from=builder /usr/local/bin /usr/local/bin

# Copy application code
COPY . .

# Set environment variables
ENV PATH=/usr/local/bin:$PATH \
    PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PYTHONPATH=/app

# Switch to non-root user
USER appuser

# Expose port
EXPOSE 8000

# Health check
HEALTHCHECK CMD curl --fail http://localhost:8000/health || exit 1

# Run FastAPI
CMD ["fastapi", "run", "main/app.py", "--port", "8000"]