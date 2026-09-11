def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        raise ZeroDivisionError("Cannot divide by zero.")
    return a / b

def main():
    print("Simple Calculator")
    print("Supported operations: add, subtract, multiply, divide")
    print("Type 'quit' to exit.\n")
    
    while True:
        try:
            user_input = input("Enter operation (add/subtract/multiply/divide): ").strip().lower()
            if user_input == 'quit':
                print("Exiting calculator. Goodbye!")
                break
                
            if user_input not in ('add', 'subtract', 'multiply', 'divide'):
                print("Invalid operation. Please try again.\n")
                continue
                
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
            
            if user_input == 'add':
                result = add(num1, num2)
            elif user_input == 'subtract':
                result = subtract(num1, num2)
            elif user_input == 'multiply':
                result = multiply(num1, num2)
            elif user_input == 'divide':
                result = divide(num1, num2)
                
            print(f"Result: {num1} {user_input} {num2} = {result}\n")
            
        except ValueError:
            print("Invalid input. Please enter numeric values.\n")
        except ZeroDivisionError as e:
            print(f"Error: {e}\n")
        except KeyboardInterrupt:
            print("\nExiting calculator. Goodbye!")
            break
        except Exception as e:
            print(f"An unexpected error occurred: {e}\n")

if __name__ == "__main__":
    main()
