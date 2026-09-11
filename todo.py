import sys

class TodoManager:
    def __init__(self):
        self.todos = []

    def add(self, text):
        if not text.strip():
            print("Error: Task description cannot be empty.")
            return
        self.todos.append(text.strip())
        print(f"Added: {text.strip()}")

    def remove(self, task_id):
        try:
            # User likely provides 1-based index
            idx = int(task_id) - 1
            if 0 <= idx < len(self.todos):
                removed_task = self.todos.pop(idx)
                print(f"Removed: {removed_task}")
            else:
                print(f"Error: Invalid task ID '{task_id}'.")
        except ValueError:
            print("Error: Task ID must be a number.")

    def list_items(self):
        if not self.todos:
            print("Todo list is empty.")
            return
        
        print(f"\n--- Todo List ({len(self.todos)} items) ---")
        for i, task in enumerate(self.todos, 1):
            print(f"{i}. {task}")
        print("------------------------------\n")

def main():
    manager = TodoManager()
    print("Welcome to Todo List Manager!")
    print("Commands: add <task>, remove <id>, list, quit")
    
    while True:
        try:
            command = input(">> ").strip().lower()
            if not command:
                continue
            
            parts = command.split(maxsplit=1)
            action = parts[0]
            args = parts[1] if len(parts) > 1 else ""

            if action == 'add':
                manager.add(args)
            elif action == 'remove':
                manager.remove(args)
            elif action == 'list':
                manager.list_items()
            elif action in ['quit', 'exit', 'q']:
                print("Goodbye!")
                break
            else:
                print("Unknown command. Use 'add', 'remove', 'list', or 'quit'.")
        except KeyboardInterrupt:
            print("\nExiting...")
            break
        except Exception as e:
            print(f"Unexpected error: {e}")

if __name__ == "__main__":
    main()
