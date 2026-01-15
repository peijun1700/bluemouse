import os
import sys
from contextlib import contextmanager

@contextmanager
def suppress_stdout_stderr():
    """A context manager that redirects stdout and stderr to devnull"""
    with open(os.devnull, "w") as devnull:
        old_stdout = sys.stdout
        old_stderr = sys.stderr
        sys.stdout = devnull
        sys.stderr = devnull
        try:
            yield
        finally:
            sys.stdout = old_stdout
            sys.stderr = old_stderr

# Suppress warnings/prints during import to keep JSON-RPC stream clean
with suppress_stdout_stderr():
    from server import mcp

if __name__ == "__main__":
    # Explicitly run in stdio mode for Glama/MCP Proxy compatibility
    mcp.run(transport="stdio")
