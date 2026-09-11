import os
import shutil
from pathlib import Path

def organize_files(target_dir):
    # Ensure target_dir is a Path object
    target_dir = Path(target_dir)
    
    if not target_dir.is_dir():
        print(f"Error: {target_dir} is not a valid directory.")
        return

    # File count for progress
    moved_count = 0
    
    # Iterate over items in the directory
    # Note: We only care about immediate children files, not recursing into subfolders for safety
    for item in target_dir.iterdir():
        if item.is_file():
            # Get the file suffix (extension)
            # e.g., "image.jpg" -> ".jpg"
            suffix = item.suffix
            
            if suffix:
                # Remove the leading dot and convert to lowercase for folder name
                # e.g., ".JPG" -> "jpg"
                folder_name = suffix[1:].lower()
            else:
                # Files without extension
                folder_name = "no_extension"
            
            # Construct the destination path
            dest_folder = target_dir / folder_name
            
            # Create folder if it doesn't exist
            if not dest_folder.exists():
                dest_folder.mkdir()
            
            # Construct full destination file path
            dest_file = dest_folder / item.name
            
            # Check if file already exists in destination to avoid overwrite
            if dest_file.exists():
                print(f"Skipping {item.name}, already exists in {dest_folder}")
            else:
                # Move the file
                try:
                    shutil.move(str(item), str(dest_file))
                    print(f"Moved {item.name} to {folder_name}/")
                    moved_count += 1
                except Exception as e:
                    print(f"Error moving {item.name}: {e}")

    print(f"Done. Organized {moved_count} files.")

if __name__ == "__main__":
    import sys
    
    # Check for command line argument, otherwise use current directory
    if len(sys.argv) > 1:
        directory_to_organize = sys.argv[1]
    else:
        directory_to_organize = "."
        
    organize_files(directory_to_organize)
