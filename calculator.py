import sys

def add(a: float, b: float) -> float:
    return a + b

def subtract(a: float, b: float) -> float:
    return a - b

def multiply(a: float, b: float) -> float:
    return a * b

def divide(a: float, b: float) -> float:
    if b == 0:
        raise ZeroDivisionError("Cannot divide by zero")
    return a / b

def get_number(prompt: str) -> float:
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid input. Please enter a number.")

def main():
    operations = {
        'add': add,
        '+': add,
        'subtract': subtract,
        '-': subtract,
        'multiply': multiply,
        '*': multiply,
        'divide': divide,
        '/': divide
    }
    
    print("Simple Calculator")
    print("Operations: add, subtract, multiply, divide")
    print("Type 'quit' to exit.")
    
    while True:
        op = input("\nEnter operation (or 'quit'): ").strip().lower()
        if op == 'quit':
            print("Goodbye!")
            break
        if op not in operations:
            print("Invalid operation.")
            continue
            
        num1 = get_number("Enter first number: ")
        num2 = get_number("Enter second number: ")
        
        try:
            result = operations[op](num1, num2)
            print(f"Result: {result}")
        except ZeroDivisionError as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    main()
