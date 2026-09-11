import sys

class TodoManager:
    def __init__(self):
        self.tasks = {} # id -> description
        self.next_id = 1

    def add_task(self, description):
        if not description.strip():
            print("Task description cannot be empty.")
            return False
        self.tasks[self.next_id] = description
        print(f"Added task {self.next_id}: {description}")
        self.next_id += 1
        return True

    def remove_task(self, task_id):
        if task_id in self.tasks:
            removed_task = self.tasks.pop(task_id)
            print(f"Removed task {task_id}: {removed_task}")
            return True
        else:
            print(f"Task with ID {task_id} not found.")
            return False

    def list_tasks(self):
        if not self.tasks:
            print("Your todo list is empty.")
            return
        print("\n--- Todo List ---")
        for tid, desc in self.tasks.items():
            print(f"[{tid}] {desc}")
        print("-----------------\n")

def main():
    manager = TodoManager()
    print("Welcome to the Todo List Manager!")
    print("Commands: add, remove, list, quit")
    
    while True:
        print("\n> ", end="")
        try:
            command = input().strip().lower()
        except (KeyboardInterrupt, EOFError):
            print("\nGoodbye!")
            break

        if command == 'quit' or command == 'exit':
            print("Goodbye!")
            break
        elif command == 'add':
            desc = input("Enter task description: ")
            manager.add_task(desc)
        elif command == 'remove':
            manager.list_tasks() # Show list so user knows IDs
            if not manager.tasks:
                print("Nothing to remove.")
                continue
            try:
                tid_input = input("Enter task ID to remove: ")
                tid = int(tid_input)
                manager.remove_task(tid)
            except ValueError:
                print("Invalid ID. Please enter a number.")
        elif command == 'list':
            manager.list_tasks()
        else:
            print("Unknown command. Use: add, remove, list, quit")

if __name__ == "__main__":
    main()
