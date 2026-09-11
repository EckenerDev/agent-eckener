import sys

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

def main():
    print("Simple Calculator")
    print("Operations: +, -, *, /")
    print("Type 'q' to quit.")
    
    operations = {
        '+': add,
        '-': subtract,
        '*': multiply,
        '/': divide
    }
    
    while True:
        try:
            user_input = input("\nEnter expression (e.g., 10 + 5): ").strip()
            
            if user_input.lower() == 'q':
                print("Exiting calculator.")
                break
            
            # Simple parsing logic
            # We expect format: number operator number
            # Split might be tricky if there are spaces or lack thereof. 
            # Better to use regex or a robust split logic? 
            # For a "simple" calculator, checking for operators in string is a start.
            
            parts = user_input.split()
            
            if len(parts) != 3:
                # Maybe the user didn't separate by spaces, e.g., "10+5"
                # Let's try to parse using regex for robustness? 
                # Or just try to locate the operator.
                pass 
                
        except Exception as e:
            print(f"Error: {e}")
