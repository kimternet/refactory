from fractions import Fraction
import random
from .utils import fraction_to_latex

def generate_problem1(constant1, constant2, variable):
    if constant1 == 1:
        const1_str = f"{variable}"
    elif constant1 == -1:
        const1_str = f"-{variable}"
    else:
        const1_str = f"{constant1}{variable}"

    if constant2 > 0 and constant1 > 0:
        expression = f"{const1_str} × {constant2}"
    elif constant2 < 0 and constant1 > 0:
        expression = f"{const1_str} × ({constant2})"
    elif constant2 > 0 and constant1 < 0:
        expression = f"{constant2} × ({const1_str})"
    elif constant2 < 0 and constant1 < 0:
        expression = f"({const1_str}) × ({constant2})"

    result = constant1 * constant2
    if result == 1:
        result_str = f"{variable}"
    elif result == -1:
        result_str = f"-{variable}"
    else:
        result_str = f"{result}{variable}"

    incorrect_result = result + random.choice([1, -1])
    while incorrect_result == result:
        incorrect_result = result + random.choice([1, -1])
    incorrect_str = f"{incorrect_result}{variable}"

    return f'\\({expression}\\)', f'\\({result_str}\\)', f'\\({incorrect_str}\\)'

def generate_problem2(constant1, constant2, variable):
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

def generate_problem3(constant1, constant2, variable):
    constant3 = random.randint(-10, 10)
    constant4 = random.randint(-10, 10)
    while constant3 == 0:
        constant3 = random.randint(-10, 10)
    while constant4 == 0:
        constant4 = random.randint(-10, 10)

    f = Fraction(constant1, constant2).limit_denominator()
    f2 = Fraction(constant3, constant4).limit_denominator()

    while f.denominator == 1:
        f = Fraction(random.randint(-10, 10), random.randint(-10, 10)).limit_denominator()
    while f2.denominator == 1:
        f2 = Fraction(random.randint(-10, 10), random.randint(-10, 10)).limit_denominator()

    f_latex = f"({fraction_to_latex(f)})" if f < 0 else f"{fraction_to_latex(f)}"

    operation = random.choice(["×", "÷"])
    if operation == "÷":
        if f2 < 0:
            expression = f"{f_latex} ÷ ({fraction_to_latex(f2)}{variable})"
        else:
            expression = f"{f_latex} ÷ {fraction_to_latex(f2)}{variable}"
        result = f / f2
    else:
        if f2 < 0:
            expression = f"{f_latex} × ({fraction_to_latex(f2)}{variable})"
        else:
            expression = f"{f_latex} × {fraction_to_latex(f2)}{variable}"
        result = f * f2

    result_str = f"{fraction_to_latex(result.limit_denominator())}{variable}"

    incorrect_result = result + random.choice([Fraction(1, 1), Fraction(-1, 1)])
    while incorrect_result == result:
        incorrect_result = result + random.choice([Fraction(1, 1), Fraction(-1, 1)])
    incorrect_str = f"{fraction_to_latex(incorrect_result)}{variable}" if incorrect_result.denominator != 1 else f"{incorrect_result.numerator}{variable}"

    return f'\\({expression}\\)', f'\\({result_str}\\)', f'\\({incorrect_str}\\)'