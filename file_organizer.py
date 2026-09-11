   import os
   import shutil
   import argparse
   from pathlib import Path
   import sys

   def main():
       parser = argparse.ArgumentParser(description="Organize files in a directory by extension.")
       parser.add_argument("directory", nargs="?", default=".", help="Target directory to organize (default: current directory)")
       parser.add_argument("--dry-run", action="store_true", help="Show what would be done without moving files")
       parser.add_argument("--recursive", action="store_true", help="Process subdirectories recursively")
       args = parser.parse_args()

       target_dir = Path(args.directory).resolve()
       if not target_dir.is_dir():
           print(f"Error: '{target_dir}' is not a valid directory.")
           sys.exit(1)

       # Collect files
       files_to_organize = []
       if args.recursive:
           iterator = target_dir.rglob("*")
       else:
           iterator = target_dir.iterdir()

       for item in iterator:
           if item.is_file() and not item.name.startswith('.'): # Skip hidden files for safety
               files_to_organize.append(item)

       # Group by extension
       ext_groups = {}
       for file_path in files_to_organize:
           ext = file_path.suffix.lower().lstrip('.') or "no_extension"
           if ext not in ext_groups:
               ext_groups[ext] = []
           ext_groups[ext].append(file_path)

       # Show summary
       print(f"Found {len(files_to_organize)} file(s) to organize:")
       for ext, files in sorted(ext_groups.items()):
           print(f"  .{ext} ({len(files)} files):")
           for f in files:
               print(f"    - {f.name}")

       if args.dry_run:
           print("\n[Dry Run] No files were moved.")
           return

       # Move files
       moved_count = 0
       skipped_count = 0
       for ext, files in ext_groups.items():
           dest_dir = target_dir / ext
           dest_dir.mkdir(exist_ok=True)

           for file_path in files:
               dest_path = dest_dir / file_path.name
               try:
                   if dest_path.exists():
                       # Handle collision
                       base = file_path.stem
                       suffix = file_path.suffix
                       counter = 1
                       while dest_path.exists():
                           new_name = f"{base}_{counter}{suffix}"
                           dest_path = dest_dir / new_name
                           counter += 1
                   shutil.move(str(file_path), str(dest_path))
                   print(f"Moved: {file_path.name} -> {dest_path.name}")
                   moved_count += 1
               except Exception as e:
                   print(f"Failed to move {file_path.name}: {e}")
                   skipped_count += 1

       print(f"\nDone. Moved: {moved_count}, Skipped: {skipped_count}")

   if __name__ == "__main__":
       main()
   
