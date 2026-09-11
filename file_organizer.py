   import os
   import shutil
   from pathlib import Path

   def organize_files(directory, dry_run=False):
       dir_path = Path(directory)
       if not dir_path.is_dir():
           print(f"Error: {directory} is not a valid directory.")
           return

       # Dictionary to track extension -> target folder
       # We can just process file by file to avoid keeping state in memory

       for item in dir_path.iterdir():
           if not item.is_file():
               continue
           # Skip hidden files
           if item.name.startswith('.'):
               continue

           ext = item.suffix.lower()
           folder_name = f"{ext.lstrip('.')}_files" if ext else "no_extension_files"
           target_dir = dir_path / folder_name

           if dry_run:
               print(f"[DRY RUN] Would move '{item.name}' to '{target_dir.name}/'")
               continue

           try:
               target_dir.mkdir(exist_ok=True)
               target_path = target_dir / item.name
               # Handle name collisions
               if target_path.exists():
                   base = item.stem
                   counter = 1
                   while target_path.exists():
                       target_path = dir_path / folder_name / f"{base}_{counter}{ext}"
                       counter += 1
               shutil.move(str(item), str(target_path))
               print(f"Moved: {item.name} -> {target_dir.name}/")
           except Exception as e:
               print(f"Error moving {item.name}: {e}")

   if __name__ == "__main__":
       import argparse
       parser = argparse.ArgumentParser(description="Organize files by extension in a directory.")
       parser.add_argument("directory", help="Path to the directory to organize")
       parser.add_argument("--dry-run", action="store_true", help="Preview changes without moving files")
       args = parser.parse_args()
       organize_files(args.directory, args.dry_run)
   
