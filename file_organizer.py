import os
import shutil
from pathlib import Path

class FileOrganizer:
    def __init__(self, source_dir, dry_run=False):
        self.source_dir = Path(source_dir)
        self.dry_run = dry_run
        
    def organize(self):
        if not self.source_dir.is_dir():
            print(f"Error: {self.source_dir} is not a valid directory.")
            return

        # Iterate over files in the directory
        files = [f for f in self.source_dir.iterdir() if f.is_file()]
        
        for file in files:
            ext = file.suffix
            # Normalize extension: strip the dot, make lowercase
            ext_folder_name = ext[1:].lower() if ext else "no_extension"
            
            dest_dir = self.source_dir / ext_folder_name
            self._ensure_dir(dest_dir)
            
            dest_file = dest_dir / file.name
            
            self._move_file(file, dest_file)

    def _ensure_dir(self, path):
        if not self.dry_run:
            path.mkdir(exist_ok=True)
        else:
            print(f"  [DRY-RUN] Would create directory: {path}")

    def _move_file(self, src, dest):
        # Check if file already exists in dest
        if dest.exists():
            # Handle collision
            counter = 1
            stem = dest.stem
            while dest.exists():
                dest = dest.with_name(f"{stem}_{counter}{dest.suffix}")
                counter += 1
        
        print(f"Moving: {src.name} -> {dest.parent.name}/")
        if not self.dry_run:
            try:
                shutil.move(str(src), str(dest))
            except Exception as e:
                print(f"Error moving {src}: {e}")
        else:
            print(f"  [DRY-RUN] Would move {src} to {dest}")

if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(description="Sort files by extension.")
    parser.add_argument("directory", nargs="?", default=".", help="Directory to organize")
    parser.add_argument("-y", "--yes", action='store_true', help="Execute moves (default is dry-run)")
    
    args = parser.parse_args()
    
    # If --yes is not passed, treat as dry run for safety
    dry_run = not args.yes
    
    organizer = FileOrganizer(args.directory, dry_run)
    organizer.organize()
