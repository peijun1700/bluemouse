from server import mcp

if __name__ == "__main__":
    # Explicitly run in stdio mode for Glama/MCP Proxy compatibility
    mcp.run(transport="stdio")
