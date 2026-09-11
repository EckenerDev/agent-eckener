
<think>
The user wants a Python program for a todo list manager.
The program should have `add`, `remove`, and `list` (or `show`) functions.
It should be self-contained, use no external dependencies, and be wrapped in a markdown Python block.

Key features to implement:
1.  Data structure to hold todo items (a list or dictionary). A list of dictionaries might be best to allow removing by ID or name, but a simple list of strings is often enough for a basic manager. Let's go with a list of dictionaries to support unique IDs, making removal safer.
2.  Functions:
    *   `add_task`: Takes a task description, assigns an ID, adds to the list.
    *   `remove_task`: Takes an ID (or index), removes the task.
    *   `list_tasks`: Prints the current list of tasks.
3.  Main loop/Interface: To make it a runnable program, it needs an interactive loop or a simple script execution. An interactive CLI is usually what is expected for a "manager".

Design decisions:
*   State management: Since this is a simple script, I can use a global list or encapsulate it in a class. A class `TodoListManager` is cleaner and more object-oriented.
*   Task representation: `{'id': 1, 'description': 'Buy milk', 'done': False}`. Actually, the prompt just says "todo list manager", keeping it simple is better. Maybe just `{'id': 1, 'description': '...'}`.
*   Input/Output: Standard `input()` and `print()`.

Let's refine the class structure:
`TodoApp`:
*   `__init__`: initializes an empty list `tasks = []` and a counter `next_id = 1`.
*   `add(description)`: adds to list, increments counter.
*   `remove(task_id)`: finds id and removes.
*   `list_tasks()`: prints formatted list.
*   `run()`: The CLI loop.

Error handling:
*   Invalid input for ID (not a number).
*   ID not found.
*   Empty description.

Code Structure:
```python
import sys

class TodoManager:
    def __init__(self):
        self.tasks = []
        self.next_id = 1

    def add(self, description):
        if not description.strip():
            print("Task description cannot be empty.")
            return
        task = {"id": self.next_id, "description": description}
        self.tasks.append(task)
        print(f"Added task #{self.next_id}: {description}")
        self.next_id += 1

    def remove(self, task_id):
        # Check if id exists
        task_index = None
        for i, task in enumerate(self.tasks):
            if task["id"] == task_id:
                task_index = i
                break
        
        if task_index is not None:
            removed_task = self.tasks.pop(task_index)
            print(f"Removed task: {removed_task['description']}")
        else:
            print(f"Task ID {task_id} not found.")

    def list_tasks(self):
        if not self.tasks:
            print("No tasks in the list.")
            return
        print("-" * 30)
        print(f"{'ID':<5} | Description")
        print("-" * 30)
        for task in self.tasks:
            print(f"{task['id']:<5} | {task['description']}")
        print("-" * 30)

    def run(self):
        print("Simple Todo List Manager")
        print("Commands: add <description>, remove <id>, list, quit")
        
        while True:
            try:
                command = input("\n> ").strip().lower()
                if not command:
                    continue
                
                parts = command.split(maxsplit=1)
                cmd = parts[0]
                
                if cmd == "add":
                    if len(parts) > 1:
                        self.add(parts[1])
                    else:
                        print("Usage: add <description>")
                elif cmd == "remove":
                    if len(parts) > 1:
                        try:
                            task_id = int(parts[1])
                            self.remove(task_id)
                        except ValueError:
                            print("ID must be a number.")
                    else:
                        print("Usage: remove <id>")
                elif cmd == "list":
                    self.list_tasks()
                elif cmd in ["quit", "exit", "q"]:
                    print("Goodbye!")
                    break
                else:
                    print(f"Unknown command: