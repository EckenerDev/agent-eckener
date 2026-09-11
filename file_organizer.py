
<think>
The user wants a Python program that sorts files by extension.
- It should organize files from a specified directory into subdirectories based on their file extensions.
- No external dependencies (standard library only).
- Clean, robust, self-contained.
- Python 3.
- Single markdown fenced block.

I need to:
1. Define a main function or class that takes a source directory and optionally a target directory (or use the source directory itself for organization).
2. Walk through the source directory.
3. For each file, extract the extension (e.g., '.txt', '.jpg'). Handle files without extensions.
4. Create a subdirectory for each extension in the target location.
5. Move (or copy) the file to the appropriate subdirectory.
6. Handle potential issues: overwriting files, permissions, invalid paths, etc.
7. Provide a CLI interface or a simple script with arguments.

Let's design it as a script that takes arguments via `argparse`.
Options:
- `--source`: source directory (default: current directory)
- `--target`: target directory (default: inside source directory, named `organized`) or a separate directory. I'll make it default to a subdirectory called `_organized` inside the source, or allow specifying it.
- `--dry-run`: to test without actually moving files.
- Handle files without extension under a `_no_extension` folder.
- Use `shutil.move` for moving files.
- Ensure robust error handling (try-except for file operations, check for existing files, ask for overwrite or auto-rename).

Actually, to keep it simple but robust, I'll:
- Use `argparse` for source and destination.
- Walk through the directory using `pathlib`.
- Create a mapping of extensions to lists of files.
- Move files.
- Handle duplicates by appending a suffix.
- Provide feedback.

Let's structure the code:
```python
import argparse
import os
import sys
import shutil
from pathlib import Path

def organize_files(source_dir: Path, target_dir: Path, dry_run: bool = False):
    source_dir = source_dir.resolve()
    target_dir = target_dir.resolve()
    
    if not source_dir.is_dir():
        print(f"Error: '{source_dir}' is not a valid directory.")
        sys.exit(1)
        
    if target_dir == source_dir:
        print("Error: Source and target directories cannot be the same.")
        sys.exit(1)
        
    # Map to store extension -> list of files
    ext_map = {}
    no_ext_files = []
    
    # Iterate over files in the source directory (non-recursive for simplicity, or recursive? Usually organizers work recursively or just in the given dir. I'll make it non-recursive for the top-level files to avoid moving subdirectories contents into the target in a confusing way, but I'll add an option or just stick to top-level files. Let's do top-level files only for safety, or process only files (not directories).)
    for item in source_dir.iterdir():
        if item.is_file():
            ext = item.suffix.lower() if item.suffix else ""
            if ext:
                ext_map.setdefault(ext, []).append(item)
            else:
                no_ext_files.append(item)
                
    # Create target directory
    if not dry_run:
        target_dir.mkdir(parents=True, exist_ok=True)
        
    moved_count = 0
    skipped_count = 0
    
    def move_file(src_file, target_ext_dir):
        nonlocal moved_count
        if dry_run:
            moved_count += 1
            return True
            
        target_file = target_ext_dir / src_file.name
        if target_file.exists():
            # Handle duplicates
            base_name = src_file.stem
            suffix = src_file.suffix
            counter = 1
            while target_file.exists():
                new_name = f"{base_name}_{counter}{suffix}"
                target_file = target_ext_dir / new_name
                counter += 1
                
        try:
            shutil.move(str(src_file), str(target_file))
            moved_count += 1
            return True
        except Exception as e:
            print(f"Error moving {src_file}: {e}")
            return False

    # Process files with extensions
    for ext, files in ext_map.items():
        ext_dir = target_dir / ext.replace('.', '_').lstrip('_')
        if not dry_run:
            ext_dir.mkdir(parents=True, exist_ok=True)
        for f in files:
            move_file(f, ext_dir)
            
    # Process files without extensions
    if no_ext_files:
        no_ext_dir = target_dir / "_