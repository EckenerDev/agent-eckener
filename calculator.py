   def add(a, b):
       return a + b

   def subtract(a, b):
       return a - b

   def multiply(a, b):
       return a * b

   def divide(a, b):
       if b == 0:
           raise ZeroDivisionError("Cannot divide by zero")
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
       print("Type 'quit' to exit.\n")

       while True:
           op = input("Enter operation (+, -, *, /) or 'quit': ").strip()
           if op.lower() == 'quit':
               print("Goodbye!")
               break

           if op not in ('+', '-', '*', '/'):
               print("Invalid operation. Please choose +, -, *, or /.\n")
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
               print(f"Result: {result}\n")
           except ZeroDivisionError:
               print("Error: Division by zero is not allowed.\n")

   if __name__ == "__main__":
       main()
   
