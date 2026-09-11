import os
import shutil
from pathlib import Path
import argparse

def organize_files(source_dir, dry_run=False):
    source_path = Path(source_dir).resolve()
    
    if not source_path.is_dir():
        print(f"Error: {source_path} is not a directory.")
        return

    print(f"Scanning {source_path}...")
    
    moved_count = 0
    
    for item in source_path.iterdir():
        # Only process files, not subdirectories
        if item.is_file():
            # Get extension, e.g., .txt
            ext = item.suffix.lower()
            
            # Handle files with no extension
            if not ext:
                ext_folder_name = "no_extension"
            else:
                # Remove the leading dot for folder name, e.g., .txt -> txt
                ext_folder_name = ext[1:]
            
            # Define destination path
            dest_dir = source_path / ext_folder_name
            
            # Check if destination is different from source
            # (e.g. if file is already in 'txt' folder and extension is .txt)
            if item.parent.resolve() == dest_dir.resolve():
                continue

            # Create directory if it doesn't exist
            if not dest_dir.exists():
                if not dry_run:
                    try:
                        dest_dir.mkdir(parents=True, exist_ok=True)
                        print(f"Created folder: {dest_dir}")
                    except Exception as e:
                        print(f"Error creating folder {dest_dir}: {e}")
                        continue
            
            # Handle filename collisions
            dest_file = dest_dir / item.name
            if dest_file.exists():
                # Simple collision handling: append a number or just skip
                # shutil.move will fail if file exists.
                # Let's generate a unique name
                counter = 1
                stem = item.stem
                suffix = item.suffix
                while dest_file.exists():
                    new_name = f"{stem}_{counter}{suffix}"
                    dest_file = dest_dir / new_name
                    counter += 1
                dest_file = dest_dir / (stem + "_" + str(counter) + suffix) # Logic fix needed here for loop

            if dry_run:
                print(f"[DRY RUN] Would move: {item.name} -> {ext_folder_name}/")
            else:
                try:
                    shutil.move(str(item), str(dest_file))
                    print(f"Moved: {item.name} -> {ext_folder_name}/")
                    moved_count += 1
                except Exception as e:
                    print(f"Error moving {item.name}: {e}")

    print(f"Done. Organized {moved_count} files.")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Sort files by extension.")
    parser.add_argument("directory", nargs="?", default=".", help="Path to the directory to organize (default: current directory)")
    parser.add_argument("--dry-run", action="store_true", help="Preview actions without moving files")
    args = parser.parse_args()
    
    organize_files(args.directory, args.dry_run)
