import sys

class TodoListManager:
    def __init__(self):
        self.tasks = []

    def add(self, task):
        self.tasks.append(task)
        print(f"Added: '{task}'")

    def remove(self, task_index):
        try:
            # User inputs usually 1-based, convert to 0-based
            idx = int(task_index) - 1
            if 0 <= idx < len(self.tasks):
                removed_task = self.tasks.pop(idx)
                print(f"Removed: '{removed_task}'")
            else:
                print("Invalid task number.")
        except ValueError:
            print("Please enter a valid number.")

    def list_tasks(self):
        if not self.tasks:
            print("No tasks in the list.")
            return
        for i, task in enumerate(self.tasks, 1):
            print(f"{i}. {task}")

def main():
    manager = TodoListManager()
    while True:
        print("\n--- Todo List Manager ---")
        print("1. Add task")
        print("2. Remove task")
        print("3. List tasks")
        print("4. Exit")
        
        choice = input("Enter your choice: ").strip()
        
        if choice == '1':
            task = input("Enter task description: ")
            if task:
                manager.add(task)
            else:
                print("Task description cannot be empty.")
        elif choice == '2':
            manager.list_tasks() # Show list so user knows what to remove
            idx = input("Enter task number to remove: ").strip()
            manager.remove(idx)
        elif choice == '3':
            manager.list_tasks()
        elif choice == '4':
            print("Goodbye!")
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()
