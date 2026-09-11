import sys

def add(x: float, y: float) -> float:
    return x + y

def subtract(x: float, y: float) -> float:
    return x - y

def multiply(x: float, y: float) -> float:
    return x * y

def divide(x: float, y: float) -> float:
    if y == 0:
        raise ZeroDivisionError("Cannot divide by zero.")
    return x / y

OPERATIONS = {
    '+': add,
    'add': add,
    '-': subtract,
    'subtract': subtract,
    '*': multiply,
    'multiply': multiply,
    '/': divide,
    'divide': divide,
    'x': multiply,
    '×': multiply,
}

def get_number(prompt: str) -> float:
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid input. Please enter a number.")

def get_operation() -> str:
    valid = list(OPERATIONS.keys())
    print(f"Available operations: {', '.join(valid)}")
    choice = input("Enter operation: ").strip().lower()
    if choice in OPERATIONS:
        return choice
    print("Invalid operation. Please try again.")
    return get_operation()

def main():
    print("=== Simple Calculator ===")
    print("Type 'quit' at any time to exit.\n")
    
    while True:
        try:
            num1 = get_number("Enter first number (or 'quit'): ")
            if num1 == num1: # Hack for quit check isn't needed if we check input string first, but let's handle quit properly.
                pass
        except (ValueError, TypeError):
            break 

Wait, `get_number` returns a float, so checking for 'quit' inside it is better.
Let's adjust `get_number` to accept 'quit'.

Actually, simpler: handle 'quit' inside the `get_number` function by checking the input string before conversion.
