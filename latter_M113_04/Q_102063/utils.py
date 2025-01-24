import random
from fractions import Fraction

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

def get_random_variable():
    """랜덤 변수 선택"""
    variables = ['a', 'x', 'y', 'z', 'b']
    return random.choice(variables)