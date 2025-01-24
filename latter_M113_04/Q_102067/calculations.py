from .utils import generate_irreducible_fraction, fraction_to_latex
from fractions import Fraction
import random

def generate_problem():
    """문제 생성"""
    variables = ['a', 'x', 'y', 'z', 'b']
    variable = random.choice(variables)

    frac_constant, constant_numerator, constant_denominator = generate_irreducible_fraction()
    divisor, divisor_numerator, divisor_denominator = generate_irreducible_fraction()

    variable_coefficient = random.randint(2, 10)
    variable_sign = random.choice([-1, 1])

    # 음수 부호를 포함한 역수 계산
    reciprocal = -Fraction(divisor_denominator, divisor_numerator)
    result_variable = Fraction(variable_coefficient * variable_sign) * reciprocal
    result_constant = (-frac_constant) * reciprocal

    # 분모가 1인 경우 정수로 표현
    variable_latex = f"{result_variable.numerator}{variable}" if result_variable.denominator == 1 else f"{fraction_to_latex(result_variable)}{variable}"
    constant_latex = f"{result_constant.numerator}" if result_constant.denominator == 1 else f"{fraction_to_latex(result_constant)}"

    answer = f"{variable_latex} + {constant_latex}"
    problem = f"\\left( {variable_sign * variable_coefficient}{variable} - \\frac{{{constant_numerator}}}{{{constant_denominator}}} \\right) \\div \\left( - \\frac{{{divisor_numerator}}}{{{divisor_denominator}}} \\right)"

    # 역수의 분모가 1인 경우 처리
    reciprocal_latex = f"(-{divisor_denominator})" if divisor_numerator == 1 else f"(-\\frac{{{divisor_denominator}}}{{{divisor_numerator}}})"

    explanation = (
        f"\\left( {variable_sign * variable_coefficient}{variable} - \\frac{{{constant_numerator}}}{{{constant_denominator}}} \\right) \\div \\left( - \\frac{{{divisor_numerator}}}{{{divisor_denominator}}} \\right)"
        f"\\\\= \\left( {variable_sign * variable_coefficient}{variable} - \\frac{{{constant_numerator}}}{{{constant_denominator}}} \\right) \\times {reciprocal_latex}"
        f" = {answer}"
    )

    return problem, result_variable, result_constant, explanation