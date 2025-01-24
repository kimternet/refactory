import random
from fractions import Fraction
from .utils import get_random_nonzero_integer, get_random_variable, fraction_to_latex

def generate_problem1():
    variable = get_random_variable()
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

    incorrect_result = result + random.choice([1, -1])
    incorrect_str = f"{incorrect_result}{variable}"

    return f'\\({expression}\\)', f'\\({result_str}\\)', f'\\({incorrect_str}\\)'

def generate_problem2():
    variable = get_random_variable()
    constant1 = get_random_nonzero_integer()
    constant2 = get_random_nonzero_integer()

    if constant1 == 1:
        const1_str = f"{variable}"
    elif constant1 == -1:
        const1_str = f"-{variable}"
    else:
        const1_str = f"{constant1}{variable}"

    if constant2 > 0 and constant1 > 0:
        expression = f" {const1_str} ÷ {constant2}"
    elif constant2 < 0 and constant1 > 0:
        expression = f"{const1_str} ÷ ({constant2})"
    elif constant2 > 0 and constant1 < 0:
        expression = f"({const1_str}) ÷ {constant2}"
    elif constant2 < 0 and constant1 < 0:
        expression = f"({const1_str}) ÷ ({constant2})"

    if constant1 % constant2 == 0:
        result = constant1 // constant2
        if result == 1:
            result_str = f"{variable}"
        elif result == -1:
            result_str = f"-{variable}"
        else:
            result_str = f"{result}{variable}"    
    else:
        result = Fraction(constant1, constant2).limit_denominator()
        result_str = f"{fraction_to_latex(result)}{variable}"

    incorrect_result = result + random.choice([Fraction(1, 1), Fraction(-1, 1)])
    while incorrect_result == result:
        incorrect_result = result + random.choice([Fraction(1, 1), Fraction(-1, 1)])
    incorrect_str = f"{fraction_to_latex(incorrect_result)}{variable}" if incorrect_result.denominator != 1 else f"{incorrect_result.numerator}{variable}"

    return f'\\({expression}\\)', f'\\({result_str}\\)', f'\\({incorrect_str}\\)'

def generate_problem3():
    variable = get_random_variable()
    constant1 = get_random_nonzero_integer()
    constant2 = get_random_nonzero_integer()
    constant3 = get_random_nonzero_integer()
    constant4 = get_random_nonzero_integer()

    f = Fraction(constant1, constant2)
    f2 = Fraction(constant3, constant4)

    while f.denominator == 1:
        constant1 = get_random_nonzero_integer()
        constant2 = get_random_nonzero_integer()
        f = Fraction(constant1, constant2)
    while f2.denominator == 1:
        constant3 = get_random_nonzero_integer()
        constant4 = get_random_nonzero_integer()
        f2 = Fraction(constant3, constant4)

    f_latex = f"({fraction_to_latex(f)})" if f < 0 else fraction_to_latex(f)
    operation = random.choice(["×", "÷"])

    if operation == "×":
        expression = f"{f_latex} × {fraction_to_latex(f2)}{variable}"
        result_fraction = f * f2
    else:
        expression = f"{f_latex} ÷ {fraction_to_latex(f2)}{variable}"
        result_fraction = f / f2

    if result_fraction.denominator == 1:
        coefficient = result_fraction.numerator
        if coefficient == 1:
            result_str = f"{variable}"
        elif coefficient == -1:
            result_str = f"-{variable}"
        else:
            result_str = f"{coefficient}{variable}"
    else:
        result_str = f"{fraction_to_latex(result_fraction)}{variable}"

    incorrect_fraction = result_fraction + random.choice([Fraction(1, 1), Fraction(-1, 1)])
    while incorrect_fraction == result_fraction or incorrect_fraction == 0:
        incorrect_fraction += random.choice([Fraction(1, 1), Fraction(-1, 1)])

    if incorrect_fraction.denominator == 1:
        coefficient = incorrect_fraction.numerator
        if coefficient == 1:
            incorrect_str = f"{variable}"
        elif coefficient == -1:
            incorrect_str = f"-{variable}"
        else:
            incorrect_str = f"{coefficient}{variable}"
    else:
        incorrect_str = f"{fraction_to_latex(incorrect_fraction)}{variable}"

    return f'\\({expression}\\)', f'\\({result_str}\\)', f'\\({incorrect_str}\\)'