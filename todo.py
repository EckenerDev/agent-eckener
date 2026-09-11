import sys

class TodoManager:
    def __init__(self):
        self.tasks = []

    def add_task(self, description):
        if description:
            self.tasks.append(description)
            print(f"Task added: {description}")
        else:
            print("Task description cannot be empty.")

    def list_tasks(self):
        if not self.tasks:
            print("Todo list is empty.")
            return
        print("\nYour Todo List:")
        for index, task in enumerate(self.tasks, 1):
            print(f"{index}. {task}")

    def remove_task(self, task_index):
        try:
            # Convert input to int, check if it's a valid index (1-based)
            idx = int(task_index)
            if 1 <= idx <= len(self.tasks):
                removed_task = self.tasks.pop(idx - 1)
                print(f"Task removed: {removed_task}")
            else:
                print(f"Invalid task number. Please choose a number between 1 and {len(self.tasks)}.")
        except ValueError:
            print("Please enter a valid number.")

def main():
    manager = TodoManager()
    print("Welcome to the Todo List Manager!")
    
    while True:
        print("\nOptions:")
        print("1. Add Task")
        print("2. Remove Task")
        print("3. List Tasks")
        print("4. Exit")
        
        choice = input("Enter your choice (1-4): ").strip()
        
        if choice == '1':
            task_desc = input("Enter task description: ").strip()
            manager.add_task(task_desc)
        elif choice == '2':
            manager.list_tasks() # Show list so user knows indices
            if manager.tasks:
                task_num = input("Enter task number to remove: ").strip()
                manager.remove_task(task_num)
        elif choice == '3':
            manager.list_tasks()
        elif choice == '4':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
