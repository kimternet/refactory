import random
from fractions import Fraction
import math

def generate_irreducible_fraction():
    """약분되지 않는 기약분수를 생성"""
    numerator = random.randint(1, 12)
    denominator = random.randint(2, 12)
    while math.gcd(numerator, denominator) != 1:
        numerator = random.randint(1, 12)
        denominator = random.randint(2, 12)
    return Fraction(numerator, denominator), numerator, denominator

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
    """변수와 계수를 포맷"""
    if coefficient == 1:
        return f"{variable}"  # 1은 생략
    elif coefficient == -1:
        return f"-{variable}"  # -1도 생략
    else:
        return f"{coefficient}{variable}"

def get_random_nonzero_integer():
    """0이 아닌 랜덤 정수 생성"""
    value = 0
    while value == 0:
        value = random.randint(-10, 10)
    return value

def get_random_nonzero_integer_exclude_one():
    """0과 ±1을 제외한 랜덤 정수 생성"""
    return random.choice([i for i in range(-10, 11) if i not in [-1, 0, 1]])