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
def format_fraction_with_sign(fraction_or_numerator, denominator=None):
    if isinstance(fraction_or_numerator, Fraction):
        numerator = fraction_or_numerator.numerator
        denominator = fraction_or_numerator.denominator
    else:
        numerator = fraction_or_numerator

    if denominator == 1 or denominator is None:
        return f"{numerator}"
    return f"\\frac{{{abs(numerator)}}}{{{denominator}}}" if numerator > 0 else f"-\\frac{{{abs(numerator)}}}{{{denominator}}}"

# 랜덤 기호를 포함한 분수를 생성하는 함수
def generate_random_sign_fraction():
    denominator = random.randint(2, 9)
    numerator = random.randint(-9, 9)
    while math.gcd(abs(numerator), denominator) != 1 or numerator == 0:
        numerator = random.randint(-9, 9)
    return Fraction(numerator, denominator)

# 두 정수를 랜덤하게 생성하여 뺄셈 문제를 만들고 출력
def integer_integer_calculation():
    while True:
        num1 = random.randint(-10, 10)
        num2 = random.randint(-10, 10)
        if num1 != 0 and num2 != 0:
            break

    result = num1 - num2

    num1_str = str(num1)
    num2_str = f"({num2})" if num2 < 0 else str(num2)
    neg_num2_str = str(-num2)

    expression = f"{num1_str} - {num2_str}"
    calculation = f"{num1_str} - {num2_str} = {num1_str} + {neg_num2_str} = {result}"

    return f"\\{expression}\\", f"\\{result}\\", f"\\{calculation}\\"

# 랜덤 소수를 생성하여 뺄셈 문제를 만들고 출력
def decimal_decimal_calculation():
    while True:
        num1 = round(random.uniform(-10, 10), 1)
        num2 = round(random.uniform(-10, 10), 1)
        if num1 != 0 and num2 != 0:
            break

    result = num1 - num2

    num1_str = str(num1)
    num2_str = f"({num2})" if num2 < 0 else str(num2)
    neg_num2_str = str(-num2)

    expression = f"{num1_str} - {num2_str}"
    calculation = f"{num1_str} - {num2_str} = {num1_str} + {neg_num2_str} = {result}"

    return f"\\{expression}\\", f"\\{result}\\", f"\\{calculation}\\"

# 랜덤한 분수를 생성하여 분수의 뺄셈 문제를 만들고 출력
def fraction_fraction_calculation():
    fraction1 = generate_random_sign_fraction()
    fraction2 = generate_random_sign_fraction()

    while abs(fraction1) == abs(fraction2):
        fraction2 = generate_random_sign_fraction()

    fraction1_str = format_fraction_with_sign(fraction1)
    fraction2_str = f"({format_fraction_with_sign(fraction2)})" if fraction2.numerator < 0 else format_fraction_with_sign(fraction2)

    expression = f"{fraction1_str} - {fraction2_str}"

    common_denominator = (fraction1.denominator * fraction2.denominator) // math.gcd(fraction1.denominator, fraction2.denominator)
    
    fraction1_scaled = Fraction(
        fraction1.numerator * (common_denominator // fraction1.denominator),
        common_denominator
    )
    fraction2_scaled = Fraction(
        fraction2.numerator * (common_denominator // fraction2.denominator),
        common_denominator
    )

    result = fraction1_scaled - fraction2_scaled
    simplified_result = result.limit_denominator()

    result_str = format_fraction_with_sign(simplified_result)
    calculation = f"{expression} = {result_str}"

    return f"\\{expression}\\", f"\\{result_str}\\", f"\\{calculation}\\"

# 정수와 소수를 조합하여 뺄셈 문제를 만들고 출력
def integer_decimal_calculation():
    while True:
        num1 = random.randint(-10, 10)
        num2 = round(random.uniform(-10, 10), 1)
        if num1 != 0 and num2 != 0:
            break

    if random.choice([True, False]):
        num1_str = str(num1)
        num2_str = f"({num2})" if num2 < 0 else str(num2)
        neg_num2_str = str(-num2)

        expression = f"{num1_str} - {num2_str}"
        calculation = f"{num1_str} - {num2_str} = {num1_str} + {neg_num2_str}"
        result = num1 - num2
    else:
        num2_str = str(num2)
        num1_str = f"({num1})" if num1 < 0 else str(num1)
        neg_num1_str = str(-num1)

        expression = f"{num2_str} - {num1_str}"
        calculation = f"{num2_str} - {num1_str} = {num2_str} + {neg_num1_str}"
        result = num2 - num1

    calculation += f" = {result}"

    return f"\\{expression}\\", f"\\{result}\\", f"\\{calculation}\\"

# 정수와 분수를 조합하여 뺄셈 문제를 만들고 출력
def integer_fraction_calculation():
    while True:
        num1 = random.randint(-10, 10)
        if num1 != 0:
            break

    fraction = generate_non_simplifiable_fraction()

    if random.choice([True, False]):
        num1_str = str(num1)
        fraction_str = f"({format_fraction_with_sign(fraction)})" if fraction.numerator < 0 else format_fraction_with_sign(fraction)

        expression = f"{num1_str} - {fraction_str}"
        num1_fraction = Fraction(num1 * fraction.denominator, fraction.denominator)
        result = num1_fraction - fraction
    else:
        fraction_str = format_fraction_with_sign(fraction)
        num1_str = f"({num1})" if num1 < 0 else str(num1)

        expression = f"{fraction_str} - {num1_str}"
        num1_fraction = Fraction(num1 * fraction.denominator, fraction.denominator)
        result = fraction - num1_fraction

    simplified_result = result.limit_denominator()
    result_str = format_fraction_with_sign(simplified_result)
    calculation = f"{expression} = {result_str}"

    return f"\\{expression}\\", f"\\{result_str}\\", f"\\{calculation}\\"