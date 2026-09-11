import sys

class TodoListManager:
    def __init__(self):
        self.tasks = []

    def add(self, task):
        if not task.strip():
            print("Task cannot be empty.")
            return False
        self.tasks.append(task)
        print(f"Added: '{task}'")
        return True

    def remove(self, index):
        try:
            idx = int(index)
            if 0 <= idx < len(self.tasks):
                removed_task = self.tasks.pop(idx)
                print(f"Removed: '{removed_task}'")
                return True
            else:
                print(f"Error: Index {index} is out of range.")
                return False
        except ValueError:
            print("Error: Invalid index. Please enter a number.")
            return False

    def list_tasks(self):
        if not self.tasks:
            print("No tasks found.")
            return
        print("\n--- To-Do List ---")
        for i, task in enumerate(self.tasks):
            print(f"{i}. {task}")
        print("------------------")

    def run(self):
        print("Welcome to the Todo List Manager!")
        while True:
            print("\nOptions:")
            print("1. Add a task")
            print("2. Remove a task")
            print("3. List tasks")
            print("0. Exit")
            
            choice = input("\nEnter your choice: ").strip()
            
            if choice == '1':
                task = input("Enter task description: ")
                self.add(task)
            elif choice == '2':
                self.list_tasks()
                if self.tasks:
                    index = input("Enter the number of the task to remove: ")
                    self.remove(index)
            elif choice == '3':
                self.list_tasks()
            elif choice == '0':
                print("Exiting...")
                break
            else:
                print("Invalid choice. Please try again.")

if __name__ == "__main__":
    manager = TodoListManager()
    manager.run()
