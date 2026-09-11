import sys

def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    if n2 == 0:
        raise ZeroDivisionError("Cannot divide by zero")
    return n1 / n2

def get_float_input(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid input. Please enter a valid number.")

def get_operation():
    print("Select operation:")
    print("1. Add (+)")
    print("2. Subtract (-)")
    print("3. Multiply (*)")
    print("4. Divide (/)")
    
    choice = input("Enter choice (1/2/3/4): ")
    if choice in ['1', '2', '3', '4']:
        return choice
    else:
        return None

def main():
    print("Welcome to the Simple Calculator")
    
    while True:
        choice = get_operation()
        
        if choice is None:
            print("Invalid choice. Please try again.")
            continue
            
        # If valid choice, get numbers
        # However, to make the flow cleaner, maybe ask for numbers first or inside the specific blocks?
        # Standard flow: Op -> Num1 -> Num2 -> Result
        
        # Actually, get_operation is inside the loop, but getting numbers is better done conditionally or just straight after validation.
        # Let's restructure slightly for better UX.
        pass

# Revised Main Logic
def main():
    print("=== Simple Calculator ===")
    
    while True:
        print("\nSelect operation:")
        print("1. Add (+)")
        print("2. Subtract (-)")
        print("3. Multiply (*)")
        print("4. Divide (/)")
        print("0. Exit")
        
        user_choice = input("Enter choice (1/2/3/4/0): ").strip()
        
        if user_choice == '0':
            print("Goodbye!")
            break
            
        if user_choice not in ['1', '2', '3', '4']:
            print("Invalid selection. Please choose a valid option.")
            continue
            
        # Get numbers
        num1 = None
        num2 = None
        
        while num1 is None:
            try:
                num1 = float(input("Enter first number: "))
            except ValueError:
                print("Invalid input. Please enter a number.")
        
        while num2 is None:
            try:
                num2 = float(input("Enter second number: "))
            except ValueError:
                print("Invalid input. Please enter a number.")
                
        result = None
        operator_symbol = ""
        
        if user_choice == '1':
            result = add(num1, num2)
            operator_symbol = "+"
        elif user_choice == '2':
            result = subtract(num1, num2)
            operator_symbol = "-"
        elif user_choice == '3':
            result = multiply(num1, num2)
            operator_symbol = "*"
        elif user_choice == '4':
            try:
                result = divide(num1, num2)
                operator_symbol = "/"
            except ZeroDivisionError as e:
                print(f"Error: {e}")
                # Continue to next iteration without displaying result
                continue
        
        if result is not None:
            # Formatting output to remove unnecessary .0 for integers if desired, 
            # but float is fine for general calculator.
            print(f"Result: {num1} {operator_symbol} {num2} = {result}")

if __name__ == "__main__":
    main()
