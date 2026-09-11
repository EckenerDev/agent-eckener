   import argparse
   import logging
   import os
   import shutil
   import sys
   from pathlib import Path
   from typing import Dict, List, Optional

   def setup_logging(verbose: bool) -> logging.Logger:
       logger = logging.getLogger("file_organizer")
       logger.setLevel(logging.DEBUG if verbose else logging.INFO)
       handler = logging.StreamHandler(sys.stdout)
       handler.setFormatter(logging.Formatter("%(levelname)s: %(message)s"))
       logger.addHandler(handler)
       return logger

   def collect_files(directory: Path, skip_hidden: bool = True) -> List[Path]:
       files = []
       for p in directory.iterdir():
           if p.is_file() and not p.is_symlink():
               if skip_hidden and p.name.startswith(('.', '_'))):
                   continue
               files.append(p)
       return files

   def normalize_extension(ext: str) -> str:
       if not ext or ext == '.':
           return "no_extension"
       # Remove leading dot, convert to lowercase
       return ext.lower().lstrip('.')

   def resolve_collision(target_path: Path, logger: logging.Logger) -> Path:
       if not target_path.exists():
           return target_path
       stem = target_path.stem
       suffix = target_path.suffix
       parent = target_path.parent
       counter = 1
       while True:
           new_name = f"{stem}_{counter}{suffix}"
           new_path = parent / new_name
           if not new_path.exists():
               logger.info(f"Collision detected. Renaming to {new_name}")
               return new_path
           counter += 1

   def organize_files(directory: Path, dry_run: bool = False, skip_hidden: bool = True, force: bool = False):
       logger = setup_logging(verbose=True) # Actually, let's pass verbose from CLI
       # ... implementation details ...
   
