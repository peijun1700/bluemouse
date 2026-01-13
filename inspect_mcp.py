
try:
    from server import mcp
    print("Found mcp object:", type(mcp))
    print("mcp dir:", dir(mcp))
    
    # Check for FastAPI app attributes
    if hasattr(mcp, 'fastapi_app'):
        print("Has fastapi_app attribute")
    if hasattr(mcp, '_fastapi_app'):
        print("Has _fastapi_app attribute")
        
except ImportError as e:
    print("Import error:", e)
except Exception as e:
    print("Error:", e)
