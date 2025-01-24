from .utils import generate_irreducible_fraction, fraction_to_latex, format_variable_expression, get_random_nonzero_integer, get_random_nonzero_integer_exclude_one
from fractions import Fraction
import random

def problem1():
    """문제 1 생성"""
    variables = ['a', 'x', 'y', 'z', 'b']
    variable = random.choice(variables)

    constant1 = get_random_nonzero_integer()
    constant2 = get_random_nonzero_integer()

    const1_str = "" if constant1 == 1 else "-" if constant1 == -1 else f"{constant1}"
    
    if constant1 > 0 and constant2 > 0:
        expression = f"{const1_str}{variable} × {constant2}"
    elif constant1 > 0 and constant2 < 0:
        expression = f"{const1_str}{variable} × ({constant2})"
    elif constant1 < 0 and constant2 > 0:
        expression = f"({const1_str}{variable}) × {constant2}"
    elif constant1 < 0 and constant2 < 0:
        expression = f"({const1_str}{variable}) × ({constant2})"

    result = constant1 * constant2
    result_str = f"{result}{variable}"
    step = f"{expression} = {result}{variable}"
    
    incorrect_result = result + random.choice([1, -1])
    incorrect_str = f"{incorrect_result}{variable}"

    return f'\\({expression}\\)', f'\\({result_str}\\)', f'\\({incorrect_str}\\)', f'\\({step}\\)'

def problem2():
    """문제 2 생성"""
    variables = ['a', 'x', 'y', 'z', 'b']
    variable = random.choice(variables)

    constant1 = random.randint(-10, 10)
    constant2 = random.randint(-10, 10)
    constant3 = random.randint(-10, 10)

    while constant1 == 0 or constant1 == constant3:
        constant1 = random.randint(-10, 10)
    while constant2 == 0 or constant2 == constant3:
        constant2 = random.randint(-10, 10)
    while constant3 == 0 or abs(constant3) == 1:
        constant3 = random.randint(-10, 10)

    expression_1 = f"({format_variable_expression(constant1, variable)} + {constant2})"
    expression_1 = expression_1.replace(" + -", " - ")
    expression = f"{expression_1} ÷ {abs(constant3)}"

    result_variable = Fraction(constant1, abs(constant3))
    result_constant = Fraction(constant2, abs(constant3))

    if result_variable.denominator == 1:
        variable_term = f"{result_variable.numerator}{variable}" if result_variable.numerator != 1 else f"{variable}"
    else:
        variable_term = f"{fraction_to_latex(result_variable)}{variable}"

    constant_term = fraction_to_latex(result_constant)
    final_answer = f"{variable_term} + {constant_term}".replace("+ -", "- ")

    step = f"{expression} = {expression_1} × {fraction_to_latex(Fraction(1, abs(constant3)))} = {final_answer}"

    incorrect_constant2 = constant2 + random.choice([1, -1])
    incorrect_result_constant = Fraction(incorrect_constant2, abs(constant3))

    incorrect_variable_term = f"{fraction_to_latex(result_variable)}{variable}" if result_variable.denominator != 1 else f"{result_variable.numerator}{variable}"
    incorrect_constant_term = fraction_to_latex(incorrect_result_constant)
    incorrect_answer = f"{incorrect_variable_term} + {incorrect_constant_term}".replace("+ -", "- ")

    return f'\\({expression}\\)', f'\\({final_answer}\\)', f'\\({incorrect_answer}\\)', f'\\({step}\\)'

def problem3():
    """문제 3 생성"""
    variables = ['a', 'x', 'y', 'z', 'b']
    variable = random.choice(variables)

    constant1 = get_random_nonzero_integer_exclude_one()
    constant2 = get_random_nonzero_integer_exclude_one()

    const1_str = format_variable_expression(constant1, variable)
    expression = f"{const1_str} ÷ {constant2}"

    if constant1 % constant2 == 0:
        result = constant1 // constant2
        result_str = f"{result}{variable}" if result != 1 else f"{variable}"
    else:
        result = Fraction(constant1, constant2)
        result_str = f"{fraction_to_latex(result)}{variable}"

    incorrect_result = result + random.choice([Fraction(1, 1), Fraction(-1, 1)])
    incorrect_str = f"{fraction_to_latex(incorrect_result)}{variable}" if incorrect_result.denominator != 1 else f"{incorrect_result.numerator}{variable}"

    fraction_part = fraction_to_latex(Fraction(1, abs(constant2)))
    if constant2 < 0:
        fraction_part = f"-{fraction_part}"
    step = f"{expression} = ({const1_str}) × ({fraction_part}) = {result_str}"

    return f'\\({expression}\\)', f'\\({result_str}\\)', f'\\({incorrect_str}\\)', f'\\({step}\\)'