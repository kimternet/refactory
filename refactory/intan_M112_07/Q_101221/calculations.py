import random
from fractions import Fraction
from math import gcd
from .utils import (
   generate_non_simplifiable_fraction,
   parse_fraction
)

def integer_integer_calculation():
   while True:
       num1 = random.randint(-10, 10) 
       num2 = random.randint(-10, 10)
       if num1 != 0 and num2 != 0:
           break

   result = num1 - num2
   result_str = str(result) if result >= 0 else f"{result:+}"
   expression = f"({num1:+}) - ({num2:+})"
   calculation = f"({num1:+}) - ({num2:+}) = ({num1:+}) + ({-num2:+}) = {result_str}"
   
   return f"\\({expression}\\)", result_str if result >= 0 else result_str, f"\\({calculation}\\)"

def decimal_decimal_calculation():
   while True:
       num1 = round(random.uniform(-10, 10), 1)
       num2 = round(random.uniform(-10, 10), 1) 
       if num1 != 0 and num2 != 0 and int(num1 * 10) % 10 != 0 and int(num2 * 10) % 10 != 0:
           break
   result = num1 + (-num2)
   result_str = (
       "0" if result == 0 
       else f"{int(result)}" if result % 1 == 0
       else f"{round(result, 1)}"
   )
   expression = f"({num1:+}) - ({num2:+})"
   calculation = f"({num1:+}) - ({num2:+}) = ({num1:+}) + ({-num2:+}) = {result_str}"
   return f"\\({expression}\\)", f"{result_str}" if result >= 0 else result_str, f"\\({calculation}\\)"

def generate_random_sign_fraction():
   fraction = generate_non_simplifiable_fraction()
   sign = random.choice([-1, 1])
   return Fraction(sign * fraction.numerator, fraction.denominator)

def fraction_fraction_calculation_with_proper_parentheses_corrected():
   fraction1 = generate_random_sign_fraction()
   fraction2 = generate_random_sign_fraction()

   def format_fraction_with_sign(fraction):
       sign = "-" if fraction.numerator < 0 else "+"
       return f"{sign}\\frac{{{abs(fraction.numerator)}}}{{{fraction.denominator}}}"
   
   def format_fraction_with_sign_answer2(fraction):
       sign = "-" if fraction.numerator < 0 else ""
       if fraction.denominator == 1:
           return f"{sign}{abs(fraction.numerator)}"
       else:      
           return f"{sign}\\frac{{{abs(fraction.numerator)}}}{{{fraction.denominator}}}"

   fraction1_str = f"\\left({format_fraction_with_sign(fraction1)}\\right)"
   fraction2_str = f"\\left({format_fraction_with_sign(fraction2)}\\right)"

   neg_fraction2 = Fraction(-fraction2.numerator, fraction2.denominator)
   neg_fraction2_str = f"\\left({format_fraction_with_sign(neg_fraction2)}\\right)"

   expression = f"{fraction1_str} - {fraction2_str}"
   calculation = f"{fraction1_str} - {fraction2_str} = {fraction1_str} + {neg_fraction2_str}"

   common_denominator = fraction1.denominator * fraction2.denominator
   fraction1_new = Fraction(fraction1.numerator * fraction2.denominator, common_denominator)
   fraction2_new = Fraction(-fraction2.numerator * fraction1.denominator, common_denominator)

   fraction1_new_str = f"\\left({format_fraction_with_sign(fraction1_new)}\\right)"
   fraction2_new_str = f"\\left({format_fraction_with_sign(fraction2_new)}\\right)"

   calculation += f" = {fraction1_new_str} + {fraction2_new_str}"

   result = fraction1_new + fraction2_new
   simplified_result = result.limit_denominator()

   result_str = format_fraction_with_sign_answer2(result)
   answer = result_str

   calculation += f" = {result_str}"

   return f"\\({expression}\\)", f"\\({answer}\\)", f"\\({calculation}\\)"

def integer_decimal_calculation_modified():
   while True:
       num1 = random.randint(-10, 10)
       num2 = round(random.uniform(-10, 10), 1)
       if num1 != 0 and num2 != 0 and int(num2 * 10) % 10 != 0:
           break
           
   if random.choice([True, False]):
       expression = f"({num1:+}) - ({num2:+})"
       calculation = f"({num1:+}) - ({num2:+}) = ({num1:+}) + ({-num2:+})"
       result = num1 + (-num2)
   else:
       expression = f"({num2:+}) - ({num1:+})"
       calculation = f"({num2:+}) - ({num1:+}) = ({num2:+}) + ({-num1:+})"
       result = num2 + (-num1)

   result_str = "0" if result == 0 else f"{round(result, 1)}" if result >= 0 else f"{round(result, 1):+}"
   calculation += f" = {result_str}"
   
   return f"\\({expression}\\)", result_str, f"\\({calculation}\\)"

def integer_fraction_calculation_with_multiplication():
   while True:
       num1 = random.randint(-10, 10)
       if num1 != 0:
           break
   fraction = generate_non_simplifiable_fraction()

   def format_fraction_with_sign(fraction):
       sign = "-" if fraction.numerator < 0 else "+"
       return f"{sign}\\frac{{{abs(fraction.numerator)}}}{{{fraction.denominator}}}"

   fraction_str = format_fraction_with_sign(fraction)

   if random.choice([True, False]):
       expression = f"({num1:+}) - ({fraction_str})"

       neg_fraction = Fraction(-fraction.numerator, fraction.denominator)
       neg_fraction_str = format_fraction_with_sign(neg_fraction)
       sign_change = f"({num1:+}) + ({neg_fraction_str})"

       num1_as_fraction = Fraction(num1 * fraction.denominator, fraction.denominator)
       num1_as_fraction_str = format_fraction_with_sign(num1_as_fraction)
       fraction_addition = f"({num1_as_fraction_str}) + ({neg_fraction_str})"

       result = num1_as_fraction + neg_fraction
   else:
       expression = f"({fraction_str}) - ({num1:+})"

       neg_num1 = -num1
       neg_num1_as_fraction = Fraction(neg_num1 * fraction.denominator, fraction.denominator)
       neg_num1_as_fraction_str = format_fraction_with_sign(neg_num1_as_fraction)
       sign_change = f"({fraction_str}) + ({neg_num1:+})"
       fraction_addition = f"({fraction_str}) + ({neg_num1_as_fraction_str})"

       result = fraction + neg_num1_as_fraction

   simplified_result = result.limit_denominator()

   result_str = format_fraction_with_sign(result)
   if result != simplified_result:
       simplified_result_str = format_fraction_with_sign(simplified_result)
       answer = simplified_result_str
   else:
       answer = result_str

   calculation = f"{expression} = {sign_change} = {fraction_addition} = {result_str}"

   return f"\\({expression}\\)", f"\\({answer}\\)", f"\\({calculation}\\)"