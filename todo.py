import sys

class TodoManager:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)
        print(f"Added: {task}")

    def remove_task(self, index):
        try:
            # Convert 1-based input to 0-based index
            idx = int(index) - 1
            if 0 <= idx < len(self.tasks):
                removed = self.tasks.pop(idx)
                print(f"Removed: {removed}")
            else:
                print("Invalid task number.")
        except ValueError:
            print("Please enter a valid number.")

    def list_tasks(self):
        if not self.tasks:
            print("Your to-do list is empty.")
        else:
            print("\n--- To-Do List ---")
            for i, task in enumerate(self.tasks, start=1):
                print(f"{i}. {task}")
            print("------------------\n")

def main():
    manager = TodoManager()
    while True:
        print("\nOptions:")
        print("1. Add Task")
        print("2. Remove Task")
        print("3. List Tasks")
        print("4. Exit")
        
        choice = input("Enter choice: ").strip()
        
        if choice == '1':
            task = input("Enter task: ").strip()
            if task:
                manager.add_task(task)
            else:
                print("Task cannot be empty.")
        elif choice == '2':
            manager.list_tasks() # Show tasks so user knows what to remove
            idx = input("Enter task number to remove: ").strip()
            if idx:
                manager.remove_task(idx)
            else:
                print("Input cancelled.")
        elif choice == '3':
            manager.list_tasks()
        elif choice == '4':
            print("Exiting...")
            break
        else:
            print("Invalid option.")

if __name__ == "__main__":
    main()
