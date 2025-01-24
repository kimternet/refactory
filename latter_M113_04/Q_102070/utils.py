import random
import math

def format_constant_term(constant):
    """Format constant terms for LaTeX representation."""
    if constant > 0:
        return f"+ {constant}"
    elif constant < 0:
        return f"- {abs(constant)}"
    else:
        return ""

def format_term(coefficient, variable):
    """Format variable terms for LaTeX representation."""
    if coefficient == 1:
        return f"{variable}"
    elif coefficient == -1:
        return f"-{variable}"
    else:
        return f"{coefficient}{variable}"

def gcd(x, y):
    """Calculate the greatest common divisor (GCD) of two numbers."""
    while y:
        x, y = y, x % y
    return x

def generate_irreducible_fraction(num, den):
    """Generate an irreducible fraction."""
    while num == den or gcd(num, den) != 1 or den == 1:
        num, den = random.randint(1, 10), random.randint(2, 10)
    return num, den

def ensure_divisible(c_den, d, e):
    """Ensure that the denominator cleanly divides the numerators."""
    d = c_den * random.randint(1, 10)
    e = c_den * random.randint(1, 10)
    return d, e

def clean_combined_expression(expression):
    """Clean up LaTeX expressions by removing redundant signs."""
    return expression.replace("+ -", "-")