import os
import shutil
from pathlib import Path

def organize_files(directory_path):
    # Validate input directory
    if not os.path.isdir(directory_path):
        print(f"Error: {directory_path} is not a valid directory.")
        return

    # Iterate through files
    for item in os.listdir(directory_path):
        source_path = os.path.join(directory_path, item)
        
        # Skip directories
        if os.path.isdir(source_path):
            continue
            
        # Skip the script itself if it's in the directory (optional safety)
        # But usually users run this on a specific data folder.
        
        # Get extension
        # use().suffix gives '.txt', etc. If no ext, it gives ''
        ext = os.path.splitext(item)[1]
        
        dest_dir_name = ext if ext else "no_extension"
        dest_dir_path = os.path.join(directory_path, dest_dir_name)
        
        # Create dir
        os.makedirs(dest_dir_path, exist_ok=True)
        
        dest_file_path = os.path.join(dest_dir_path, item)
        
        # Handle collision
        counter = 1
        base_name, file_ext = os.path.splitext(item)
        while os.path.exists(dest_file_path):
            # Construct new name: name (1).ext, name (2).ext
            # If file had no ext, just name (1)
            if file_ext:
                new_name = f"{base_name} ({counter}){file_ext}"
            else:
                new_name = f"{base_name} ({counter})"
            
            dest_file_path = os.path.join(dest_dir_path, new_name)
            counter += 1
        
        # Move
        try:
            shutil.move(source_path, dest_file_path)
            print(f"Moved: {item} -> {dest_dir_name}/")
        except Exception as e:
            print(f"Error moving {item}: {e}")

# Main block to run
if __name__ == "__main__":
    # Ask user or use CWD
    path = input("Enter directory path (leave empty for current): ").strip()
    if not path:
        path = os.getcwd()
    organize_files(path)
