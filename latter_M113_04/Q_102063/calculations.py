from .utils import get_random_nonzero_integer, fraction_to_latex, get_random_variable
from fractions import Fraction
from sympy import symbols, Rational, nsimplify

def generate_problem1(variable):
    """문제 1 생성"""
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

def generate_problem5():
    """문제 5 생성"""
    variable = get_random_variable()
    x = symbols(variable)

    a = get_random_nonzero_integer(1, 10)
    b = get_random_nonzero_integer(-10, 10)
    denominator = get_random_nonzero_integer(2, 12)
    multiplier = get_random_nonzero_integer(2, 10)

    expression = ((a * x + b) / denominator) * multiplier
    simplified_expression = nsimplify(expression, rational=True)

    result_x_term = Rational(a * multiplier, denominator)
    result_constant_term = Rational(b * multiplier, denominator)

    expression_str = f"\\frac{{{a}{variable} {b:+}}}{{{denominator}}} \\times {multiplier}"
    result = f"{fraction_to_latex(result_x_term)}{variable} {'+' if result_constant_term >= 0 else ''}{fraction_to_latex(result_constant_term)}"
    
    step1 = f"\\frac{{{a}{variable} {b:+}}}{{{denominator}}} \\times {multiplier} = ({a}{variable} {b:+}) \\times \\frac{{{multiplier}}}{{{denominator}}}"
    step2 = f"= {fraction_to_latex(result_x_term)}{variable} {'+' if result_constant_term >= 0 else ''}{fraction_to_latex(result_constant_term)}"
    calculation = f"{step1} \\ {step2}"

    return expression_str, result, calculation