import random
from fractions import Fraction

def get_random_nonzero_integer(low, high):
    value = random.randint(low, high)
    while value == 0:
        value = random.randint(low, high)
    return value

def get_random_variable():
    variables = ['a', 'x', 'y', 'z', 'b']
    return random.choice(variables)

def fraction_to_latex(fraction):
    numerator = abs(fraction.numerator)
    denominator = abs(fraction.denominator)
    if fraction < 0:
        if denominator == 1:
            return f"-{numerator}"
        else:
            return f"-\\frac{{{numerator}}}{{{denominator}}}"
    elif fraction.denominator == 1:
        return f"{fraction.numerator}"
    else:
        return f"\\frac{{{numerator}}}{{{denominator}}}"