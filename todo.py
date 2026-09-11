class TodoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        if not task.strip():
            print("Task cannot be empty.")
            return
        self.tasks.append(task)
        print(f"Task added: '{task}'")

    def remove_task(self, index):
        # Adjust for 1-based indexing
        idx = int(index) - 1
        if 0 <= idx < len(self.tasks):
            removed = self.tasks.pop(idx)
            print(f"Removed: '{removed}'")
        else:
            print("Invalid task number.")

    def list_tasks(self):
        if not self.tasks:
            print("No tasks.")
        else:
            for i, task in enumerate(self.tasks, start=1):
                print(f"{i}. {task}")
