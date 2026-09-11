import sys

def add(x, y):
    """Return the sum of x and y."""
    return x + y

def subtract(x, y):
    """Return the difference of x and y."""
    return x - y

def multiply(x, y):
    """Return the product of x and y."""
    return x * y

def divide(x, y):
    """Return the division of x by y."""
    if y == 0:
        raise ValueError("Cannot divide by zero")
    return x / y

def get_number(prompt):
    """Helper to get a number from user input, handling errors."""
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid input. Please enter a valid number.")

def main():
    print("===== Simple Calculator =====")
    print("Supported operations: +, -, *, /")
    
    while True:
        # Get first number
        try:
            num1 = get_number("Enter first number (or 'q' to quit): ")
        except EOFError:
            break
        
        if isinstance(num1, str) and num1.lower() == 'q':
            # Handle the case where get_number might return a string if logic changes, 
            # but currently get_number forces float. 
            # Let's adjust logic to handle quit before parsing or check string.
            # Actually, simpler to just check input directly in main loop or modify get_number.
            # Let's stick to a standard loop.
            pass 

        # Redoing the flow to handle 'q' cleanly.
        pass

    # Let's refactor the main loop structure for clarity.
    
    while True:
        print("\n--- Options: + (add), - (subtract), * (multiply), / (divide), q (quit) ---")
        user_input_operation = input("Enter operation: ").strip().lower()
        
        if user_input_operation == 'q':
            print("Exiting calculator. Goodbye!")
            break
            
        if user_input_operation not in ['+', '-', '*', '/']:
            print("Invalid operation. Please try again.")
            continue
            
        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
        except ValueError:
            print("Invalid number format. Please try again.")
            continue
            
        try:
            result = None
            if user_input_operation == '+':
                result = add(num1, num2)
            elif user_input_operation == '-':
                result = subtract(num1, num2)
            elif user_input_operation == '*':
                result = multiply(num1, num2)
            elif user_input_operation == '/':
                result = divide(num1, num2)
            
            # Formatting output to remove trailing zeros for cleaner look, or just print raw.
            # Raw float is usually fine, but maybe format.
            if isinstance(result, float):
                # Check if it's an integer value
                if result.is_integer():
                    print(f"Result: {int(result)}")
                else:
                    print(f"Result: {result}")
            else:
                print(f"Result: {result}")
                
        except ValueError as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    main()
