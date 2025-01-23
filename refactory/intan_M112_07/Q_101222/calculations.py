from .utils import *
from fractions import Fraction
from math import gcd

def integer_integer_calculation():
   while True:
       num1 = random.randint(-10, 10)
       num2 = random.randint(-10, 10)
       if num1 != 0 and num2 != 0:
           break
       
   correct_result = num1 - num2 
   correct_result_str = str(correct_result) if correct_result >= 0 else f"{correct_result}"
   correct_expression = f"({num1:+}) - ({num2:+})"
   correct_calc = f"({num1:+}) - ({num2:+}) = ({num1:+}) + ({-num2:+}) = {correct_result_str}"

   incorrect_result = num1 + num2
   incorrect_result_str = str(incorrect_result) if incorrect_result >= 0 else f"{incorrect_result}"
   incorrect_calc = f"({num1:+}) - ({num2:+}) = {incorrect_result_str}"

   return f"\\({correct_expression}\\)", f'\\({correct_result_str}\\)', f"\\({correct_calc}\\)", f"\\({incorrect_calc}\\)"

def decimal_decimal_calculation():
   while True:
       num1 = round(random.uniform(-10, 10), 1)
       num2 = round(random.uniform(-10, 10), 1)
       if num1 != 0 and num2 != 0 and int(num1 * 10) % 10 != 0 and int(num2 * 10) % 10 != 0:
           break
   correct_result = num1 + (-num2)
   
   correct_result_str = (
       "0" if correct_result == 0 
       else f"{int(correct_result)}" if correct_result % 1 == 0  
       else f"{round(correct_result, 1)}" 
   )
   correct_expression = f"({num1:+}) - ({num2:+})"
   correct_calculation = f"({num1:+}) - ({num2:+}) = ({num1:+}) + ({-num2:+}) = {correct_result_str}"

   incorrect_result = num1 + num2
   incorrect_result_str = f"{round(incorrect_result, 1)}" if incorrect_result >= 0 else f"{round(incorrect_result, 1):+}"
   incorrect_calc = f"({num1:+}) - ({num2:+}) = {incorrect_result_str}"
   return f"\\({correct_expression}\\)", f"\\({correct_result_str}\\)", f"\\({correct_calculation}\\)", f"\\({incorrect_calc}\\)"

def fraction_fraction_calculation_with_proper_parentheses_corrected():
   fraction1 = generate_random_sign_fraction()
   fraction2 = generate_random_sign_fraction()

   while abs(fraction1) == abs(fraction2):
       fraction2 = generate_random_sign_fraction()

   def format_fraction_with_sign(numerator, denominator):
       sign = "-" if numerator < 0 else "+"
       return f"{sign}\\frac{{{abs(numerator)}}}{{{denominator}}}"
   
   def format_fraction_with_sign_answer(numerator, denominator):
       sign = "-" if numerator < 0 else ""
       if denominator == 1:
           return f"{sign}{abs(numerator)}"    
       else:
           return f"{sign}\\frac{{{abs(numerator)}}}{{{denominator}}}"

   fraction1_str = f"\\left({format_fraction_with_sign(fraction1.numerator, fraction1.denominator)}\\right)"
   fraction2_str = f"\\left({format_fraction_with_sign(fraction2.numerator, fraction2.denominator)}\\right)"
   neg_fraction2_str = f"\\left({format_fraction_with_sign(-fraction2.numerator, fraction2.denominator)}\\right)"

   expression = f"{fraction1_str} - {fraction2_str}"
   calculation = f"{fraction1_str} + {neg_fraction2_str}"

   if fraction1.denominator == fraction2.denominator:
       common_denominator = fraction1.denominator
       fraction1_scaled_numerator = fraction1.numerator
       fraction2_scaled_numerator = -fraction2.numerator
   elif fraction2.denominator % fraction1.denominator == 0:
       common_denominator = fraction2.denominator
       fraction1_scaled_numerator = fraction1.numerator * fraction2.denominator * (common_denominator // fraction1.denominator)
       fraction2_scaled_numerator = -fraction2.numerator
   else:
       common_denominator = (fraction1.denominator * fraction2.denominator) // gcd(fraction1.denominator, fraction2.denominator)
       fraction1_scaled_numerator = fraction1.numerator * fraction2.denominator * (common_denominator // fraction1.denominator)
       fraction2_scaled_numerator = -fraction2.numerator * fraction1.denominator * (common_denominator // fraction2.denominator)

   fraction1_new = Fraction(fraction1_scaled_numerator, common_denominator)
   fraction2_new = Fraction(fraction2_scaled_numerator, common_denominator)

   fraction1_new_str = f"\\left({format_fraction_with_sign(fraction1_new.numerator, common_denominator)}\\right)"
   fraction2_new_str = f"\\left({format_fraction_with_sign(fraction2_new.numerator, common_denominator)}\\right)"

   calculation += f" = {fraction1_new_str} + {fraction2_new_str}"

   result_numerator = (fraction1_new.numerator) + (fraction2_new.numerator)
   result = Fraction(result_numerator, common_denominator)
   simplified_result = result.limit_denominator()

   result_str = format_fraction_with_sign_answer(result.numerator, result.denominator)

   if result != simplified_result:
       simplified_result_str = format_fraction_with_sign_answer(simplified_result.numerator, simplified_result.denominator)
       answer = simplified_result_str
   else:
       answer = result_str

   calculation += f" = {result_str}"

   incorrect_numerator = result_numerator + 3
   incorrect_result = Fraction(incorrect_numerator, common_denominator)
   incorrect_result_str = f"\\frac{{{incorrect_result.numerator}}}{{{incorrect_result.denominator}}}" if incorrect_result.numerator >= 0 else f"\\frac{{{incorrect_result.numerator:+}}}{{{incorrect_result.denominator}}}"
   incorrect_calc = f"{fraction1_str} - {fraction2_str} = {incorrect_result_str}"

   return f"\\({expression}\\)", f"\\({answer}\\)", f"\\({calculation}\\)", f"\\({incorrect_calc}\\)"

def integer_fraction_calculation_with_multiplication():
   while True:
       num1 = random.randint(-10, 10)
       if num1 != 0:
           break
   fraction = generate_non_simplifiable_fraction()

   fraction_str = format_fraction_with_sign(fraction.numerator, fraction.denominator)

   if random.choice([True, False]):
       expression = f"({num1:+}) - ({fraction_str})"
       
       neg_fraction = Fraction(-fraction.numerator, fraction.denominator)
       sign = "" if num1 * fraction.denominator >= 0 else "-"
       neg_fraction_str = f"{sign}\\frac{{{abs(neg_fraction.numerator)}}}{{{neg_fraction.denominator}}}"
       sign_change = f"({num1:+}) + ({neg_fraction_str})"
       
       num1_as_fraction = Fraction(num1 * fraction.denominator, fraction.denominator)
       sign = "+" if num1 * fraction.denominator >= 0 else "-"
       num1_as_fraction_str = f"{sign}\\frac{{{abs(num1 * fraction.denominator)}}}{{{fraction.denominator}}}"
       fraction_addition = f"({num1_as_fraction_str}) + ({neg_fraction_str})"
       
       result = num1_as_fraction + neg_fraction
   else:
       expression = f"({fraction_str}) - ({num1:+})"
       
       neg_num1 = -num1
       sign_change = f"({fraction_str}) + ({neg_num1:+})"
       
       num1_as_fraction = Fraction(neg_num1 * fraction.denominator, fraction.denominator)
       sign = "+" if neg_num1 * fraction.denominator >= 0 else "-"
       num1_as_fraction_str = f"{sign}\\frac{{{abs(num1 * fraction.denominator)}}}{{{abs(fraction.denominator)}}}"
       fraction_addition = f"({fraction_str}) + ({num1_as_fraction_str})"
       
       result = fraction + num1_as_fraction

   simplified_result = result.limit_denominator()
   
   result_str = f"\\frac{{{result.numerator}}}{{{result.denominator}}}" if result.numerator > 0 else f"-\\frac{{{abs(result.numerator)}}}{{{result.denominator}}}"
   
   if result != simplified_result:
       simplified_result_str = f"\\frac{{{simplified_result.numerator}}}{{{simplified_result.denominator}}}" if simplified_result.numerator > 0 else f"-\\frac{{{abs(simplified_result.numerator)}}}{{{simplified_result.denominator}}}"
       answer = simplified_result_str
   else:
       answer = result_str

   calculation = f"{expression} = {sign_change} = {fraction_addition} = {result_str}"

   return f"\\({expression}\\)", f"\\({answer}\\)", f"\\({calculation}\\)"