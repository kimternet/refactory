import random
from fractions import Fraction
import math

def get_random_nonzero_integer(low, high):
    """0이 아닌 랜덤 정수 생성"""
    value = random.randint(low, high)
    while value == 0:
        value = random.randint(low, high)
    return value

def fraction_to_latex(fraction):
    """Fraction 객체를 LaTeX 문자열로 변환"""
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

def format_variable_expression(coefficient, variable):
    """변수와 계수를 올바르게 포맷"""
    if coefficient == 1:
        return f"{variable}"  # 1은 생략
    elif coefficient == -1:
        return f"-{variable}"  # -1도 생략
    else:
        return f"{coefficient}{variable}"

def generate_irreducible_fraction():
    """약분되지 않는 분수를 생성"""
    numerator = random.randint(1, 12)
    denominator = random.randint(2, 12)
    while math.gcd(numerator, denominator) != 1:
        numerator = random.randint(1, 12)
        denominator = random.randint(2, 12)
    return Fraction(numerator, denominator), numerator, denominator