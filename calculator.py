def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        raise ValueError("Cannot divide by zero.")
    return x / y

def main():
    print("Simple Calculator")
    print("Operations: +, -, *, /")
    print("Type 'quit' to exit.")
    
    while True:
        try:
            input_str = input("\nInput (e.g., 5 + 3 or 'quit'): ").strip()
            if input_str.lower() in ['quit', 'q']:
                print("Exiting calculator.")
                break
            
            parts = input_str.split()
            if len(parts) != 3:
                print("Invalid format. Please use format: number operator number")
                continue
            
            try:
                num1 = float(parts[0])
                num2 = float(parts[2])
            except ValueError:
                print("Invalid numbers. Please enter numeric values.")
                continue
            
            op = parts[1]
            
            if op == '+':
                result = add(num1, num2)
            elif op == '-':
                result = subtract(num1, num2)
            elif op == '*':
                result = multiply(num1, num2)
            elif op == '/':
                result = divide(num1, num2)
            else:
                print("Invalid operator. Use +, -, *, or /.")
                continue
                
            print(f"Result: {result}")
            
        except ValueError as e:
            if "Cannot divide by zero" in str(e):
                print("Error: Cannot divide by zero.")
            else:
                print(f"Error: {e}")
        except KeyboardInterrupt:
            print("\nExiting calculator.")
            break

if __name__ == "__main__":
    main()
