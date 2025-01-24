import random
import math
from fractions import Fraction

# 랜덤 기약분수를 생성하는 함수
def generate_non_simplifiable_fraction():
    while True:
        numerator = random.randint(1, 9)
        denominator = random.randint(2, 9)
        if math.gcd(numerator, denominator) == 1:
            return Fraction(numerator, denominator)

# 분수 또는 정수를 LaTeX 형식으로 포맷팅하는 함수
def format_fraction_with_sign(fraction):
    if fraction.numerator < 0:
        return f"-\\frac{{{abs(fraction.numerator)}}}{{{fraction.denominator}}}"
    else:
        return f"\\frac{{{fraction.numerator}}}{{{fraction.denominator}}}"

# 랜덤 기호를 포함한 분수를 생성하는 함수
def generate_random_sign_fraction():
    denominator = random.randint(2, 9)
    numerator = random.randint(-9, 9)
    while math.gcd(abs(numerator), denominator) != 1 or numerator == 0:
        numerator = random.randint(-9, 9)
    return Fraction(numerator, denominator)

# 정답 출력을 위한 분수 포맷팅 함수
def format_fraction_with_sign_answer(numerator, denominator):
    if numerator < 0:
        return f"-\\frac{{{abs(numerator)}}}{{{denominator}}}" if denominator != 1 else f"-{abs(numerator)}"
    else:
        return f"\\frac{{{numerator}}}{{{denominator}}}" if denominator != 1 else f"{numerator}"

# Fraction 객체를 정답 형식으로 포맷팅하는 함수
def format_fraction_with_sign_answer2(fraction):
    if fraction.numerator < 0:
        return f"-\\frac{{{abs(fraction.numerator)}}}{{{fraction.denominator}}}"
    else:
        return f"\\frac{{{fraction.numerator}}}{{{fraction.denominator}}}"

# 뺄셈 표현에서 뒤에 음수가 올 때 괄호를 포함하도록 처리
def format_subtraction_expression(lhs, rhs):
    lhs_str = format_fraction_with_sign(lhs) if isinstance(lhs, Fraction) else str(lhs)
    rhs_str = f"({format_fraction_with_sign(rhs)})" if isinstance(rhs, Fraction) and rhs.numerator < 0 else (f"({rhs})" if rhs < 0 else str(rhs))
    return f"{lhs_str} - {rhs_str}"