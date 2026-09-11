import sys

class TodoManager:
    def __init__(self):
        self.todos = []

    def add(self, task):
        if not task or not task.strip():
            print("Error: Task cannot be empty.")
            return False
        self.todos.append({"id": len(self.todos) + 1, "task": task.strip()})
        print(f"Added: {task.strip()}")
        return True

    def remove(self, task_id):
        # Find index of the task with the given ID
        # IDs are 1-based
        try:
            index = task_id - 1
            if 0 <= index < len(self.todos):
                removed_task = self.todos.pop(index)
                print(f"Removed: {removed_task['task']}")
                self._reindex()
                return True
            else:
                print(f"Error: Task ID {task_id} does not exist.")
                return False
        except Exception as e:
            print(f"Error removing task: {e}")
            return False

    def list_items(self):
        if not self.todos:
            print("Your todo list is empty.")
        else:
            print("\n--- Todo List ---")
            for i, item in enumerate(self.todos, 1):
                print(f"[{i}] {item['task']}")
            print("-----------------\n")

    def _reindex(self):
        # Re-index tasks if we want IDs to be contiguous 1..N
        # Though strictly not necessary if we just store index, 
        # but for user friendliness, contiguous IDs are good.
        # Actually, pop(index) shifts elements, so if we access by 1-based index 
        # corresponding to list index, we don't need explicit reindexing logic 
        # inside the list structure if we just map input_id -> index.
        # Wait, if I pop index 0, item at index 1 becomes new index 0.
        # So if user asks to remove ID 1 (index 0), `pop(0)` works.
        # If user asks to remove ID 2 (index 1), `pop(1)` works.
        # The IDs displayed are just `enumerate(index, 1)`.
        # So explicit reindexing of stored data isn't needed if IDs are dynamic.
        pass

# Actually, let's keep it simple.
# Store just strings or dicts? Dicts allow more metadata later.
# Dynamic indexing (1-based) based on current list position is easiest.

    def remove_by_index(self, target_index):
        # target_index is 1-based
        index = target_index - 1
        if 0 <= index < len(self.todos):
            task = self.todos.pop(index)
            print(f"Removed: '{task}'")
        else:
            print(f"Error: Index {target_index} is out of range (1-{len(self.todos)}).")

def print_menu():
    print("\n1. Add Task")
    print("2. Remove Task")
    print("3. List Tasks")
    print("4. Exit")

def main():
    manager = TodoManager()
    
    while True:
        print_menu()
        try:
            choice = input("Enter choice (1-4): ").strip()
        except EOFError:
            print("\nExiting...")
            break
        except KeyboardInterrupt:
            print("\nExiting...")
            break

        if choice == '1':
            try:
                task = input("Enter task: ").strip()
                if not task:
                    print("Error: Task cannot be empty.")
                else:
                    manager.add(task)
            except Exception as e:
                print(f"Error: {e}")

        elif choice == '2':
            manager.list_items() # Show items first to know index
            try:
                idx_input = input("Enter task ID to remove: ").strip()
                if not idx_input.isdigit():
                    print("Error: Please enter a valid number.")
                else:
                    index = int(idx_input)
                    manager.remove_by_index(index)
            except Exception as e:
                print(f"Error: {e}")

        elif choice == '3':
            manager.list_items()

        elif choice == '4':
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Please enter a number between 1 and 4.")

if __name__ == "__main__":
    main()
