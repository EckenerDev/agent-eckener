import json
import os

class TodoList:
    def __init__(self):
        self.tasks = []
        self.next_id = 1

    def add(self, title):
        task = {'id': self.next_id, 'title': title, 'done': False}
        self.tasks.append(task)
        self.next_id += 1
        return task

    def remove(self, task_id):
        for task in self.tasks:
            if task['id'] == task_id:
                self.tasks.remove(task)
                return True
        return False

    def list(self):
        for task in self.tasks:
            print(f"[{task['id']}] {task['title']} ({'Done' if task['done'] else 'Pending'})")

# CLI Logic
def main():
    todo = TodoList()
    while True:
    # ... commands ...
