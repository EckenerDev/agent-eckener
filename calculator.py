
<think>
The user wants a simple Python calculator program.
It needs to support the following operations:
- Add
- Subtract
- Multiply
- Divide

Constraints:
- Python 3.
- Standard library only.
- Single markdown block.
- Clean, robust code.

Plan:
1.  Create a class `Calculator` to encapsulate the logic.
2.  Implement methods for each operation: `add`, `subtract`, `multiply`, `divide`.
3.  Handle division by zero.
4.  Create a simple user interface (CLI) to demonstrate usage.
5.  Include a main block to run the demo.

Implementation details:
- `add(a, b)`: returns `a + b`.
- `subtract(a, b)`: returns `a - b`.
- `multiply(a, b)`: returns `a * b`.
- `divide(a, b)`: checks if `b == 0`, raises an error or returns an error message.
- CLI: Loop asking for input until a specific command (like 'quit') is entered.

Let's refine the CLI part to be user-friendly.
Prompt: "Enter operation (+, -, *, /) or 'quit'"
Prompt: "Enter number 1"
Prompt: "Enter number 2"

Robustness checks:
- Input validation for numbers.
- Input validation for operation.

Let's write the code.

```python
import sys

class Calculator:
    """A simple calculator class with basic arithmetic operations."""

    @staticmethod
    def add(a: float, b: float) -> float:
        """Returns the sum of a and b."""
        return a + b

    @staticmethod
    def subtract(a: float, b: float) -> float:
        """Returns the difference of a and b."""
        return a - b

    @staticmethod
    def multiply(a: float, b: float) -> float:
        """Returns the product of a and b."""
        return a * b

    @staticmethod
    def divide(a: float, b: float) -> float:
        """Returns the quotient of a and b."""
        if b == 0:
            raise ZeroDivisionError("Cannot divide by zero.")
        return a / b

    def perform_operation(self, operator: str, a: float, b: float) -> float:
        """
        Performs the specified operation on a and b.
        Raises ValueError if operator is invalid.
        Raises ZeroDivisionError if dividing by zero.
        """
        operations = {
            '+': self.add,
            '-': self.subtract,
            '*': self.multiply,
            '/': self.divide
        }

        if operator not in operations:
            raise ValueError(f"Invalid operator: {operator}. Use +, -, *, or /.")

        return operations[operator](a, b)


def get_number(prompt: str) -> float:
    """Helper function to get a float from user input."""
    while True:
        try:
            # Check for EOF or interrupt
            val = input(prompt)
            if val.lower() == 'q':
                sys.exit(0)
            return float(val)
        except ValueError:
            print("Invalid input. Please enter a number.")
        except (EOFError, KeyboardInterrupt):
            print("\nExiting program.")
            sys.exit(0)


def main():
    """Main function to run the calculator interactive loop."""
    print("Simple Calculator")
    print("----------------")
    print("Supported operations: +, -, *, /")
    print("Type 'q' at any point to quit.")
    print()

    calc = Calculator()

    while True:
        try:
            # Get inputs
            print("Calculating...")
            a = get_number("Enter first number: ")
            op = input("Enter operator (+, -, *, /): ").strip()
            b = get_number("Enter second number: ")

            # Handle quit check for operator input
            if op.lower() == 'q':
                print("Exiting...")
                break

            # Perform calculation
            try:
                result = calc.perform_operation(op, a, b)
                # Format result to remove trailing zeros for clean display if it's an integer
                if result.is_integer():
                    result = int(result)
                print(f"Result: {result}")
            except ZeroDivisionError as e:
                print(f"Error: {e}")
            except ValueError as e:
                print(f"Error: {e}")

            print()

        except (EOFError, KeyboardInterrupt):
            print("\nExiting program.")
            break

if __name__ == "__main