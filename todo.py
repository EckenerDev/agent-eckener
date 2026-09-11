import sys

class TodoManager:
    def __init__(self):
        self.tasks = []

    def add(self, task):
        self.tasks.append(task)
        print(f"Added: {task}")

    def remove(self, task_id):
        try:
            index = int(task_id) - 1
            if 0 <= index < len(self.tasks):
                removed = self.tasks.pop(index)
                print(f"Removed: {removed}")
            else:
                print("Invalid task ID.")
        except ValueError:
            print("Please enter a valid number.")

    def list_tasks(self):
        if not self.tasks:
            print("No tasks found.")
        else:
            print("\n--- My Todo List ---")
            for i, task in enumerate(self.tasks, 1):
                print(f"{i}. {task}")
            print("-------------------\n")

def main():
    manager = TodoManager()
    # Loop for interaction
    ...
