import json
import os

class TodoManager:
    def __init__(self, filename="todos.json"):
        self.filename = filename
        self.todos = self._load()
    
    def _load(self):
        if os.path.exists(self.filename):
            with open(self.filename, 'r') as f:
                return json.load(f)
        return []
    
    def _save(self):
        with open(self.filename, 'w') as f:
            json.dump(self.todos, f)

    def add(self, task):
        self.todos.append({"task": task, "done": False})
        self._save()
        
    def remove(self, index):
        try:
            idx = int(index)
            if 0 <= idx < len(self.todos):
                del self.todos[idx]
                self._save()
                print(f"Removed task: {index}")
            else:
                print("Invalid index.")
        except ValueError:
            print("Index must be a number.")

    def list_tasks(self):
        if not self.todos:
            print("No tasks in list.")
            return
        for i, item in enumerate(self.todos):
            status = " [x]" if item["done"] else " [ ]"
            print(f"{i}. {item['task']}{status}")

def main():
    manager = TodoManager()
    while True:
        print("\n--- Todo List Manager ---")
        print("Commands: add, remove, list, quit")
        cmd = input("Enter command: ").strip().lower()
        
        if cmd == "add":
            task = input("Enter task to add: ")
            manager.add(task)
            print("Task added.")
        elif cmd == "remove":
            manager.list_tasks()
            idx = input("Enter index to remove: ")
            manager.remove(idx)
        elif cmd == "list":
            manager.list_tasks()
        elif cmd == "quit":
            break
        else:
            print("Unknown command.")

if __name__ == "__main__":
    main()
