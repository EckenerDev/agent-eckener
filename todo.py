
<think>
The user wants a Python program for a Todo List Manager.
Requirements:
1.  Standard library only.
2.  Functions: `add`, `remove`, `list` (to display tasks).
3.  Clean, robust, self-contained.
4.  Single markdown code block.

Plan:
1.  Create a class `TodoList` to encapsulate state.
2.  Use a simple data structure (list of dictionaries or a list of strings) to store tasks. A list of dictionaries is better for extensibility (e.g., holding task ID, description, completion status).
3.  Implement `__init__` to initialize the task list.
4.  Implement `add_task(description)` to append a new task.
5.  Implement `remove_task(task_id)` to delete a task by its ID.
6.  Implement `list_tasks()` to display all current tasks.
7.  Add a simple CLI loop using `input()` to allow the user to interact with the manager.
8.  Handle basic error checking (e.g., invalid task ID, empty input).
9.  Add persistence? The prompt didn't explicitly ask for persistence (saving to file), but it's a nice touch for a "manager". However, to keep it strictly simple and robust within the constraints, I will implement an in-memory solution first, as it's the core requirement. I'll add a simple persistence mechanism using `json` (standard library) to make it a "complete" program as is standard for such exercises, ensuring data isn't lost on exit.

Refining the data model:
Task: `{ "id": int, "description": str, "completed": bool }`

Methods:
- `add(description)`: Generate new ID, append to list.
- `remove(task_id)`: Filter out task with matching ID.
- `list()`: Print formatted table/list of tasks.
- `toggle_complete(task_id)`: Useful feature to add for a "manager".

Structure of the code:
1.  Imports: `json`, `os`.
2.  Class `TodoApp`.
3.  File handling for persistence (load/save).
4.  Main loop handling user commands.

Let's stick to the specific requirement: "add, remove, and list functions". I will ensure these are clearly defined methods.

Drafting the code:
```python
import json
import os

class TodoManager:
    def __init__(self, filename="todos.json"):
        self.filename = filename
        self.tasks = []
        self._load()

    def _load(self):
        if os.path.exists(self.filename):
            try:
                with open(self.filename, 'r') as f:
                    self.tasks = json.load(f)
            except (json.JSONDecodeError, IOError):
                self.tasks = []
                
    def _save(self):
        with open(self.filename, 'w') as f:
            json.dump(self.tasks, f, indent=4)

    def add(self, description):
        if not description.strip():
            raise ValueError("Task description cannot be empty.")
        
        # Generate ID: max existing ID + 1 or 1 if empty
        if not self.tasks:
            new_id = 1
        else:
            new_id = max(t['id'] for t in self.tasks) + 1
            
        task = {
            "id": new_id,
            "description": description,
            "completed": False
        }
        self.tasks.append(task)
        self._save()
        return task

    def remove(self, task_id):
        original_len = len(self.tasks)
        self.tasks = [t for t in self.tasks if t['id'] != task_id]
        if len(self.tasks) < original_len:
            self._save()
            return True
        return False

    def list(self):
        # Return list of formatted task strings or just return the data?
        # The prompt implies a program, so printing is appropriate.
        if not self.tasks:
            print("No tasks currently.")
            return
        
        for t in self.tasks:
            status = "Done" if t['completed'] else "Pending"
            print(f"[{t['id']}] {t['description']} ({status})")

    # Helper for CLI
    def run_cli(self):
        print("Todo List Manager")
        print("Commands: add <description>, remove <id>, list, exit")
        
        while True:
            try:
                command = input("\n> ").strip().lower()
                if command == 'exit' or command == 'quit':
                    print("Goodbye!")
                    break
                elif command.startswith