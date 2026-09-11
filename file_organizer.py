
<think>
The user wants a Python program that organizes files by sorting them into directories based on their file extensions.

Key requirements:
1.  **Functionality**: Look at files in a specified directory, read their extensions, and move them into subdirectories named after those extensions (e.g., `.jpg` files go to a `jpg` folder).
2.  **Robustness**: Handle errors (file in use, permission denied, file not found). Handle file existence (if file already exists in destination). Handle edge cases (files without extensions).
3.  **Self-contained**: Standard library only (`os`, `shutil`, `pathlib`).
4.  **CLI**: It should be easy to use, ideally via command line arguments or a simple interactive prompt, but a clean CLI interface is best for a "program".

Plan:
1.  Use `pathlib` for modern path manipulation.
2.  Define a main function that takes a target directory.
3.  Iterate through files in the directory.
4.  Identify extension.
5.  Create target folder (e.g., `.jpg` -> `Images/jpg` or just `jpg`). Let's stick to the extension name (e.g., `jpg`) or a category map. A simple approach is just the extension name (case-insensitive).
6.  Move the file.
7.  Add error handling (try-except blocks).
8.  Add a dry-run mode so the user can see what *would* happen before actually moving files. This is crucial for file manipulation tools to prevent data loss.

Refining the logic:
-   Input: Directory path.
-   Logic:
    -   List files.
    -   For each file:
        -   Get suffix (e.g., `.pdf`). Strip the dot for folder name (`pdf`).
        -   If no extension, maybe put in `Misc` or `NoExtension`.
        -   Create folder if not exists.
        -   Construct new path.
        -   If file exists at new path:
            -   Option A: Skip.
            -   Option B: Rename with counter (`filename_1.pdf`).
            -   Let's go with skipping or user prompt, but for a script, skipping with a warning or unique naming is safer. I'll implement a unique naming strategy (loop counter) to avoid overwriting.
        -   Move file.
-   Output: Print actions taken.

Let's structure the code:
-   `organize_files(target_dir, dry_run=False)`
-   Argument parsing using `argparse`.

Implementation details:
-   `os.walk` or `pathlib.Path.iterdir`? `iterdir` is fine for a single directory.
-   Handling extension: `path.suffix`.
-   Case sensitivity: Use `.lower()` for folder names.
-   Reserved characters in folder names: Extension is usually safe, but good to be aware.

Let's write the code.

```python
import os
import shutil
import argparse
from pathlib import Path

def get_unique_path(dest_path):
    """
    If dest_path exists, generate a unique filename by appending a counter.
    Example: file.jpg -> file_1.jpg -> file_2.jpg
    """
    if not dest_path.exists():
        return dest_path

    stem = dest_path.stem
    suffix = dest_path.suffix
    parent = dest_path.parent
    counter = 1
    while True:
        new_name = f"{stem}_{counter}{suffix}"
        new_path = parent / new_name
        if not new_path.exists():
            return new_path
        counter += 1

def organize_files(directory, dry_run=False):
    dir_path = Path(directory)
    
    if not dir_path.exists() or not dir_path.is_dir():
        print(f"Error: Directory '{directory}' does not exist or is not a directory.")
        return

    # Map to keep track of created folders to avoid redundant checks? 
    # Not strictly necessary, Path.exists check is fast.
    
    print(f"Scanning directory: {dir_path.resolve()}")
    
    files_moved = 0
    
    for item in dir_path.iterdir():
        # Skip directories (we are organizing files into subdirs)
        if item.is_dir():
            continue
            
        # Get extension
        extension = item.suffix
        if not extension:
            # Handle files without extension
            ext_folder_name = "no_extension"
            print(f"Skipping {item.name} (no extension) or moving to {ext_folder_name}? "
                  "Log: Files without extensions will be moved to 'unsorted'.")
            ext_folder_name = "unsorted"
        else:
            ext