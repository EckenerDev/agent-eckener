
<think>
The user wants a Python program that organizes/sorts files by extension. Let me think about what this entails:

1. The program should scan a directory (or work with files in the current directory)
2. Group files by their file extensions
3. Organize them - this likely means moving them into subdirectories named after their extensions, or at least listing them grouped by extension.

Let me write a robust, clean Python program that:
1. Takes a source directory as input (defaults to current directory)
2. Scans for files
3. Groups them by extension
4. Optionally moves them into subdirectories named by extension (or just lists them)
5. Has a dry-run mode for safety
6. Handles edge cases (no extension, hidden files, already organized directories, etc.)

I'll make it a command-line tool with argparse for a clean interface. It should:
- Accept a directory path
- Support a dry-run flag
- Support a move action (actually move files into extension-named subdirectories)
- Skip files that already exist in the correct location
- Handle errors gracefully
- Provide verbose logging

Let me design this carefully:

- Use `pathlib` for path handling (Python 3.4+)
- Use `argparse` for CLI
- Use `shutil` for moving files
- Group files by their `.lower()` suffix to normalize extensions
- Handle files with no extension separately
- Skip directories recursively or just work on the top level

I'll make it organized and well-documented with clear structure.

Let me write the code now.
</think>

```python
"""
File Organizer: Sorts files in a directory by their file extensions.

Creates subdirectories named after each extension (e.g., .jpg files -> jpg/)
and moves corresponding files into them. Includes dry-run mode for safe previewing.

Usage examples:
    python organize.py /path/to/directory
    python organize.py . --dry-run
    python organize.py ./photos --verbose
"""

import argparse
import logging
import os
import shutil
import sys
from pathlib import Path

# ---------------------------------------------------------------------------
# Constants & Logging Setup
# ---------------------------------------------------------------------------
logger = logging.getLogger("FileOrganizer")

# Custom file types that should not be moved (e.g., system files)
_SKIPPED_EXTENSIONS = {
    ".lnk",  # Windows shortcuts
    ".desktop",  # Linux desktop files
    ".sh",  # Shell scripts
    ".bat",  # Windows batch files
    ".exe",  # Executables
}

def setup_logging(verbose: bool = False) -> None:
    """Configure logging levels and formatting."""
    level = logging.DEBUG if verbose else logging.INFO
    logger.setLevel(level)
    handler = logging.StreamHandler(sys.stdout)
    formatter = logging.Formatter("[%(levelname)s] %(message)s")
    handler.setFormatter(formatter)
    logger.addHandler(handler)


# ---------------------------------------------------------------------------
# Core Organization Logic
# ---------------------------------------------------------------------------
def get_extension(filename: str) -> str:
    """Extract and normalize the file extension."""
    suffix = Path(filename).suffix.lower()
    return suffix


def group_files_by_extension(directory: Path) -> dict[str, list[Path]]:
    """Group files in the given directory by their extension."""
    groups: dict[str, list[Path]] = {}  # Extension -> list of file paths

    for item in directory.iterdir():
        if not item.is_file():
            continue

        # Skip hidden files (starting with a dot)
        if item.name.startswith("."):
            continue

        ext = get_extension(item.name)
        if not ext:
            ext = "no_extension"

        if ext in _SKIPPED_EXTENSIONS:
            logger.debug(f"Skipping {ext} file: {item.name}")
            continue

        groups.setdefault(ext, []).append(item)

    return groups


def organize_files(directory: Path, dry_run: bool = False) -> int:
    """Move files into subdirectories named by their extensions.

    Returns the number of files processed.
    """
    directory = directory.resolve()
    if not directory.is_dir():
        raise FileNotFoundError(f"'{directory}' is not a valid directory.")

    groups = group_files_by_extension(directory)
    if not groups:
        logger.info("No files found to organize.")
        return 0

    processed_count = 0
    for ext, files in groups.items():
        # Sanitize extension name for directory creation
        dir_name = ext if ext != "no_extension" else ext

        target_dir = directory / dir_name
        should_create = False

        if not target_dir.exists():
            should_create = True
        elif not target_dir.is_dir():
            raise FileExists