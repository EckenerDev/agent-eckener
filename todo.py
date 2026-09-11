import sys

class TodoManager:
    def __init__(self):
        self.todos = []

    def add(self, description):
        if not description.strip():
            print("Error: Todo description cannot be empty.")
            return False
        self.todos.append(description.strip())
        print(f"Added: {description}")
        return True

    def remove(self, index):
        # Indexes are usually 1-based in user interfaces
        if not 0 < index <= len(self.todos):
            print(f"Error: Invalid index {index}. Range is 1-{len(self.todos)}.")
            return False
        
        removed_item = self.todos.pop(index - 1)
        print(f"Removed: {removed_item}")
        return True

    def list_todos(self):
        if not self.todos:
            print("The todo list is empty.")
            return
        
        print("\n--- Todo List ---")
        for i, todo in enumerate(self.todos, 1):
            print(f"{i}. {todo}")
        print("-----------------\n")

def main():
    manager = TodoManager()
    
    print("Welcome to Todo Manager.")
    print("Commands: add, remove, list, quit\n")
    
    while True:
        try:
            user_input = input("Enter command (add/remove/list/quit): ").strip().lower()
            
            if user_input == 'quit' or user_input == 'exit' or user_input == 'q':
                print("Goodbye!")
                break
            
            if user_input == 'add':
                description = input("Enter item to add: ").strip()
                manager.add(description)
            
            elif user_input == 'remove':
                manager.list_todos()
                if manager.todos:
                    try:
                        idx_str = input("Enter the number of the item to remove: ").strip()
                        if not idx_str.isdigit():
                            print("Error: Please enter a valid number.")
                        else:
                            idx = int(idx_str)
                            manager.remove(idx)
                    except ValueError:
                        print("Error: Invalid input.")
            
            elif user_input == 'list':
                manager.list_todos()
            
            else:
                print("Unknown command. Please use add, remove, list, or quit.")
        
        except KeyboardInterrupt:
            print("\nOperation cancelled by user. Exiting.")
            sys.exit(0)
        except EOFError:
            print("\nExited.")
            sys.exit(0)

if __name__ == "__main__":
    main()
