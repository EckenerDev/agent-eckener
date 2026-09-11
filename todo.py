
<think>
The user wants a Python program to manage a todo list.
The requirements are:
1.  Add a task.
2.  Remove a task.
3.  List tasks.
4.  No external dependencies (standard library only).
5.  Single python block.
6.  Clean, robust, self-contained code.

Design considerations:
-   **GUI vs CLI**: Usually, a CLI is preferred for simple text-based tasks unless specified otherwise. However, a simple GUI using `tkinter` (standard library) is also an option and often more user-friendly for "managers". Given the prompt is generic, a CLI is the safest bet for a "program", but a `tkinter` app feels more like a "manager". Let's stick to a robust CLI with a persistent storage (JSON) to make it useful, or just an in-memory solution if it's meant to be a simple script.
    -   *Decision*: I will build a CLI application that uses `json` to persist data to a file, as that makes it a robust "manager" rather than just a temporary script. It adds value without external dependencies.
-   **Data Structure**: A list of dictionaries or strings. List of dictionaries allows for more metadata (completed status, timestamps), which is good practice.
-   **Storage**: A JSON file (`todo.json`).
-   **Functions**:
    -   `load_todos()`: Load from file.
    -   `save_todos()`: Save to file.
    -   `add_todo(task)`: Add to list.
    -   `remove_todo(task_index)`: Remove by index.
    -   `list_todos()`: Print formatted list.
    -   `main()`: Interactive loop.

Let's refine the "Robust" part:
-   Handle file not found (first run).
-   Handle invalid inputs (non-existent index).
-   Use `argparse` for command-line arguments? Or just an interactive prompt?
    -   *Decision*: An interactive prompt is easier to demonstrate the `add/remove/list` functions clearly in a single run. However, using `argparse` is more "programmatic". The prompt asks for "functions", implying a usage like `todo add ...`.
    -   Let's provide a CLI tool that accepts commands like `python todo.py add "Buy milk"`, `python todo.py list`, `python todo.py remove 1`. This is more professional.

Plan:
1.  Import `json`, `os`, `argparse`, `sys`.
2.  Define a data file path (in the same directory or a standard config folder). Let's stick to a local file `todo.json`.
3.  Implement helper functions for data persistence.
4.  Implement `add`, `remove`, `list` logic.
5.  Set up `argparse` to handle subcommands.

Wait, if the user just wants a script that runs and manages a list, an interactive menu is also very standard for "Write a program that satisfies...".
Let's look at the phrasing: "A todo list manager with add, remove, and list **functions**".
This implies the code should expose these behaviors.
I will write a script that supports both an interactive mode and a command-line mode, or just a clean command-line interface.
Actually, a simple interactive loop is often less confusing for a general request than `subparsers` in argparse, but `argparse` is the standard way to write CLI tools in Python.
Let's go with `argparse` as it's robust and standard.

Data structure:
`[ {"id": 1, "text": "Buy milk", "done": False}, ... ]`

Features:
-   `add`: Takes a string. Appends to list. Saves.
-   `remove`: Takes an ID. Removes item. Saves.
-   `list`: Prints items.

Let's add a `complete` function? The prompt didn't ask for it, just add, remove, list. I'll stick to the scope but maybe mark removal as the only deletion method.

Code Structure:
```python
import json
import os
import sys
import argparse

TODO_FILE = "todo_list.json"

def load_todos():
    """Load todos from JSON file."""
    if not os.path.exists(TODO_FILE):
        return []
    try:
        with open(TODO_FILE, 'r') as f:
            return json.load(f)
    except (json.JSONDecodeError, IOError):
        return []

def save_todos(todos):
    """Save todos to JSON file."""
    with open(TODO_FILE, 'w') as f:
        json.dump(todos, f, indent=4)

