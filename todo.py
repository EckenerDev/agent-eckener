import sys

class TodoManager:
    def __init__(self):
        self.tasks = []

    def add(self, description):
        if not description or not description.strip():
            print("Error: Task description cannot be empty.")
            return
        self.tasks.append({"id": len(self.tasks) + 1, "description": description, "done": False})
        print(f"Task added: {desc}")

    def remove(self, task_id):
        # Find task by id to be safer, or remove by index? 
        # Let's remove by index provided by the user, but handle errors.
        try:
            index = int(task_id) - 1
            if 0 <= index < len(self.tasks):
                removed = self.tasks.pop(index)
                print(f"Removed task: {removed['description']}")
                # Re-index? Or just keep gaps? 
                # Keeping gaps in IDs is fine, but if we re-index, the list is more stable.
                # Let's just re-index the IDs to stay 1..N.
                for i, task in enumerate(self.tasks):
                    task['id'] = i + 1
            else:
                print("Error: Invalid task number.")
        except ValueError:
            print("Error: Task number must be an integer.")

    def list_tasks(self):
        if not self.tasks:
            print("Your todo list is empty.")
            return
        print("\n--- Todo List ---")
        for task in self.tasks:
            status = "Done" if task['done'] else "Pending"
            print(f"[{task['id']}] {task['description']} ({status})")
        print("-----------------")

def main():
    manager = TodoManager()
    while True:
        print("\nOptions: [add] / [remove] / [list] / [quit]")
        choice = input("Enter command: ").strip().lower()

        if choice == 'add':
            desc = input("Enter task description: ")
            manager.add(desc)
        elif choice == 'remove':
            task_num = input("Enter task number to remove: ")
            manager.remove(task_num)
        elif choice == 'list':
            manager.list_tasks()
        elif choice == 'quit':
            print("Goodbye!")
            break
        else:
            print("Unknown command.")

if __name__ == "__main__":
    main()
