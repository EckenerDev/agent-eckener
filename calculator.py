def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        raise ValueError("Division by zero is not allowed.")
    return x / y

def main():
    print("Simple Calculator")
    print("Operations: +, -, *, /")
    print("Type 'quit' to exit.\n")
    
    while True:
        try:
            user_input = input("Enter expression (e.g., 5 + 3): ").strip()
            if user_input.lower() in ('quit', 'exit', 'q'):
                print("Exiting calculator. Goodbye!")
                break
            if not user_input:
                continue
                
            parts = user_input.split()
            if len(parts) != 3:
                print("Invalid format. Please use: number operator number (e.g., 10 / 2)\n")
                continue
                
            a_str, op, b_str = parts
            a = float(a_str)
            b = float(b_str)
            
            if op == '+':
                result = add(a, b)
            elif op == '-':
                result = subtract(a, b)
            elif op == '*':
                result = multiply(a, b)
            elif op == '/':
                result = divide(a, b)
            else:
                print(f"Unknown operator '{op}'. Please use +, -, *, or /\n")
                continue
                
            print(f"Result: {result}\n")
            
        except ValueError as e:
            if str(e) == "Division by zero is not allowed.":
                print("Error: Division by zero is not allowed.\n")
            else:
                print(f"Error: Invalid number format. Please enter valid numbers.\n")
        except Exception as e:
            print(f"An unexpected error occurred: {e}\n")

if __name__ == "__main__":
    main()
