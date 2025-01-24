import random
from fractions import Fraction
import math

def generate_irreducible_fraction():
    """약분되지 않는 기약분수를 생성"""
    numerator = random.randint(1, 10)
    denominator = random.randint(2, 10)
    while math.gcd(numerator, denominator) != 1:
        numerator = random.randint(1, 10)
        denominator = random.randint(2, 10)
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