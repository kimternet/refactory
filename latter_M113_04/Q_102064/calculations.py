from .utils import fraction_to_latex, format_variable_expression, generate_irreducible_fraction
from fractions import Fraction
import random

def problem1_or_2():
    """문제 1 또는 2 생성"""
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

    if random.choice([True, False]):
        expression = f"({format_variable_expression(constant1, variable)} + {constant2}) ÷ {abs(constant3)}"
        result = Fraction(constant1, abs(constant3))
        result_constant = Fraction(constant2, abs(constant3))
        result_expression = format_variable_expression(result.numerator, variable)
        latex_result = f"{result_expression} + {fraction_to_latex(result_constant)}"
        step = f"{expression} = ({format_variable_expression(constant1, variable)} + {constant2}) × {fraction_to_latex(Fraction(1, abs(constant3)))}"
    else:
        expression = f"({format_variable_expression(constant3, variable)} - {abs(constant2)}) ÷ ({-abs(constant3)})"
        result = Fraction(-constant3, abs(constant3))
        result_constant = Fraction(abs(constant2), abs(constant3))
        result_expression = format_variable_expression(result.numerator, variable)
        latex_result = f"{result_expression} + {fraction_to_latex(result_constant)}"
        step = f"{expression} = ({format_variable_expression(constant3, variable)} - {abs(constant2)}) × {fraction_to_latex(Fraction(-1, abs(constant3)))}"

    final_answer = latex_result.replace(" + -", " - ")
    step += f" = {final_answer}"
    expression = expression.replace(" + -", " - ")
    return expression, final_answer, step

def problem3():
    """문제 3 생성"""
    frac1, numerator1, denominator1 = generate_irreducible_fraction()
    frac2, numerator2, denominator2 = generate_irreducible_fraction()
    random_divisor = random.randint(2, 20)

    result_addition = frac1 + frac2
    result_multiplication = result_addition * random_divisor
    variable_result = frac1 * random_divisor
    constant_result = frac2 * random_divisor

    variable_latex = fraction_to_latex(variable_result)
    constant_latex = fraction_to_latex(constant_result)

    problem = f"\\left( \\frac{{{numerator1}}}{{{denominator1}}} a + \\frac{{{numerator2}}}{{{denominator2}}} \\right) \\div \\frac{{1}}{{{random_divisor}}}"
    explanation = (
        f"\\left( \\frac{{{numerator1}}}{{{denominator1}}} a + \\frac{{{numerator2}}}{{{denominator2}}} \\right) \\div \\frac{{1}}{{{random_divisor}}} "
        f"= \\left( \\frac{{{numerator1}}}{{{denominator1}}} a + \\frac{{{numerator2}}}{{{denominator2}}} \\right) \\times {random_divisor} "
        f"= {variable_latex}a + {constant_latex}"
    )
    result = f"{variable_latex}a + {constant_latex}"

    return problem, result, explanation

def problem4():
    """문제 4 생성"""
    frac_constant, constant_numerator, constant_denominator = generate_irreducible_fraction()
    divisor, divisor_numerator, divisor_denominator = generate_irreducible_fraction()
    variable_coefficient = random.randint(1, 12)
    variable_sign = random.choice([-1, 1])

    reciprocal = Fraction(divisor_denominator, divisor_numerator)
    result_variable = Fraction(variable_coefficient * variable_sign) * reciprocal
    result_constant = frac_constant * reciprocal

    variable_latex = f"{int(reciprocal * variable_coefficient)}b" if result_variable.denominator == 1 else fraction_to_latex(result_variable) + "b"
    constant_latex = fraction_to_latex(result_constant)

    answer = f"{variable_latex} + {constant_latex}"
    problem = f"\\left( {variable_sign * variable_coefficient}b - \\frac{{{constant_numerator}}}{{{constant_denominator}}} \\right) \\div \\left( - \\frac{{{divisor_numerator}}}{{{divisor_denominator}}} \\right)"
    explanation = (
        f"\\left( {variable_sign * variable_coefficient}b - \\frac{{{constant_numerator}}}{{{constant_denominator}}} \\right) \\div \\left( - \\frac{{{divisor_numerator}}}{{{divisor_denominator}}} \\right)"
        f"\\\\= \\left( {variable_sign * variable_coefficient}b - \\frac{{{constant_numerator}}}{{{constant_denominator}}} \\right) \\times \\left( -\\frac{{{divisor_denominator}}}{{{divisor_numerator}}} \\right)"
        f" = {answer}"
    )

    return problem, answer, explanation