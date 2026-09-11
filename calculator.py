import sys

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Error: Division by zero"
    return x / y

def calculator():
    print("Simple Calculator")
    print("Select operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Exit")

    while True:
        choice = input("Enter choice (1/2/3/4/5): ")

        if choice == '5':
            print("Exiting calculator. Goodbye!")
            break

        if choice not in ['1', '2', '3', '4']:
            print("Invalid input. Please enter a number between 1 and 5.")
            continue

        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
        except ValueError:
            print("Invalid input. Please enter numeric values.")
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

        # Check if result is a string (error message) or number
        if isinstance(result, str):
            print(f"Result: {result}")
        else:
            print(f"Result: {num1} {get_op_name(choice)} {num2} = {result}")

def get_op_name(choice):
    ops = {
        '1': '+',
        '2': '-',
        '3': '*',
        '4': '/'
    }
    return ops.get(choice, '?')

if __name__ == "__main__":
    calculator()
