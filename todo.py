     import json
     import os
     from typing import List, Dict, Optional

     class TodoManager:
         def __init__(self, storage_file: str = "todos.json"):
             self.todos: List[Dict[str, any]] = []
             self.next_id: int = 1
             self.storage_file: str = storage_file
             self._load()

         def _load(self) -> None: ...
         def _save(self) -> None: ...
         def add(self, text: str) -> None: ...
         def remove(self, task_id: int) -> bool: ...
         def list(self) -> None: ...
     
