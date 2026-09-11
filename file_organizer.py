
<think>
Here's a thinking process:

1.  **Understand User Goal**: The user wants a Python program that acts as a "file organizer" that sorts files by their extension. It should be clean, robust, self-contained, use only standard library modules, and be wrapped in a single markdown Python code block.

2.  **Key Requirements**:
   - Sort files by extension
   - Organize them (likely move/copy into folders named after the extension)
   - Self-contained, Python 3 standard library only
   - Robust (handle errors, skip files, handle missing directories, etc.)
   - Clean code structure

3.  **Core Functionality**:
   - Take a target directory as input
   - Scan files in that directory
   - Get file extension for each file
   - Create subdirectories named after the extension (e.g., `.txt`, `.jpg`, or without the dot: `txt`, `jpg`)
   - Move files into corresponding subdirectories
   - Handle edge cases: hidden files, files without extensions, existing files in destination, read-only files, etc.
   - Provide clear feedback/logging

4.  **Design Decisions**:
   - Use `pathlib` for modern, clean path handling
   - Use `shutil` for moving files
   - Use `os` or `sys` for command-line arguments
   - Handle extensions case-insensitively or normalize them (lowercase)
   - Skip directories (except maybe the organized ones) and hidden files
   - Handle files without extensions (put in a `no_extension` folder)
   - Add dry-run option? Maybe not required, but good for robustness. I'll stick to basic move but add safety checks.
   - Use `logging` for clean output

5.  **Implementation Steps**:
   - Parse command line args (target directory)
   - Validate directory exists and is readable
   - Iterate through files in the directory (non-recursive first, or maybe recursive? I'll stick to non-recursive for simplicity, but can add recursive option if needed. I'll keep it simple: single directory)
   - For each file:
     - Get suffix/extension
     - Normalize extension (lowercase, strip leading dot, handle empty)
     - Create target subdirectory
     - Move file (handle conflicts, permissions)
   - Use `pathlib.Path` throughout
   - Add try-except for robustness
   - Print/log progress

   Let's draft the code mentally:

   ```python
   import sys
   import shutil
   import logging
   from pathlib import Path

   def setup_logging():
       logging.basicConfig(
           level=logging.INFO,
           format='%(asctime)s - %(levelname)s - %(message)s'
       )

   def organize_files(directory: str) -> None:
       source_dir = Path(directory).resolve()
       if not source_dir.is_dir():
           logging.error(f"Directory does not exist or is not a directory: {source_dir}")
           sys.exit(1)

       logging.info(f"Organizing files in: {source_dir}")
       moved_count = 0
       skipped_count = 0

       # Get all files (non-directories) in the source directory
       files = [f for f in source_dir.iterdir() if f.is_file() and not f.name.startswith('.')]

       for file_path in files:
           # Get extension, handle missing extension
           ext = file_path.suffix.lower()
           ext_folder_name = ext.lstrip('.') if ext else 'no_extension'

           # Create destination directory
           dest_dir = source_dir / ext_folder_name
           if not dest_dir.is_dir():
               try:
                   dest_dir.mkdir(parents=True)
                   logging.info(f"Created directory: {dest_dir}")
               except OSError as e:
                   logging.error(f"Failed to create directory {dest_dir}: {e}")
                   continue

           dest_path = dest_dir / file_path.name

           # Handle naming conflicts
           if dest_path.exists():
               base = file_path.stem
               suffix = file_path.suffix
               counter = 1
               while dest_path.exists():
                   dest_path = dest_dir / f"{base}_{counter}{suffix}"
                   counter += 1
               logging.warning(f"File already exists, renamed to: {dest_path.name}")

           try:
               shutil.move(str(file_path), str(dest_path))
               logging.info(f"Moved: {file_path.name} -> {dest_dir.name}/")
               moved_count += 1
           except shutil.Error as e:
               logging.warning(f"Could not move {file_path.name}: {e}")
               skipped_count += 1
           except OSError as e:
               logging.error(f"OS