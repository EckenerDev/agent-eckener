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
        return "Error: Division by zero"
    return x / y

def main():
    print("Simple Calculator")
    print("Operations:")
    print("1. Add (+)")
    print("2. Subtract (-)")
    print("3. Multiply (*)")
    print("4. Divide (/)")

    while True:
        print("\nSelect operation (1-4) or 'q' to quit:")
        choice = input("> ")

        if choice.lower() == 'q':
            print("Goodbye!")
            break
        
        if choice not in ['1', '2', '3', '4']:
            print("Invalid choice. Please select 1-4.")
            continue

        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue

        result = 0
        
        if choice == '1':
            result = add(num1, num2)
        elif choice == '2':
            result = subtract(num1, num2)
        elif choice == '3':
            result = multiply(num1, num2)
        elif choice == '4':
            result = divide(num1, num2)
            
        print(f"Result: {result}")

if __name__ == "__main__":
    main()
