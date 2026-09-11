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

def get_number(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid input. Please enter a valid number.")

def main():
    print("Simple Calculator")
    print("Operations: +, -, *, /")
    print("Type 'q' to quit.")
    
    while True:
        op = input("Enter operation (+, -, *, /) or 'q' to quit: ").strip().lower()
        if op == 'q':
            print("Exiting calculator. Goodbye!")
            break
        if op not in ('+', '-', '*', '/'):
            print("Invalid operation. Please enter +, -, *, or /.")
            continue
            
        num1 = get_number("Enter first number: ")
        num2 = get_number("Enter second number: ")
        
        try:
            if op == '+':
                result = add(num1, num2)
            elif op == '-':
                result = subtract(num1, num2)
            elif op == '*':
                result = multiply(num1, num2)
            elif op == '/':
                result = divide(num1, num2)
                
            print(f"Result: {num1} {op} {num2} = {result}")
        except ZeroDivisionError as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    main()
