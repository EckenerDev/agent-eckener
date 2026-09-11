import sys

class TodoList:
    def __init__(self):
        self.tasks = []

    def add(self, description):
        if not description.strip():
            print("Task description cannot be empty.")
            return False
        self.tasks.append(description.strip())
        print(f"Added task: '{description.strip()}'")
        return True

    def remove(self, index):
        try:
            idx = int(index)
            if 0 <= idx < len(self.tasks):
                removed_task = self.tasks.pop(idx)
                print(f"Removed task: '{removed_task}'")
            else:
                print(f"Index {idx} is out of range.")
        except ValueError:
            print("Invalid index. Please enter a number.")

    def show(self):
        if not self.tasks:
            print("Todo list is empty.")
            return
        print("\n--- Todo List ---")
        for i, task in enumerate(self.tasks):
            print(f"[{i}] {task}")
        print("-----------------\n")

def main():
    todo = TodoList()
    while True:
        print("\nCommands: 'add <task>', 'remove <index>', 'list', 'quit'")
        user_input = input("> ").strip()
        
        if not user_input:
            continue
            
        parts = user_input.split(' ', 1) # Split into command and rest
        command = parts[0].lower()
        argument = parts[1] if len(parts) > 1 else ""

        if command == 'add':
            if argument:
                todo.add(argument)
            else:
                print("Usage: add <task description>")
        elif command == 'remove' or command == 'delete':
            if argument:
                todo.remove(argument)
            else:
                print("Usage: remove <task index>")
        elif command == 'list' or command == 'show' or command == 'l':
            todo.show()
        elif command == 'quit' or command == 'exit' or command == 'q':
            print("Goodbye!")
            break
        else:
            print("Unknown command.")

if __name__ == "__main__":
    main()
