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

def main():
    print("Simple Calculator")
    print("Select operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")

    while True:
        choice = input("\nEnter choice (1/2/3/4) or 'q' to quit: ")

        if choice.lower() == 'q':
            print("Exiting calculator.")
            break

        if choice not in ['1', '2', '3', '4']:
            print("Invalid input. Please select a valid option.")
            continue

        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
        except ValueError:
            print("Invalid number format. Please enter numeric values.")
            continue

        if choice == '1':
            result = add(num1, num2)
        elif choice == '2':
            result = subtract(num1, num2)
        elif choice == '3':
            result = multiply(num1, num2)
        elif choice == '4':
            result = divide(num1, num2)

        if isinstance(result, str):
            # Handle the error message from divide function
            print(f"Result: {result}")
        else:
            print(f"{num1} {get_operator_symbol(choice)} {num2} = {result}")

def get_operator_symbol(choice):
    symbols = {
        '1': '+',
        '2': '-',
        '3': '*',
        '4': '/'
    }
    return symbols[choice]

if __name__ == "__main__":
    main()
