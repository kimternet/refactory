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
               numerator = random.randint(1, 9)
               denominator = random.randint(2, 9)
               if math.gcd(numerator, denominator) == 1:
                   fraction_num = Fraction(numerator, denominator) * random.choice([1, -1])
                   if fraction_num not in existing_numbers and fraction_num != Fraction(1):
                       return fraction_num

def format_number(num):
   if isinstance(num, Fraction):
       return f"\\frac{{{abs(num.numerator)}}}{{{num.denominator}}}" if num >= 0 else f"-\\frac{{{abs(num.numerator)}}}{{{num.denominator}}}"
   else:
       return f"{abs(num)}" if num >= 0 else f"-{abs(num)}"

def format_result(result):
   if isinstance(result, Fraction):
       return f"\\frac{{{result.numerator}}}{{{result.denominator}}}"
   elif isinstance(result, float):
       return f"{round(result, 1)}"
   else:
       return f"{int(result)}"