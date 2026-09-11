
<think>
The user wants a Python program that organizes files by extension. This means:
- It should look at files in a directory
- Group them by their file extension
- Move or copy them into subdirectories named after the extension
- Handle edge cases (no extension, hidden files, directories, etc.)
- Should be robust and self-contained

Let me think about the design:
1. Take a source directory as input (could be command line argument or default to current directory)
2. Scan all files in the directory
3. Group them by extension (e.g., .txt, .jpg, .pdf)
4. Create subdirectories for each extension
5. Move (or optionally copy) files into those subdirectories
6. Handle errors gracefully

Key considerations:
- Use `os` and `shutil` modules (standard library)
- Handle files without extensions
- Skip directories already created
- Handle duplicate filenames (e.g., same filename in different extensions or same name in multiple places)
- Make it safe - maybe add a dry-run mode or confirm before moving
- Handle special cases like hidden files (starting with .)
- The extension should be normalized (lowercase, with or without leading dot)

Let me write a robust implementation:

Features:
- Command-line interface with argparse
- Dry-run mode to preview changes
- Handle files with no extension
- Skip directories and the script itself
- Handle duplicate filenames
- Preserve original directory structure optionally (flat vs subdirectories)
- Use `shutil.move` for moving files

I'll structure it as a proper script with:
- A `FileOrganizer` class or functions
- Clear docstrings
- Error handling
- Progress output

Let me write this out carefully.
</think>

```python
#!/usr/bin/env python3
"""
A robust file organizer that sorts files by extension into subdirectories.

Usage:
    python file_organizer.py [OPTIONS] [DIRECTORY]

Options:
    --dry-run       Preview changes without moving files
    --copy          Copy files instead of moving them
    --no-dot        Exclude the leading dot from folder names
    --reverse-ext   Place files without extensions in 'no_extension' folder
"""

import os
import sys
import shutil
import argparse
from pathlib import Path
from collections import defaultdict


class FileOrganizer:
    """Organizes files in a directory by their extensions."""

    def __init__(self, source_dir: str, dry_run: bool = False, copy: bool = False,
                 no_dot: bool = False, reverse_ext: bool = False):
        self.source_dir = Path(source_dir).resolve()
        self.dry_run = dry_run
        self.copy = copy
        self.no_dot = no_dot
        self.reverse_ext = reverse_ext
        self.moved_files: list[tuple[str, str]] = []
        self.skipped_files: list[tuple[str, str]] = []
        self.created_dirs: list[str] = []
        self.errors: list[tuple[str, str]] = []

    def validate_source(self) -> bool:
        """Validate that the source directory exists and is accessible."""
        if not self.source_dir.exists():
            print(f"Error: Directory '{self.source_dir}' does not exist.")
            return False
        if not self.source_dir.is_dir():
            print(f"Error: '{self.source_dir}' is not a directory.")
            return False
        if not os.access(self.source_dir, os.R_OK | os.W_OK):
            print(f"Error: Insufficient permissions for '{self.source_dir}'.")
            return False
        return True

    def get_file_extension(self, file_path: Path) -> str:
        """
        Extract and normalize the file extension.
        
        Returns the extension including the leading dot, lowercased.
        Returns 'no_extension' for files without extensions.
        """
        # Handle files starting with dot (e.g., .gitignore, .bashrc)
        name = file_path.name
        if name.startswith('.') and '.' not in name[1:]:
            # Hidden file with no additional extension
            if self.reverse_ext:
                return 'no_extension'
            return 'no_extension'
        
        ext = file_path.suffix.lower()
        if not ext:
            return 'no_extension'
        return ext

    def get_target_directory(self, extension: str) -> Path:
        """Get the target directory path for a given extension."""
        if self.no_dot and extension != 'no_extension':
            dir_name = extension[1:]  # Remove the leading dot
        else:
            dir_name = extension
        return self.source_dir / dir_name

    def find_files(self) -> list[Path]:
        """Find all files in the source directory (non-recursive)."""
        files = []
        try:
            for item in self.source_dir.iterdir():
                if item.is_file():
                    files.append(item)
        except PermissionError as e:
            self.errors.append((str(self.source_dir), str(e)))
        except OSError as e:
            self.errors.append((str(self.source_dir), str(e)))
        return sorted(files, key=lambda x: x.name.lower())

    def group_by_extension(self, files: list[Path]) -> dict[str, list[Path]]:
        """Group files by their extensions."""
        groups = defaultdict(list)
        for file_path in files:
            ext = self.get_file_extension(file_path)
            groups[ext].append(file_path)
        return dict(groups)

    def resolve_duplicate_names(self, target_dir: Path, file_path: Path) -> Path:
        """
        Handle filename conflicts by appending a counter.
        Returns the target path that doesn't conflict.
        """
        target_path = target_dir / file_path.name
        if not target_path.exists():
            return target_path

        stem = file_path.stem
        ext = file_path.suffix
        counter = 1
        while True:
            new_name = f"{stem}_{counter}{ext}"
            target_path = target_dir / new_name
            if not target_path.exists():
                return target_path
            counter += 1

    def organize(self) -> bool:
        """Main method to perform the file organization."""
        if not self.validate_source():
            return False

        print(f"Scanning directory: {self.source_dir}")
        
        files = self.find_files()
        if not files:
            print("No files found to organize.")
            return True

        groups = self.group_by_extension(files)
        
        action = "DRY RUN" if self.dry_run else ("COPY" if self.copy else "MOVE")
        print(f"Action: {action}")
        print(f"Found {len(files)} file(s) in {len(groups)} extension group(s):\n")

        for ext in sorted(groups.keys()):
            file_list = groups[ext]
            target_dir = self.get_target_directory(ext)
            
            print(f"  [{ext}] {len(file_list)} file(s) -> {target_dir.name}/")
            
            if not self.dry_run:
                try:
                    if not target_dir.exists():
                        target_dir.mkdir(parents=True)
                        self.created_dirs.append(str(target_dir))
                        print(f"    Created directory: {target_dir}")
                    elif not target_dir.is_dir():
                        self.errors.append((str(target_dir), "Path exists but is not a directory"))
                        continue
                except PermissionError as e:
                    self.errors.append((str(target_dir), f"Permission denied: {e}"))
                    continue
                except OSError as e:
                    self.errors.append((str(target_dir), str(e)))
                    continue

            for file_path in file_list:
                # Skip files that are already in the correct directory
                if file_path.parent == target_dir:
                    print(f"    SKIP (already in place): {file_path.name}")
                    self.skipped_files.append((str(file_path), "already in correct directory"))
                    continue
                # Skip files owned by this script
                if file_path.name == __file__ or (file_path.name in ['file_organizer.py', 
                                                                     '__pycache__']):
                    print(f"    SKIP (script file): {file_path.name}")
                    self.skipped_files.append((str(file_path), "script file"))
                    continue

                target_path = self.resolve_duplicate_names(target_dir, file_path)
                
                action_str = "WOULD COPY" if self.dry_run and self.copy else \
                            "WOULD MOVE" if self.dry_run else \
                            ("COPY" if self.copy else "MOVE")
                
                if self.dry_run:
                    print(f"    {action_str}: {file_path.name} -> {target_dir.name}/{target_path.name}")
                else:
                    try:
                        if self.copy:
                            shutil.copy2(str(file_path), str(target_path))
                        else:
                            shutil.move(str(file_path), str(target_path))
                        self.moved_files.append((str(file_path), str(target_path)))
                        print(f"    {action_str}: {file_path.name} -> {target_dir.name}/{target_path.name}")
                    except shutil.Error as e:
                        self.errors.append((str(file_path), f"Shutil error: {e}"))
                        print(f"    ERROR: {file_path.name} - {