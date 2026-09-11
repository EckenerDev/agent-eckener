   def add(a, b):
       return a + b

   def subtract(a, b):
       return a - b

   def multiply(a, b):
       return a * b

   def divide(a, b):
       if b == 0:
           raise ValueError("Cannot divide by zero")
       return a / b

   def main():
       print("Simple Calculator")
       print("Operations: +, -, *, /")
       print("Enter 'q' to quit")

       while True:
           operation = input("Enter operation (+, -, *, /): ").strip().lower()
           if operation == 'q' or operation == 'quit':
               print("Goodbye!")
               break

           if operation not in ('+', '-', '*', '/'):
               print("Invalid operation. Please try again.")
               continue

           try:
               num1 = float(input("Enter first number: "))
               num2 = float(input("Enter second number: "))
           except ValueError:
               print("Invalid number input. Please enter valid numbers.")
               continue

           try:
               if operation == '+':
                   result = add(num1, num2)
               elif operation == '-':
                   result = subtract(num1, num2)
               elif operation == '*':
                   result = multiply(num1, num2)
               elif operation == '/':
                   result = divide(num1, num2)
               print(f"Result: {result}")
           except ValueError as e:
               print(f"Error: {e}")

   if __name__ == "__main__":
       main()
   
