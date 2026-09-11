#!/usr/bin/env python3
"""
File Organizer - Sorts files by their extension into subdirectories.

Usage:
    python organize_files.py <target_directory> [--recursive] [--dry-run] [--force]

This script scans the specified directory, groups files by their extension,
and moves them into subdirectories named after each extension (e.g., .txt files
go to a 'txt/' subdirectory, .jpg files go to a 'jpg/' subdirectory, etc.).

Files without extensions are placed in a 'no_extension/' directory.
"""

import argparse
import os
import shutil
import sys
from pathlib import Path
from typing import Dict, List, Optional


def parse_arguments() -> argparse.Namespace:
    """Parse command-line arguments."""
    parser = argparse.ArgumentParser(
        description="Organize files in a directory by their extension."
    )
    parser.add_argument(
        "directory",
        type=str,
        help="Path to the directory containing files to organize."
    )
    parser.add_argument(
        "-r", "--recursive",
        action="store_true",
        help="Search subdirectories recursively."
    )
    parser.add_argument(
        "-n", "--dry-run",
        action="store_true",
        help="Show what would be done without actually moving any files."
    )
    parser.add_argument(
        "-f", "--force",
        action="store_true",
        help="Overwrite destination files if they already exist."
    )
    parser.add_argument(
        "-s", "--source-dir",
        type=str,
        default=None,
        help="Source directory (defaults to current directory if not specified)."
    )
    return parser.parse_args()


def get_extension_directory(base_dir: Path, extension: str) -> Path:
    """
    Create and return the path to the destination directory for a given extension.
    
    Args:
        base_dir: The root directory being organized.
        extension: The file extension (e.g., '.txt' or 'no_extension').
        
    Returns:
        Path object for the destination directory.
    """
    if extension.startswith("."):
        extension_dir_name = extension[1:]  # Remove the leading dot
    else:
        extension_dir_name = extension
    dest_dir = base_dir / extension_dir_name
    return dest_dir


def handle_duplicate_name(dest_dir: Path, file_path: Path, force: bool) -> Path:
    """
    Handle duplicate filenames in the destination directory.
    
    Args:
        dest_dir: The destination directory.
        file_path: The original file path.
        force: Whether to overwrite existing files.
        
    Returns:
        The final destination path for the file.
    """
    dest_path = dest_dir / file_path.name
    if not dest_path.exists():
        return dest_path
    if force:
        return dest_path
    # Add a suffix to make the filename unique
    stem = file_path.stem
    suffix = file_path.suffix
    counter = 1
    while dest_path.exists():
        new_name = f"{stem}_{counter}{suffix}"
        dest_path = dest_dir / new_name
        counter += 1
    return dest_path


def organize_files(directory: Path, recursive: bool, dry_run: bool, force: bool) -> None:
    """
    Organize files in the specified directory by their extension.
    
    Args:
        directory: Path to the directory to organize.
        recursive: Whether to search subdirectories recursively.
        dry_run: If True, only print what would be done without moving files.
        force: If True, overwrite existing destination files.
    """
    if not directory.is_dir():
        print(f"Error: '{directory}' is not a valid directory.", file=sys.stderr)
        sys.exit(1)
        
    # Collect all files
    if recursive:
        file_iter = directory.rglob("*")
    else:
        file_iter = directory.glob("*")
        
    files_to_move: List[Path] = []
    for item in file_iter:
        if item.is_file() and not item.name.startswith("."):  # Skip hidden files
            if item != Path(__file__).resolve():  # Skip this script
                files_to_move.append(item)
                
    # Group files by extension
    extension_groups: Dict[str, List[Path]] = {}
    for file_path in files_to_move:
        ext = file_path.suffix or "no_extension"
        extension_groups.setdefault(ext, []).append(file_path)
        
    # Display summary
    print(f"Found {len(files_to_move)} files to organize.")
    for ext, files in sorted(extension_groups.items()):
        print(f"  {ext or '(no extension)'}): {len(files)} file(s)")
    print()
    
    # Move files
    moved_count = 0
    for ext, files in extension_groups.items():
        dest_dir = get_extension_directory(directory, ext)
        
        if not dry_run:
            dest_dir.mkdir(parents=True, exist_ok=True)
        else:
            print(f"[DRY RUN] Would create directory: {dest_dir}")
            
        for file_path in files:
            # Skip files that are already in their correct destination directory
            if file_path.parent == dest_dir:
                continue
                
            dest_path = handle_duplicate_name(dest_dir, file_path, force)
            
            if dry_run:
                print(f"[DRY RUN] Would move: {file_path.relative_to(directory)} -> {dest_path.relative_to(directory)}")
            else:
                try:
                    shutil.move(str(file_path), str(dest_path))
                    print(f"Moved: {file_path.relative_to(directory)} -> {dest_path.relative_to(directory)}")
                    moved_count += 1
                except Exception as e:
                    print(f"Error moving {file_path}: {e}", file=sys.stderr)
                    
    print(f"\nMoved {moved_count} files.")
    
    # Remove empty directories if recursive and not dry-run
    if recursive and not dry_run:
        for dir_path in sorted(directory.rglob("*"), reverse=True):
            if dir_path.is_dir():
                try:
                    # Only remove if it's empty and not one of the extension directories
                    if not any(dir_path.iterdir()):
                        # Check if this is an extension directory
                        dir_name = dir_path.name
                        if any(dir_name == ext[1:] if ext.startswith(".") else ext 
                               for ext in extension_groups.keys() 
                               if ext != "no_extension" or dir_name == "no_extension"):
                            continue
                        dir_path.rmdir()
                        print(f"Removed empty directory: {dir_path.relative_to(directory)}")
                except OSError:
                    pass  # Directory not empty or permission error                   


def main():
    """Main entry point for the file organizer."""
    args = parse_arguments()
    
    target_dir = Path(args.directory).resolve()
    
    print("=== File Organizer ===")
    print(f"Target directory: {target_dir}")
    print(f"Recursive: {args.recursive}")
    print(f"Dry Run: {args.dry_run}")
    print(f"Force overwrite: {args.force}")
    print("=" * 30)
    
    organize_files(target_dir, args.recursive, args.dry_run, args.force)


if __name__ == "__main__":
    main()
