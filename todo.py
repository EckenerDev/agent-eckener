import sys

class TodoManager:
    def __init__(self):
        self.tasks = []

    def add(self, task_text):
        self.tasks.append(task_text)
        print(f"Added: {task_text}")

    def remove(self, index):
        if 0 <= index < len(self.tasks):
            removed_task = self.tasks.pop(index)
            print(f"Removed: {removed_task}")
        else:
            print("Invalid index.")

    def list_tasks(self):
        if not self.tasks:
            print("No tasks found.")
        else:
            for i, task in enumerate(self.tasks):
                print(f"{i}. {task}")

def main():
    manager = TodoManager()
    # ... interaction loop

if __name__ == "__main__":
    main()
