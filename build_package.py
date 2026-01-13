import PyInstaller.__main__
import os
import sys

# Define base variables
APP_NAME = "BlueMouse"
ENTRY_POINT = "server.py"

# Define data files to include (Source, Destination)
# Destination '.' means root of the bundle
# Note: .env matches the pattern but usually we don't bundle sensitive .env
# We will check if a 'template' or default config is needed.
# For now, we bundle data_trap.jsonl as the 'seed' data.
datas = [
    ('data_trap.jsonl', '.'),
    ('bluemouse_saas.html', '.'),
]

# Hidden imports specific to our stack (FastMCP, Uvicorn, etc often need help)
hidden_imports = [
    'uvicorn',
    'uvicorn.logging',
    'uvicorn.loops',
    'uvicorn.loops.auto',
    'uvicorn.protocols',
    'uvicorn.protocols.http',
    'uvicorn.protocols.http.auto',
    'uvicorn.lifespan',
    'uvicorn.lifespan.on',
    'fastmcp',
    'pydantic',
    'starlette',
    'fastapi',
    'anthropic',

    'dotenv'
]

# Build arguments
args = [
    ENTRY_POINT,
    '--name=' + APP_NAME,
    '--onefile', # Single executable file
    '--clean',   # Clean cache
    '--noconfirm', # Overwrite existing
    '--log-level=WARN'
]

# Add hidden imports command line args
for hidden in hidden_imports:
    args.append(f'--hidden-import={hidden}')

# Add data files command line args
sep = ';' if os.name == 'nt' else ':'
for src, dest in datas:
    if os.path.exists(src):
        args.append(f'--add-data={src}{sep}{dest}')
        print(f"📦 Adding asset: {src}")
    else:
        print(f"⚠️ Warning: Data file {src} not found, skipping.")

print(f"🚀 Starting build for {APP_NAME}...")
print(f"🔧 Entry Point: {ENTRY_POINT}")

# Run PyInstaller
try:
    PyInstaller.__main__.run(args)
    print(f"\n✅ Build complete!")
    print(f"📂 Output: dist/{APP_NAME}")
    if os.name == 'nt':
         print(f"👉 You can run: dist\\{APP_NAME}.exe")
    else:
         print(f"👉 You can run: ./dist/{APP_NAME}")
except Exception as e:
    print(f"❌ Build failed: {e}")
    sys.exit(1)
