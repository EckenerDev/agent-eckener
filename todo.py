import sys

class TodoList:
    def __init__(self):
        self.tasks = []

    def add(self, task: str):
        if not task.strip():
            print("Error: Task description cannot be empty.")
            return
        self.tasks.append({'id': len(self.tasks) + 1, 'task': task.strip(), 'completed': False})
        print(f"Added: '{task.strip()}'")

    def remove(self, task_index: int):
        if 1 <= task_index <= len(self.tasks):
            removed_task = self.tasks.pop(task_index - 1)
            # Re-indexing isn't strictly necessary for logic but nice for display
            for i, task in enumerate(self.tasks):
                task['id'] = i + 1
            print(f"Removed: '{removed_task['task']}'")
        else:
            print(f"Error: Invalid task index {task_index}. Available indices are 1-{len(self.tasks)}.")

    def list(self):
        if not self.tasks:
            print("Your todo list is empty.")
            return
        print(f"\n--- Todo List ({len(self.tasks)} items) ---")
        for task in self.tasks:
            status = "✓" if task['completed'] else "○"
            print(f"[{task['id']}] {status} {task['task']}")
        print("-" * 30)

def main():
    manager = TodoList()
    print("Welcome to the Todo List Manager!")
    print("Commands: 'add <task>', 'remove <id>', 'list', 'quit'")

    while True:
        try:
            command = input("\n> ").strip().lower()
        except (EOFError, KeyboardInterrupt):
            print("\nExiting...")
            break

        if not command:
            continue

        if command == 'quit' or command == 'exit':
            print("Goodbye!")
            break
        elif command == 'list':
            manager.list()
        elif command.startswith('add '):
            task = command[4:]
            manager.add(task)
        elif command.startswith('remove '):
            try:
                index = int(command[7:])
                manager.remove(index)
            except ValueError:
                print("Error: Please provide a valid integer ID to remove.")
        else:
            print("Unknown command. Try 'list', 'add <task>', 'remove <id>', or 'quit'.")

if __name__ == "__main__":
    main()
