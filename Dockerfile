# Dockerfile for BlueMouse MCP Server
# Used by Smithery.ai for automatic containerization

# Use a slim Python image
FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Copy requirement files first for better caching
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application
COPY . .

# Set environment variables
ENV PYTHONUNBUFFERED=1

# Install Node.js and mcp-proxy for Glama inspection support
RUN apt-get update && apt-get install -y --no-install-recommends curl \
    && curl -fsSL https://deb.nodesource.com/setup_20.x | bash - \
    && apt-get install -y --no-install-recommends nodejs \
    && npm install -g mcp-proxy \
    && apt-get clean && rm -rf /var/lib/apt/lists/*

# Expose port (if running in SSE mode, though StdIO is default)
EXPOSE 8000

# Default command to run the MCP server with mcp-proxy for inspection
# Using dedicated Stdio entry point to avoid WebSocket/HTTP conflicts
CMD ["mcp-proxy", "python", "mcp_stdio.py"]
