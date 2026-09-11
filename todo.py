
<think>
The user wants a simple Python program that acts as a todo list manager.
It needs to support three main operations:
1.  **Add**: Add a new task.
2.  **Remove**: Remove a task (likely by index or ID).
3.  **List**: Show all current tasks.

Constraints:
-   Python 3.
-   No external dependencies (standard library only).
-   Self-contained.
-   Clean and robust code.
-   Wrapped in a markdown code block.

Plan:
1.  Create a class `TodoListManager` to encapsulate the logic.
2.  Use a list of dictionaries or a simple list of strings to store tasks. A list of dictionaries allows for more features like status (done/pending) and IDs, which makes it more "robust". Let's use a structure like `{'id': int, 'text': str, 'done': bool}`.
3.  Implement `add_task(description)`.
4.  Implement `remove_task(task_id)`.
5.  Implement `list_tasks()`.
6.  Implement a simple CLI (Command Line Interface) or a REPL (Read-Eval-Print Loop) so the user can actually interact with the program.
7.  Add error handling for invalid inputs.
8.  Add a `mark_done` feature? The prompt specifically asked for add, remove, and list. I'll stick to those to be concise, but maybe mark done is a nice touch for a "manager". I'll stick strictly to the prompt requirements first to ensure correctness, maybe adding a unique ID generation.

Refining the data structure:
-   A list of strings is simplest.
-   A list of dicts is better for removal (by ID) rather than by index (which shifts).
-   Let's use a list of strings for simplicity as it's a "simple" todo list, but implement removal by index for simplicity, or by text match. Actually, removing by index is standard for simple lists. However, removing by unique ID is more robust. Let's go with a list of strings for simplicity unless I decide to make it persistent.
-   Let's stick to a list of strings.
    -   `add`: append.
    -   `remove`: remove by index (e.g., "Remove task #2").
    -   `list`: print numbered list.

Let's make it slightly more robust than just a list of strings. A class `TodoList` is a good start.

Features:
-   `add(text)`: Validates non-empty text.
-   `remove(index)`: Validates index range.
-   `list()`: Prints formatted output.
-   `run()`: Loop to get user input.

Let's write the code structure.

```python
import sys

class TodoListManager:
    def __init__(self):
        self.tasks = []

    def add(self, description):
        if not description or not description.strip():
            print("Error: Task description cannot be empty.")
            return
        self.tasks.append(description.strip())
        print(f"Task added: '{description.strip()}'")

    def remove(self, index):
        try:
            index = int(index)
            # Handle 0-based or 1-based indexing? 1-based is more user-friendly.
            if 1 <= index <= len(self.tasks):
                removed_task = self.tasks.pop(index - 1)
                print(f"Task removed: '{removed_task}'")
            else:
                print(f"Error: Invalid task index. Please enter a number between 1 and {len(self.tasks)}.")
        except ValueError:
            print("Error: Index must be a valid number.")

    def list_tasks(self):
        if not self.tasks:
            print("Todo list is empty.")
        else:
            print("--- Todo List ---")
            for i, task in enumerate(self.tasks, start=1):
                print(f"{i}. {task}")
            print("-----------------")

    def run(self):
        print("Welcome to the Todo List Manager!")
        print("Commands: 'add <text>', 'remove <number>', 'list', 'quit'")
        
        while True:
            try:
                user_input = input("> ").strip()
                if not user_input:
                    continue
                
                parts = user_input.split(' ', 1) # Split into command and argument
                command = parts[0].lower()
                argument = parts[1] if len(parts) > 1 else ""

                if command == 'add':
                    if argument:
                        self.add(argument)
                    else:
                        print("Usage: add <task description>")
                elif command == 'remove':