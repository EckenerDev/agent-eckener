
<think>
The user wants a Python program that sorts files in a directory by their extension.
I should create a script that:
1. Takes a source directory as input (or uses a default).
2. Scans the directory for files.
3. Determines the extension of each file.
4. Moves or copies the files into subdirectories named after their extensions.
5. Handles potential errors (like missing directories, permission issues, or files without extensions).
6. Is robust and self-contained using only standard library modules.

Key features to implement:
- `os` and `shutil` for file operations.
- `pathlib` might be cleaner for path handling.
- Input argument parsing (optional, but good for CLI).
- Dry-run mode (very useful for file organizers).
- Logging or verbose output to show what's happening.

Plan:
1. Define a function `organize_files(source_dir, dry_run=False)`.
2. In the function:
   - Iterate over items in `source_dir`.
   - Skip directories, only process files.
   - Get the file extension using `pathlib.Path.suffix`.
   - Handle empty extensions (name.lower().split('.')[-1] or just `.pdf`).
   - Create target path: `source_dir / extension_group_name`.
   - If `dry_run`, print what *would* happen.
   - Else, move file using `shutil.move`.
   - Handle duplicates (filenames might clash if files from different locations have same name? Actually, we are moving *into* extension folders within the *same* source dir, so names might clash if two files have same name and extension? No, we are grouping by extension, so if two files have same name and extension, one might already be in the target folder? Or maybe the source has duplicates? Unlikely but possible. I should handle destination exists or rename files to avoid overwriting.)
3. Add argument parsing.
4. Write the full script.

Refining the file moving logic:
- If target file exists, rename source file to avoid collision (e.g., prefix with timestamp or unique ID).
- Extensions should be normalized (lowercase, remove dot).

Let's write the code.

Structure:
```python
import os
import shutil
from pathlib import Path
import argparse
import sys
import time
import uuid
import logging

# Setup logging
logger = logging.getLogger('FileOrganizer')
logger.setLevel(logging.INFO)
handler = logging.StreamHandler()
formatter = logging.Formatter('%(message)s')
handler.setFormatter(formatter)
logger.addHandler(handler)

def organize_files(source_dir, dry_run=False):
    source_path = Path(source_dir)
    if not source_path.is_dir():
        raise ValueError(f"Source directory '{source_path}' does not exist or is not a directory.")

    # Collect files to move, avoiding processing newly created directories or moved files if they end up in the same directory
    # It's safer to collect the list of files first, then move them.
    files_to_process = [f for f in source_path.iterdir() if f.is_file()]

    moved_files = []
    
    for file_path in files_to_process:
        suffix = file_path.suffix.lower()
        if not suffix:
            # Files without extensions
            folder_name = "no_extension"
        else:
            folder_name = suffix[1:] # Remove the dot
        
        target_dir = source_path / folder_name
        target_file = target_dir / file_path.name

        # Handle file collision
        iteration = 0
        while target_file.exists():
            # Generate unique name if collision occurs
            # Renaming pattern: name.ext -> name_timestamp.ext or name_unique.ext
            # Simpler: prepend a random string or use UUID
            unique_name = f"{uuid.uuid4().hex}_{file_path.name}"
            target_file = target_dir / unique_name
            break # Break after one rename attempt is usually enough for unique UUIDs
        
        # Perform move or dry run
        if dry_run:
            logger.info(f"DRY RUN: Move '{file_path}' -> '{target_file}'")
        else:
            try:
                target_dir.mkdir(parents=True, exist_ok=True)
                shutil.move(str(file_path), str(target_file))
                logger.info(f"Moved '{file_path.name}' -> '{folder_name}/'")
                moved_files.append(file_path)
            except Exception as e:
                logger.error(f"Failed to move '{file_path.name}': {e}")

    if not dry_run:
        # Optionally remove empty directories created? No, we created them and populated them.
        # But what if a folder was moved out and left empty? That's fine.
        pass

if __