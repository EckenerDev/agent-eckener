
<think>
The user wants a Python program that functions as a todo list manager.
It needs to have three main functions:
1. `add`: Add a new todo item.
2. `remove`: Remove an existing todo item.
3. `list`: List all current todo items.

Constraints:
- Senior Python programmer style (clean, robust, self-contained).
- Python 3.
- No external dependencies (standard library only).
- Output in a single markdown python fenced block.

Plan:
1.  Define a class or a module structure to hold the state. A class `TodoListManager` is good for encapsulation.
2.  Use a data structure like a list of dictionaries or a list of strings. To make it robust, maybe unique IDs or just strings. Let's stick to a simple list of strings for simplicity, or a list of dicts with `id`, `text`, and `completed` status to be more "senior" level. However, the prompt specifically asks for add, remove, and list.
3.  Implement the `add` method. It should take a string and append it. Handle duplicates? Maybe just append.
4.  Implement the `remove` method. It should take an identifier (index or text). Identifying by text is easier for a CLI script.
5.  Implement the `list_` (avoid keyword `list`) method. It should print the items.
6.  Add a simple Command Line Interface (CLI) loop to demonstrate it, as "Write a Python program" implies an executable script.
7.  Use `sys` for command line arguments or input.
8.  Add error handling (e.g., removing non-existent items).

Refining the design:
- Class `TodoApp`.
- Attribute `items`: List[str].
- Method `add_item(text)`.
- Method `remove_item(text)`.
- Method `list_items()`.
- A `run()` method or `if __name__ == "__main__":` block acting as the UI.

Let's make it slightly more robust by supporting indexing for removal, as text might be ambiguous.
Actually, the simplest robust interpretation:
- Add: `add("Buy milk")`
- List: Prints `1. Buy milk`
- Remove: `remove(1)` or `remove("Buy milk")`. Let's support removing by index for precision.

Let's write the code.

```python
import sys

class TodoList:
    def __init__(self):
        # Store tasks as a list of strings
        self.tasks = []

    def add(self, task: str) -> None:
        """Add a new task to the list."""
        if not task.strip():
            print("Error: Task cannot be empty.")
            return
        self.tasks.append(task.strip())
        print(f"Added: '{task.strip()}'")

    def remove(self, index: int) -> None:
        """Remove a task by its 1-based index."""
        if not self.tasks:
            print("The list is empty.")
            return
        
        # Adjust user's 1-based index to 0-based
        if 1 <= index <= len(self.tasks):
            removed_task = self.tasks.pop(index - 1)
            print(f"Removed: '{removed_task}'")
        else:
            print(f"Error: Index {index} is out of range.")

    def list_items(self) -> None:
        """Print all tasks."""
        if not self.tasks:
            print("Your todo list is empty.")
            return
        
        print("\n--- Todo List ---")
        for i, task in enumerate(self.tasks, 1):
            print(f"{i}. {task}")
        print("-----------------\n")

def main():
    todo_app = TodoList()
    
    print("Todo List Manager. Commands: add <text>, remove <index>, list, quit")
    
    while True:
        try:
            user_input = input("\nEnter command > ").strip()
            if not user_input:
                continue
            
            parts = user_input.split(maxsplit=1)
            command = parts[0].lower()
            argument = parts[1] if len(parts) > 1 else None

            if command == 'add':
                if argument:
                    todo_app.add(argument)
                else:
                    print("Error: Please provide a task description.")
            elif command == 'remove':
                if argument:
                    try:
                        index = int(argument)
                        todo_app.remove(index)
                    except ValueError:
                        print("Error: Please provide a valid number for the task index.")
                else:
                    print("Error: Please provide the index of the