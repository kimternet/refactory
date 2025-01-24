from .utils import (
    get_random_nonzero_integer,
    fraction_to_latex
)
from fractions import Fraction

def generate_problem1(variable):
    constant1 = get_random_nonzero_integer(-10, 10)
    constant2 = get_random_nonzero_integer(-10, 10)
    constant3 = get_random_nonzero_integer(-10, 10)

    const1_str = "" if constant1 == 1 else "-" if constant1 == -1 else f"{constant1}"
    const2_str = "" if constant2 == 1 else "-" if constant2 == -1 else f"{constant2}"

    if constant1 > 0 and constant3 > 0:
        expression = f"{const1_str}({const2_str}{variable} + {constant3})"
        result_numeric = f"{constant1 * constant2}{variable} + {constant1 * constant3}"
    elif constant1 > 0 and constant3 < 0:
        expression = f"{const1_str}({const2_str}{variable} - {abs(constant3)})"
        result_numeric = f"{constant1 * constant2}{variable} - {abs(constant1 * constant3)}"
    elif constant1 < 0 and constant3 < 0:
        expression = f"{const1_str}({const2_str}{variable} + {constant3})"
        result_numeric = f"{constant1 * constant2}{variable} + {constant1 * constant3}"
    elif constant1 < 0 and constant3 > 0:
        expression = f"{const1_str}({const2_str}{variable} - {abs(constant3)})"
        result_numeric = f"{constant1 * constant2}{variable} - {abs(constant1 * constant3)}"

    return expression, result_numeric

def generate_problem2(variable):
    constant1 = get_random_nonzero_integer(-10, 10)
    constant2 = get_random_nonzero_integer(-10, 10)
    fraction = Fraction(get_random_nonzero_integer(-10, 10), get_random_nonzero_integer(-10, 10))

    const1_str = "" if constant1 == 1 else "-" if constant1 == -1 else f"{constant1}"

    if constant2 > 0:
        expression = f"({const1_str}{variable} + {constant2}) × {fraction_to_latex(fraction)}"
    else:
        expression = f"({const1_str}{variable} - {abs(constant2)}) × {fraction_to_latex(fraction)}"

    coeff1 = Fraction(constant1 * fraction.numerator, fraction.denominator)
    coeff2 = Fraction(constant2 * fraction.numerator, fraction.denominator)

    coeff1_str = "" if coeff1 == 1 else "-" if coeff1 == -1 else f"{fraction_to_latex(coeff1)}"
    if coeff2 > 0:
        result_numeric = f"{coeff1_str}{variable} + {fraction_to_latex(coeff2)}"
    else:
        result_numeric = f"{coeff1_str}{variable} - {fraction_to_latex(abs(coeff2))}"

    return expression, result_numeric

def generate_problem3(variable):
    fraction = Fraction(get_random_nonzero_integer(-10, 10), get_random_nonzero_integer(-10, 10))
    constant2 = get_random_nonzero_integer(-10, 10)

    const2_str = f"+ {constant2}" if constant2 > 0 else f"- {abs(constant2)}"
    expression = f"{fraction_to_latex(fraction)}({variable} {const2_str})"

    coeff1 = fraction
    coeff2 = Fraction(constant2 * fraction.numerator, fraction.denominator)

    coeff1_str = "" if coeff1 == 1 else "-" if coeff1 == -1 else f"{fraction_to_latex(coeff1)}"
    if coeff2 > 0:
        result_numeric = f"{coeff1_str}{variable} + {fraction_to_latex(coeff2)}"
    else:
        result_numeric = f"{coeff1_str}{variable} - {fraction_to_latex(abs(coeff2))}"

    return expression, result_numeric