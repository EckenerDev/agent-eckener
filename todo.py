
<think>
The user wants a Python program for a todo list manager.
It needs to have:
1.  Add function
2.  Remove function
3.  List function
4.  No external dependencies.
5.  Clean, robust, self-contained code.
6.  Single markdown python fenced block.

I should implement a class-based approach or a functional approach. A class `TodoManager` might be cleaner for state management, but a simple script-driven menu is usually what's expected for "todo list manager" prompts unless specified otherwise. I'll go with a class based approach wrapped in a CLI loop.

Features:
-   `add(item)`: Add a task.
-   `remove(index_or_item)`: Remove a task.
-   `list_tasks()`: Display tasks.
-   Maybe a way to save/load? JSON is standard library. "Robust" suggests maybe handling persistence, but usually "robust" in this context just means error handling and good structure. I'll stick to in-memory for simplicity unless persistence makes it significantly better. I'll add basic file persistence using `json` to make it "robust" and actually useful.
-   Input validation (empty tasks, out of range indices).

Structure:
1.  `TodoManager` class.
2.  `_load` and `_save` methods for persistence (optional but good). Let's stick to in-memory to ensure it works without disk permissions issues unless requested, but "robust" often implies it survives a crash? No, let's just stick to a clean in-memory implementation with clear methods. Actually, file persistence is quite easy with `json`. I'll include it.
3.  Main loop for interaction.

Let's refine the "Robust" part.
-   Handle empty inputs.
-   Handle negative indices.
-   Handle non-integer inputs for removal.
-   Use `click`? No, standard lib only.
-   Use `argparse`? Maybe for a CLI tool.
-   Interactive menu is easier to demonstrate "add, remove, list".

I will create a class `TodoList` that manages the list.
Methods:
-   `add_task(description)`
-   `remove_task(task_id)`
-   `show_tasks()`

Then a `run_cli()` function.

Let's write the code.

```python
import json
import os
import uuid
from datetime import datetime

class TodoManager:
    def __init__(self, storage_file='todo_list.json'):
        self.storage_file = storage_file
        self.todos = []
        self._load()

    def _load(self):
        if os.path.exists(self.storage_file):
            try:
                with open(self.storage_file, 'r') as f:
                     self.todos = json.load(f)
            except (json.JSONDecodeError, IOError):
                self.todos = []
        else:
            self.todos = []

    def _save(self):
        try:
            with open(self.storage_file, 'w') as f:
                json.dump(self.todos, f, indent=4)
        except IOError:
            print("Warning: Could not save changes to file.")

    def add(self, description):
        if not description or not description.strip():
            print("Error: Task description cannot be empty.")
            return
        
        task = {
            "id": str(uuid.uuid4())[:8], # Short ID for display
            "description": description.strip(),
            "completed": False,
            "created_at": datetime.now().isoformat()
        }
        self.todos.append(task)
        self._save()
        print(f"Added: {task['description']}")

    def remove(self, task_id_or_index):
        if not self.todos:
            print("Todo list is empty.")
            return

        # Try to find by index first (if it's an integer)
        try:
            idx = int(task_id_or_index)
            if 1 <= idx <= len(self.todos):
                removed_task = self.todos.pop(idx - 1)
                self._save()
                print(f"Removed: {removed_task['description']}")
                return
            else:
                raise ValueError
        except ValueError:
            # Not an integer or out of range, try searching by content or ID
            # For this simple manager, let's assume input is index based for removal as it's most common in simple CLIs
            # Or maybe search by substring?
            # Let's stick to index-based removal for simplicity and robustness against ambiguity.
            # If it was not a valid index string, print error.
            pass
            
        print(f"Error: Invalid index '{task_id_or_index}'. Please enter a number