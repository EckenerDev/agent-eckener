
<think>
The user wants a Python program that acts as a todo list manager.
Key features required:
1.  Add a todo.
2.  Remove a todo.
3.  List todos.

Constraint:
- Python 3.
- Standard library only.
- Single markdown block.
- Clean, robust, self-contained.

Design:
- I should probably use a simple data structure like a list or dictionary.
- A dictionary might be better to store metadata like IDs or completion status, but the prompt specifically asked for add, remove, and list. I'll keep it simple but structured.
- A CLI interface is appropriate for a "program".
- I will implement a simple loop to allow the user to interact with the program.

Implementation details:
- Use a list to store todos.
- `add( description )`
- `remove( index )` or `remove( id )`
- `list_todos()`

Let's refine the data structure.
Maybe a class `TodoManager` to encapsulate the logic.

Attributes:
- `_todos`: a list of dictionaries `{'id': 1, 'text': 'Buy milk', 'done': False}` or just strings. The prompt is simple ("add, remove, list"), so maybe just strings is sufficient, but IDs make removal safer (indices shift). Let's use a list of strings for simplicity, or a list of dicts for robustness. Given "robust" in instructions, I'll use a list of dicts with an auto-incrementing ID.

Wait, if I want to be strictly "robust" and self-contained, I should handle inputs, empty lists, invalid inputs, etc.

Functions requested:
- `add`
- `remove`
- `list` (this is a keyword, so I'll name it `list_todos` or `show`).

Let's draft the code.

```python
import sys

class TodoListManager:
    def __init__(self):
        self.todos = []
        self.current_id = 1

    def add(self, text):
        if not text.strip():
            print("Error: Todo text cannot be empty.")
            return None
        
        todo = {
            "id": self.current_id,
            "text": text,
            "is_completed": False
        }
        self.todos.append(todo)
        self.current_id += 1
        print(f"Added todo #{self.current_id - 1}: '{text}'")
        return todo

    def remove(self, todo_id):
        # Find index
        index_to_remove = None
        for i, todo in enumerate(self.todos):
            if todo["id"] == todo_id:
                index_to_remove = i
                break
        
        if index_to_remove is not None:
            removed = self.todos.pop(index_to_remove)
            print(f"Removed todo #{removed['id']}: '{removed['text']}'")
        else:
            print(f"Error: Todo ID {todo_id} not found.")

    def list_todos(self):
        if not self.todos:
            print("Todo list is empty.")
            return

        print("\n--- Todo List ---")
        for todo in self.todos:
            status = "[X]" if todo["is_completed"] else "[ ]"
            print(f"#{todo['id']}: {status} {todo['text']}")
        print("-----------------\n")

def main():
    manager = TodoListManager()
    
    print("Welcome to Todo List Manager")
    print("Commands: 'add <text>', 'remove <id>', 'list', 'quit'")

    while True:
        try:
            command = input("\n> ").strip()
            if not command:
                continue
            
            parts = command.split(maxsplit=1)
            action = parts[0].lower()
            args = parts[1] if len(parts) > 1 else None

            if action == 'add':
                if args:
                    manager.add(args)
                else:
                    print("Usage: add <text>")
            elif action == 'remove':
                if args:
                    try:
                        todo_id = int(args)
                        manager.remove(todo_id)
                    except ValueError:
                        print("Usage: remove <id> (number)")
                else:
                    print("Usage: remove <id>")
            elif action == 'list':
                manager.list_todos()
            elif action in ('quit', 'exit'):
                print("Goodbye!")
                break
            else:
                print("Unknown command. Try 'add', 'remove', 'list', or 'quit'.")
        except (EOFError, KeyboardInterrupt):
            print("\