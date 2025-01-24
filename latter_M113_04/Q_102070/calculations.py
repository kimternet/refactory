import random

from .utils import (
    format_constant_term, 
    format_term, 
    generate_irreducible_fraction, 
    ensure_divisible, 
    clean_combined_expression
)

def generate_problem():
    """Generate the main problem and solution."""
    # Randomly choose variables and constants
    c_numerator, c_denominator = generate_irreducible_fraction(random.randint(1, 10), random.randint(2, 10))
    f_numerator, f_denominator = generate_irreducible_fraction(random.randint(1, 10), random.randint(2, 10))
    while True:
        a, b = random.randint(2, 10), random.randint(1, 10)
        d, e = ensure_divisible(c_denominator, random.randint(1, 10), random.randint(1, 10))
        g, u = ensure_divisible(f_denominator, random.randint(1, 10), random.randint(1, 10))

        # Calculate terms for the problem
        c_term_x = c_numerator * d // c_denominator - a
        c_term_constant = c_numerator * e // c_denominator - b

        # Ensure non-zero terms for valid expressions
        if c_term_x != 0 and c_term_constant != 0:
            break

    return {
        "c_numerator": c_numerator,
        "c_denominator": c_denominator,
        "f_numerator": f_numerator,
        "f_denominator": f_denominator,
        "a": a,
        "b": b,
        "d": d,
        "e": e,
        "g": g,
        "u": u,
        "c_term_x": c_term_x,
        "c_term_constant": c_term_constant
    }