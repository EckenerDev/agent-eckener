import json
import os
from datetime import datetime

class TodoManager:
    def __init__(self, filename='todo.json'):
        self.filename = filename
        self.tasks = self._load_tasks()

    def _load_tasks(self):
        if os.path.exists(self.filename):
            try:
                with open(self.filename, 'r') as f:
                    return json.load(f)
            except json.JSONDecodeError:
                return []
        return []

    def _save_tasks(self):
        with open(self.filename, 'w') as f:
            json.dump(self.tasks, f, indent=4)

    def add(self, description):
        new_task = {
            'id': len(self.tasks) + 1,
            'description': description,
            'status': 'pending',
            'created_at': datetime.now().isoformat()
        }
        self.tasks.append(new_task)
        self._save_tasks()
        print(f"Task added: {description}")

    def remove(self, task_id):
        task_id = int(task_id)
        for i, task in enumerate(self.tasks):
            if task['id'] == task_id:
                removed_task = self.tasks.pop(i)
                self._save_tasks()
                print(f"Task removed: {removed_task['description']}")
                return
        print(f"Task with ID {task_id} not found.")

    def list(self):
        if not self.tasks:
            print("Your todo list is empty.")
            return
        print("Current Tasks:")
        for task in self.tasks:
            status_icon = "✓" if task['status'] == 'completed' else "○"
            print(f"[{task['id']}] {status_icon} {task['description']}")
