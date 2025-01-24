import random
from fractions import Fraction

def fraction_to_latex(fraction):
    numerator = abs(fraction.numerator)
    denominator = abs(fraction.denominator)
    if fraction < 0:
        return f"-\\frac{{{numerator}}}{{{denominator}}}"
    elif fraction.denominator == 1:
        return f"{fraction.numerator}"
    else:
        return f"\\frac{{{numerator}}}{{{denominator}}}"

def get_random_variable():
    variables = ['a', 'x', 'y', 'z']
    return random.choice(variables)

def get_nonzero_random_int(min_val=-10, max_val=10):
    constant = random.randint(min_val, max_val)
    while constant == 0:
        constant = random.randint(min_val, max_val)
    return constant