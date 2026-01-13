import os
import zipfile
import shutil

def zip_project(output_filename):
    # Get current directory
    root_dir = os.path.dirname(os.path.abspath(__file__))
    
    # Files/Dirs to EXCLUDE
    excludes = {
        '.git', 
        '.DS_Store', 
        '__pycache__', 
        'venv', 
        '.env', 
        'pack_release.py', # Don't pack the packer
        'data_trap.jsonl' # User Data Privacy (Optional, but good practice to clear)
    }

    print(f"📦 Packaging BlueMouse v6.1 to {output_filename}...")
    
    with zipfile.ZipFile(output_filename, 'w', zipfile.ZIP_DEFLATED) as zipf:
        for root, dirs, files in os.walk(root_dir):
            # Modify dirs in-place to skip excluded directories
            dirs[:] = [d for d in dirs if d not in excludes]
            
            for file in files:
                if file in excludes or file == output_filename:
                    continue
                if file.endswith('.pyc'):
                    continue
                    
                file_path = os.path.join(root, file)
                arcname = os.path.relpath(file_path, root_dir)
                
                print(f"  Adding: {arcname}")
                zipf.write(file_path, arcname)
                
    print(f"✅ Package Complete: {output_filename}")

if __name__ == "__main__":
    zip_project("BlueMouse_v6.1_Core_Logic.zip")
