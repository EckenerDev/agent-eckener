
<think>
The user wants a Python program that organizes files by their extension.
The program should:
1.  Scan a target directory.
2.  Move/copy files into subdirectories named after their extensions (e.g., `.jpg` to `images/`, `.pdf` to `documents/`).
3.  Handle edge cases like missing extensions, hidden files, permissions, or files without read/write access.
4.  Be self-contained using only the standard library.
5.  Be robust and clean.

Plan:
1.  Import `os`, `shutil`, and `argparse` for command-line interaction.
2.  Define a function to process a directory.
3.  Loop through files in the directory.
4.  Check if the item is a file (not a directory).
5.  Extract the extension.
6.  Normalize the extension (lowercase, remove the dot).
7.  Handle cases where there is no extension.
8.  Construct the destination directory path.
9.  Create the destination directory if it doesn't exist.
10. Move the file to the destination handle name collisions.
11. Use `argparse` to allow the user to specify the directory. Optional: dry-run flag.

Refinement on "Robustness":
*   Name collisions: If `file.txt` exists in `txt/`, and we try to move `file.txt`, `shutil.move` might overwrite or error depending on context. Better to append a suffix or skip. Let's skip to avoid data loss, or rename. Standard `shutil.move` overwrites in newer Python versions? Actually, it raises an error if destination exists on some OS, or might overwrite. Let's handle collisions by appending `_1`, `_2`, etc.
*   Hidden files: Start with `.`. Should they be organized? Usually yes, or maybe ignored. Let's organize them but maybe group them into `misc` or keep logic simple.
*   Directories: The script should recursively organize files or just the top level? Usually, simple organizers are top-level only to prevent massive movement operations unless specified. Let's stick to top-level for the first pass, or allow a recursive flag. Let's stick to non-recursive for safety unless requested, but perhaps add a recursive option.
*   Extensions without dots: e.g., `Makefile`. Treat as `no_extension` or based on name? Standard is `os.path.splitext`. `Makefile` -> `('Makefile', '')`.
*   Extensions with multiple dots: `file.tar.gz`. `os.path.splitext` returns `.gz`. This is usually correct for file types.

Let's refine the collision handling.
If `dest` exists:
`base, ext = os.path.splitext(filename)`
`dest_path = f"{dest_dir}/{filename}"`
`counter = 1`
`while os.path.exists(dest_path):`
`new_name = f"{base}_{counter}{ext}"`
`dest_path = f"{dest_dir}/{new_name}"`
`counter += 1`

Let's write the code structure.

```python
import os
import shutil
import argparse
import sys

def organize_files(target_dir, recursive=False, dry_run=False):
    # Validation
    if not os.path.isdir(target_dir):
        print(f"Error: {target_dir} is not a valid directory.")
        return

    # Iterate
    for filename in os.listdir(target_dir):
        src_file = os.path.join(target_dir, filename)

        if os.path.isdir(src_file):
            if recursive:
                organize_files(src_file, recursive=True, dry_run=dry_run)
            continue

        src_path = os.path.abspath(src_file) # Use absolute to avoid path mixups
        
        _, ext = os.path.splitext(filename)
        
        # Extension handling
        if ext:
            folder_name = ext[1:].lower() # remove dot, lowercase
        else:
            folder_name = "no_extension" # or "misc"

        dest_dir = os.path.join(target_dir, folder_name)
        
        # Check if moving to a different folder (avoid infinite loop if recursive)
        # If in A/file.txt, dest is A/txt/file.txt. 
        # If src is already inside a subfolder, logic needs care.
        # But usually this script runs on a 'Downloads' folder.
        
        if dry_run:
            print(f"[DRY RUN] Would move {filename} -> {folder_name}/")
            continue

        # Create dir
        os.makedirs(dest_dir, exist_ok=True)

        dest_path = os.path.join(dest_dir, filename)

        # Handle name collision
        if os.path.exists(dest_path):
            base, file_ext = os.path.splitext