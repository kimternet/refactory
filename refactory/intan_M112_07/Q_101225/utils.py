import random
import math
from fractions import Fraction

def generate_random_number(existing_numbers):
   while True:
       number_type = random.choice(['integer', 'decimal', 'fraction'])
       
       if number_type == 'integer':
           num = random.randint(-10, 10)
           if num != 0 and num not in existing_numbers:
               return num
               
       elif number_type == 'decimal':
           num = round(random.uniform(-10, 10), 1)
           if num % 1 != 0 and num not in existing_numbers:
               return num
               
       elif number_type == 'fraction':
           while True:
               numerator = random.randint(1, 4)
               denominator = random.randint(2, 6)
               if math.gcd(numerator, denominator) == 1:
                   fraction_num = Fraction(numerator, denominator) * random.choice([1, -1])
                   if fraction_num not in existing_numbers and fraction_num not in [Fraction(1), Fraction(0)]:
                       return fraction_num

def format_fraction_with_sign(numerator, denominator):
   sign = "-" if numerator < 0 else "+"
   return f"{sign}\\frac{{{abs(numerator)}}}{{{denominator}}}"

def format_fraction_with_sign_answer(numerator, denominator):        
   sign = "-" if numerator < 0 else ""
   if denominator == 1:
       return f"{sign}{abs(numerator)}"
   else:
       return f"{sign}\\frac{{{abs(numerator)}}}{{{denominator}}}"

def format_result(result):
   if isinstance(result, Fraction):
       return format_fraction_with_sign_answer(result.numerator, result.denominator)
   elif isinstance(result, float):
       return f"{round(result, 1)}"
   else:
       return f"{int(result)}"

def format_decimal_result(result):
   if result == 0:
       return "0"
   if isinstance(result, float) or isinstance(result, int):
       return f"{round(result, 1)}" if result % 1 != 0 else f"{int(result)}" 
   else:
       return str(result)

def format_number(num):
   if num == 0:
       return "0"
   if isinstance(num, Fraction):
       return f"\\left(+\\frac{{{abs(num.numerator)}}}{{{num.denominator}}}\\right)" if num >= 0 else f"\\left(-\\frac{{{abs(num.numerator)}}}{{{num.denominator}}}\\right)"
   else:
       return f"\\left({num:+}\\right)"