
<think>
The user wants a Python program for a Todo List Manager.
The program needs to support three main operations:
1.  Add a task.
2.  Remove a task.
3.  List all tasks.

Constraints:
- Senior level Python 3 code.
- Clean, robust, self-contained.
- No external dependencies.
- Single markdown fenced block.

Design choices:
- Class-based structure: `TodoList` class to encapsulate logic.
- CLI interface: Simple `argparse` or `input()` loop based CLI. An interactive loop is usually friendlier for a simple CLI tool than a script that runs and exits unless arguments are provided. I'll go with a recursive or loop-based CLI.
- Data structure: A list of dictionaries or a list of strings? A list of dictionaries allows for metadata (like ID, status, creation time), which makes "removing" easier (by ID) and makes the code look more "senior".
- Robustness: Handle edge cases like empty lists, invalid inputs for removal, etc.

Implementation details:
- Class `TodoManager`:
    - `__init__`: Initialize storage. Maybe use a JSON file for persistence? The prompt didn't ask for persistence, just functions. A memory-only solution is sufficient based on the prompt, but adding file persistence is a nice touch for "robustness". However, keeping it simple and strictly adhering to "add, remove, list functions" might be safer. I'll stick to in-memory to avoid file I/O complexity unless explicitly requested, but I'll make the structure extensible. Actually, a robust CLI tool usually implies persistence. Let's stick to a simple in-memory list to ensure it runs out of the box without worrying about file permissions or paths, but I will structure it cleanly.
    - `add(item)`: Append to list.
    - `remove(index)`: Remove by item number.
    - `list_items()`: Print formatted list.
- Main loop:
    - Prompt user for command (a, r, l, q).
    - Execute corresponding method.

Refining "Remove":
- Users usually think "remove task 1". If the list is cleared and they remove 1, it's ambiguous. It's better to remove by index or ID. Since it's a simple list, removing by index (1-based) is intuitive for CLI.

Let's write the code.

Structure:
```python
import sys

class TodoList:
    def __init__(self):
        self.tasks = []
    
    def add(self, task_text):
        if not task_text.strip():
            print("Task description cannot be empty.")
            return
        # Maybe assign an auto-increment ID or just rely on index
        # Let's use a simple dict for potential extensibility, but keep it simple
        self.tasks.append({"id": len(self.tasks) + 1, "text": task_text, "completed": False})
        print(f"Added task: '{task_text}'")

    def remove(self, task_id):
        # Find task by ID
        task_to_remove = None
        for task in self.tasks:
            if task["id"] == task_id:
                task_to_remove = task
                break
        
        if task_to_remove:
            self.tasks.remove(task_to_remove)
            # Re-index? Or just keep IDs as they are? 
            # Re-indexing makes the display cleaner (1, 2, 3...)
            self._reindex()
            print(f"Removed task #{task_id}: '{task_to_remove['text']}'")
        else:
            print(f"Task #{task_id} not found.")

    def list_tasks(self):
        if not self.tasks:
            print("No tasks in the list.")
            return
        print("\n--- Todo List ---")
        for task in self.tasks:
            status = "[x]" if task["completed"] else "[ ]"
            print(f"#{task['id']:02d} {status} {task['text']}")
        print("-----------------\n")

    def _reindex(self):
        for i, task in enumerate(self.tasks):
            task["id"] = i + 1

class TodoCLI:
    def __init__(self):
        self.todo = TodoList()

    def run(self):
        print("Welcome to the Todo List Manager.")
        while True:
            print("\nCommands:")
            print("  'add <text>' - Add a new task")
            print("  'remove <id>' - Remove a task by ID")
            print("  'list'       - List all tasks")
            print("  'quit'       - Exit")
            
            try