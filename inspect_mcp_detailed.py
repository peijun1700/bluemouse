
try:
    from server import mcp
    print("Type:", type(mcp))
    attrs = dir(mcp)
    
    if 'mount' in attrs:
        print("✅ Found 'mount' method")
    else:
        print("❌ 'mount' NOT found")
        
    if '_fastapi_app' in attrs:
        print("✅ Found '_fastapi_app' attribute")
    else:
        print("❌ '_fastapi_app' NOT found")

    if 'fastapi_app' in attrs:
        print("✅ Found 'fastapi_app' attribute")
    
    import inspect
    if hasattr(mcp, 'run'):
        print("Run signature:", inspect.signature(mcp.run))

except ImportError as e:
    print("Import error:", e)
except Exception as e:
    print("Error:", e)
