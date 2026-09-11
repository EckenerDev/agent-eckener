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

def calculate(num1, num2, operation):
    # map operations to functions
    ...

def main():
    # interactive loop
    ...

if __name__ == "__main__":
    main()
