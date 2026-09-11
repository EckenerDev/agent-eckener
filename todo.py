import sys

class TodoManager:
    def __init__(self):
        self.todos = []

    def add(self, task):
        if not task or not task.strip():
            print("Error: Task description cannot be empty.")
            return
        self.todos.append(task.strip())
        print(f"Task added: '{task.strip()}'")

    def remove(self, index):
        if is_empty(self.todos):
            print("List is empty.")
            return
        
        # Convert index to int
        try:
            idx = int(index)
        except ValueError:
            print("Error: Invalid index. Please enter a number.")
            return

        if idx < 0 or idx >= len(self.todos):
            print(f"Error: Index {idx} is out of range. Valid range: 0-{len(self.todos)-1}.")
            return
        
        removed_task = self.todos.pop(idx)
        print(f"Task removed: '{removed_task}'")

    def list(self):
        if not self.todos:
            print("No tasks in the list.")
            return
        
        print("\n--- Todo List ---")
        for i, task in enumerate(self.todos):
            print(f"{i}: {task}")
        print("-----------------\n")

def run_cli():
    manager = TodoManager()
    
    print("Welcome to Todo Manager!")
    print("Commands: 'add', 'remove', 'list', 'quit'")

    while True:
        try:
            command = input("\n> ").strip().lower()
        except (EOFError, KeyboardInterrupt):
            print("\nExiting...")
            break

        if command == 'quit' or command == 'exit' or command == 'q':
            print("Goodbye!")
            break
        elif command == 'add':
            task = input("Enter task description: ")
            manager.add(task)
        elif command == 'remove':
            manager.list() # Show list so user knows indices
            if not manager.todos:
                continue
            index_input = input("Enter index of task to remove: ")
            manager.remove(index_input)
        elif command == 'list':
            manager.list()
        else:
            if command != '':
                print(f"Unknown command: '{command}'. Available: add, remove, list, quit.")

if __name__ == "__main__":
    run_cli()
