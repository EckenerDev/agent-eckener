import sys

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero.")
    return a / b

def get_number(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid input. Please enter a valid number.")

def display_result(result):
    # Display as integer if it's a whole number, otherwise float
    if result.is_integer():
        print(f"Result: {int(result)}")
    else:
        print(f"Result: {result}")

def main():
    print("Simple Calculator")
    print("Operations: +, -, *, /")
    print("Type 'quit' to exit.\n")
    
    while True:
        try:
            num1 = get_number("Enter first number: ")
            
            while True:
                op = input("Enter operation (+, -, *, /): ").strip()
                if op in ("+", "-", "*", "/"):
                    break
                print("Invalid operation. Please enter +, -, *, or /.")
                
            num2 = get_number("Enter second number: ")
            
            operations = {
                "+": add,
                "-": subtract,
                "*": multiply,
                "/": divide
            }
            
            try:
                result = operations[op](num1, num2)
                display_result(result)
            except ValueError as e:
                print(f"Error: {e}")
                
        except KeyboardInterrupt:
            print("\nExiting calculator. Goodbye!")
            sys.exit(0)
        except EOFError:
            print("\nExiting calculator. Goodbye!")
            sys.exit(0)

if __name__ == "__main__":
    main()
