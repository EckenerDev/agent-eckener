#!/usr/bin/env python3
"""
Todo List Manager
A simple, robust command-line interface for managing a todo list.
"""

class TodoList:
    def __init__(self):
        self.todos = {}
        self.next_id = 1

    def add(self, task: str) -> None:
        """Add a task to the list."""
        if not task or not task.strip():
            raise ValueError("Task description cannot be empty.")
        
        task_id = self.next_id
        self.todos[task_id] = task.strip()
        self.next_id += 1
        print(f"Added task #{task_id}: {self.todos[task_id]}")

    def remove(self, task_id: int) -> None:
        """Remove a task by its ID."""
        if task_id in self.todos:
            removed_task = self.todos.pop(task_id)
            print(f"Removed task #{task_id}: {removed_task}")
        else:
            print(f"Error: Task #{task_id} not found.")

    def list_tasks(self) -> None:
        """Display all tasks."""
        if not self.todos:
            print("The todo list is empty.")
            return
        
        print("--- Todo List ---")
        for task_id, task in self.todos.items():
            print(f"#{task_id}: {task}")
        print("-----------------")

def main():
    todo_list = TodoList()
    
    print("Welcome to the Todo List Manager!")
    print("Commands: add, remove, list, quit")
    
    while True:
        command = input("\nEnter command: ").strip().lower()
        
        if command == 'add':
            task = input("Enter task description: ")
            try:
                todo_list.add(task)
            except ValueError as e:
                print(f"Error: {e}")
                
        elif command == 'remove':
            try:
                task_id = int(input("Enter task ID to remove: "))
                todo_list.remove(task_id)
            except ValueError:
                print("Error: Invalid ID format. Please enter a number.")
                
        elif command == 'list':
            todo_list.list_tasks()
            
        elif command == 'quit' or command == 'exit':
            print("Goodbye!")
            break
        else:
            print("Unknown command. Please use 'add', 'remove', 'list', or 'quit'.")

if __name__ == "__main__":
    main()
