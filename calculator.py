   def add(a: float, b: float) -> float:
       return a + b

   def subtract(a: float, b: float) -> float:
       return a - b

   def multiply(a: float, b: float) -> float:
       return a * b

   def divide(a: float, b: float) -> float:
       if b == 0:
           raise ZeroDivisionError("Cannot divide by zero.")
       return a / b

   def main():
       print("Simple Calculator")
       print("Operations: +, -, *, /")
       print("Type 'q' to quit")

       while True:
           expr = input("\nEnter an expression (e.g., 3.5 + 2): ").strip()
           if expr.lower() == 'q':
               print("Goodbye!")
               break

           try:
               parts = expr.split()
               if len(parts) != 3:
                   print("Invalid format. Use: number operator number")
                   continue

               a, op, b = parts
               num_a = float(a)
               num_b = float(b)

               if op == '+':
                   result = add(num_a, num_b)
               elif op == '-':
                   result = subtract(num_a, num_b)
               elif op == '*':
                   result = multiply(num_a, num_b)
               elif op == '/':
                   result = divide(num_a, num_b)
               else:
                   print("Unsupported operator. Use +, -, *, or /")
                   continue

               print(f"Result: {result}")

           except ValueError:
               print("Invalid input. Please enter valid numbers.")
           except ZeroDivisionError as e:
               print(f"Error: {e}")
           except Exception as e:
               print(f"Unexpected error: {e}")

   if __name__ == "__main__":
       main()
   
