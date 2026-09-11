
<think>
The user wants a simple calculator program in Python with add, subtract, multiply, and divide functions. I need to write clean, robust, self-contained Python 3 code with no external dependencies, wrapped in a single markdown python fenced block.

Key requirements:
1. Functions: add, subtract, multiply, divide
2. Simple calculator program
3. Python 3, standard library only
4. Clean and robust

I'll create:
- Four arithmetic functions
- A simple CLI interface (could be command-line arguments, interactive prompt, or both)
- Input validation and error handling (especially for division by zero)
- Clean structure

Let me write a robust program that can be used either interactively or via command line. I'll include:
- Proper error handling for division by zero
- Input validation
- Clear functions
- A simple REPL-like interface or command-line interface

I'll go with a command-line interface using argparse for robustness, plus an interactive mode option. Actually, to keep it simple but robust, I'll use a simple interactive prompt with proper validation and error handling.

Let me structure it:
1. Define add, subtract, multiply, divide functions
2. A calculator class or just functions
3. Main loop with input parsing
4. Error handling

I'll make it clean and professional.
</think>

```python
import sys
import argparse


def add(a: float, b: float) -> float:
    """Add two numbers and return the result."""
    return a + b


def subtract(a: float, b: float) -> float:
    """Subtract b from a and return the result."""
    return a - b


def multiply(a: float, b: float) -> float:
    """Multiply two numbers and return the result."""
    return a * b


def divide(a: float, b: float) -> float:
    """Divide a by b and return the result.
    
    Raises:
        ZeroDivisionError: If b is zero.
    """
    if b == 0:
        raise ZeroDivisionError("Cannot divide by zero")
    return a / b


def parse_expression(expression: str) -> tuple[str, float, float]:
    """Parse a simple arithmetic expression like '3 + 4' or '10 - 2'.
    
    Args:
        expression: String containing two numbers and an operator.
        
    Returns:
        Tuple of (operator_symbol, operand_a, operand_b).
        
    Raises:
        ValueError: If the expression cannot be parsed.
    """
    supported_ops = {"+", "-", "*", "/"}
    
    # Try each operator
    for op in supported_ops:
        if op in expression:
            try:
                parts = expression.split(op)
                if len(parts) != 2:
                    continue
                a = float(parts[0].strip())
                b = float(parts[1].strip())
                return op, a, b
            except (ValueError, IndexError):
                continue
    
    raise ValueError(
        "Invalid expression. Expected format: '<number> <operator> <number>'\n"
        "Supported operators: +, -, *, /\n"
        "Example: 10 + 5"
    )


def evaluate(op: str, a: float, b: float) -> float:
    """Evaluate an arithmetic operation.
    
    Args:
        op: Operator symbol (+, -, *, /).
        a: First operand.
        b: Second operand.
        
    Returns:
        Result of the operation.
        
    Raises:
        ValueError: If the operator is not supported.
        ZeroDivisionError: If dividing by zero.
    """
    operations = {
        "+": add,
        "-": subtract,
        "*": multiply,
        "/": divide,
    }
    
    if op not in operations:
        raise ValueError(f"Unsupported operator: '{op}'. Supported: {', '.join(operations.keys())}")
    
    return operations[op](a, b)


def format_result(number: float) -> str:
    """Format a float result, removing unnecessary decimal places when possible.
    
    Args:
        number: The number to format.
        
    Returns:
        Formatted string representation.
    """
    if number == int(number):
        return str(int(number))
    return f"{number:.10f}".rstrip("0").rstrip(".")


def run_interactive() -> None:
    """Run the calculator in interactive REPL mode."""
    print("=" * 40)
    print("  Simple Calculator")
    print("=" * 40)
    print("Supported operators: +, -, *, /")
