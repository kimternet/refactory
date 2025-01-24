from .utils import *
from fractions import Fraction
from math import gcd

def calculate_operation(a, b, operation='a + b'):
   fraction_addition = ""
   
   if operation == 'a - b' or operation == 'a + b':
       if isinstance(a, float) and isinstance(b, Fraction):
           a_as_fraction = Fraction(a).limit_denominator(10)
           expression = f"\\left({a}\\right) - \\left(\\frac{{{b.numerator}}}{{{b.denominator}}}\\right)"
           sign_change = f"\\left(\\frac{{{a_as_fraction.numerator}}}{{{a_as_fraction.denominator}}}\\right) - \\left(\\frac{{{b.numerator}}}{{{b.denominator}}}\\right)"
           result = a_as_fraction - b if operation == 'a - b' else a_as_fraction + b
           calculation = f"{expression} = {sign_change} = {format_result(result)}"
           
       elif isinstance(a, Fraction) and isinstance(b, float):
           b_as_fraction = Fraction(b).limit_denominator(10)
           expression = f"\\left({format_fraction_with_sign(a.numerator, a.denominator)}\\right) -  \\left({b}\\right)"
           sign_change = f"\\left({format_fraction_with_sign(a.numerator, a.denominator)}\\right) - \\left({format_fraction_with_sign(b_as_fraction.numerator, b_as_fraction.denominator)}\\right)"
           result = a - b_as_fraction if operation == 'a - b' else a + b_as_fraction
           calculation = f"{expression} = {sign_change} = {format_result(result)}"
           
       elif isinstance(a, int) and isinstance(b, Fraction):
           a_as_fraction = Fraction(a * b.denominator, b.denominator)
           neg_fraction = Fraction(-b.numerator, b.denominator)
           expression = f"\\left({a}\\right) - \\left({format_fraction_with_sign(b.numerator, b.denominator)}\\right)"
           sign_change = f"\\left(\\frac{{{a_as_fraction.numerator}}}{{{a_as_fraction.denominator}}}\\right) + \\left(\\frac{{{neg_fraction.numerator}}}{{{neg_fraction.denominator}}}\\right)"
           fraction_addition = f"\\left(\\frac{{{a_as_fraction.numerator}}}{{{b.denominator}}}\\right) + \\left(\\frac{{{neg_fraction.numerator}}}{{{neg_fraction.denominator}}}\\right)"
           result = a_as_fraction + neg_fraction 
           calculation = f"{expression} = {sign_change} = {fraction_addition} = {format_result(result)}"
           
       elif isinstance(a, Fraction) and isinstance(b, int):
           b_as_fraction = Fraction(b * a.denominator, a.denominator)
           sign_change = f"\\left(\\frac{{{a.numerator}}}{{{a.denominator}}}\\right) + \\left(\\frac{{{-b * a.denominator}}}{{{a.denominator}}}\\right)"
           result = a + b_as_fraction if operation == 'a + b' else a - b_as_fraction
           calculation = f"\\left(\\frac{{{a.numerator}}}{{{a.denominator}}}\\right) - \\left({b}\\right) = {sign_change} = {format_result(result)}"
           
       elif isinstance(a, Fraction) and isinstance(b, Fraction):
           numerator_a = a.numerator * b.denominator
           numerator_b = b.numerator * a.denominator
           common_denominator = a.denominator * b.denominator
           expression = f"\\left(\\frac{{{a.numerator}}}{{{a.denominator}}}\\right) + \\left(\\frac{{{b.numerator}}}{{{b.denominator}}}\\right)"
           detailed_addition = f"\\left(\\frac{{{numerator_a}}}{{{common_denominator}}}\\right) + \\left(\\frac{{{numerator_b}}}{{{common_denominator}}}\\right)"
           result = Fraction(numerator_a + numerator_b, common_denominator)
           calculation = f"{expression} = {detailed_addition} = {format_result(result)}"
           
       else:
           expression = f"\\left({a}\\right) - \\left({b}\\right)" if operation == 'a - b' else f"\\left({a}\\right) + \\left({b}\\right)"
           result = a - b if operation == 'a - b' else a + b
           calculation = f"{expression} = {format_decimal_result(result) if isinstance(a, (int, float)) and isinstance(b, (int, float)) else format_result(result)}"

   elif operation == 'a * b':
       expression = f"\\left({format_fraction_with_sign(a)}\\right) * \\left({format_fraction_with_sign(b)}\\right)"
       result = a * b
       calculation = f"{expression} = {format_decimal_result(result) if isinstance(a, (int, float)) and isinstance(b, (int, float)) else format_result(result)}"

   return result, calculation, fraction_addition