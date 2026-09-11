def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        raise ZeroDivisionError("Cannot divide by zero")
    return x / y

def get_number(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid number. Please try again.")

def main():
    print("Simple Calculator")
    print("Select operation:")
    print("1. Add (+)")
    print("2. Subtract (-)")
    print("3. Multiply (*)")
    print("4. Divide (/)")
    print("5. Exit")

    while True:
        choice = input("\nEnter choice (1/2/3/4/5): ").strip()

        if choice == '5':
            print("Exiting calculator. Goodbye!")
            break
        elif choice in ('1', '2', '3', '4'):
            num1 = get_number("Enter first number: ")
            num2 = get_number("Enter second number: ")

            try:
                if choice == '1':
                    result = add(num1, num2)
                elif choice == '2':
                    result = subtract(num1, num2)
                elif choice == '3':
                    result = multiply(num1, num2)
                elif choice == '4':
                    result = divide(num1, num2)
                
                print(f"Result: {num1} {get_op_symbol(choice)} {num2} = {result}")
                
            except ZeroDivisionError:
                print("Error: Division by zero is not allowed.")
        else:
            print("Invalid input. Please select a valid option (1-5).")

def get_op_symbol(choice):
    symbols = {'1': '+', '2': '-', '3': '*', '4': '/'}
    return symbols.get(choice, '')

if __name__ == "__main__":
    main()
