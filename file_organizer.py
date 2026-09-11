
<think>
The user wants a Python program to organize files by their extension.
This should be a self-contained script using only the standard library.
It should be robust, clean, and follow best practices.

Key features to consider:
1.  **Recursive Search**: It should probably look through a directory tree, not just the top level.
2.  **Configuration**: The user might want to specify the target directory.
3.  **Duplicate Handling**: What if a file with the same name already exists in the target subdirectory?
4.  **Excluded Extensions**: Maybe allow skipping certain extensions (like hidden files or system files).
5.  **Logging/Output**: It should report what it's doing so the user knows if it worked.
6.  **Dry Run**: A very useful feature for organizers is to see what *would* happen without moving files.

Plan:
1.  Import necessary modules: `pathlib`, `shutil`, `argparse`, `logging`.
2.  Use `argparse` for command-line arguments (source directory, dry run flag, verbose flag).
3.  Implement a function `organize_files(directory)`.
4.  Iterate through files in the directory (non-recursive or recursive? Recursive is usually more useful, but let's stick to the provided directory's contents to avoid accidentally moving system files from deep nested paths unless specified. Actually, a standard "file organizer" usually works on a specific folder like 'Downloads'. I'll stick to top-level or allow recursive. Let's do top-level of the specified folder to be safe, or make it recursive. Let's go with recursive as it's more powerful, but handle it carefully).
    - *Correction*: A safer default for an organizer is the specific directory provided. If I recurse, I might move files from `~/Downloads/Projects/Code/src/file.py` into `~/Downloads/code/`, breaking the project structure. Let's stick to a single directory level or ask the user. Let's stick to the immediate contents of the directory provided.
5.  Logic:
    - Identify file extension.
    - Determine target subdirectory (e.g., `.pdf` -> `pdf`).
    - Create subdirectory if not exists.
    - Handle naming conflicts (e.g., `file.pdf` already in `pdf/` -> rename to `file_1.pdf`).
    - Move file.
6.  Robustness:
    - Handle permissions.
    - Handle special files (directories, symlinks).
    - Case sensitivity (extensions like `.PDF` vs `.pdf`). Usually, standardizing to lowercase for folder names is good.

Refined Plan:
1.  Use `pathlib` for path manipulation.
2.  `argparse` for input.
3.  Handle extensions:
    - Case 1: `.jpg` -> folder `images` (Categorization).
    - Case 2: `.jpg` -> folder `jpg` (Literal).
    - Literal is safer for a general tool. I'll stick to literal extension mapped to folder name.
4.  Name collision resolution: Append a counter.

Code Structure:
- `get_extension(filename)`: Extracts extension.
- `find_unique_path(dest_dir, filename)`: Handles existing files.
- `organize(dir_path, dry_run=False)`: Main logic loop.
- `main()`: Entry point.

Let's refine the "duplicate handling".
If I move `report.pdf` to `./pdf/`, and `./pdf/report.pdf` exists:
Rename source to `report_1.pdf`, move to `./pdf/report_1.pdf`.
If `report_1.pdf` exists, `report_2.pdf`, etc.

Let's write the code.

```python
import os
import shutil
import argparse
from pathlib import Path
import logging

# Setup logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

def resolve_conflict(destination_path):
    """
    If a file already exists at destination_path, append a counter 
    to the filename until a unique name is found.
    """
    if not destination_path.exists():
        return destination_path
    
    dir_path = destination_path.parent
    stem = destination_path.stem
    suffix = destination_path.suffix
    
    counter = 1
    while True:
        new_name = f"{stem}_{counter}{suffix}"
        new_path = dir_path / new_name
        if not new_path.exists():
            return new_path
        counter += 1

def organize_files(source_dir, dry_run=False):
    """
    Organizes files in the specified directory by their extension.
    """
    source_path = Path(source_dir)
    
