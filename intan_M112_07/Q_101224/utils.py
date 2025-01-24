import random
import math
from fractions import Fraction

def generate_non_simplifiable_fraction():
   while True:
       numerator = random.randint(1, 9)
       denominator = random.randint(2, 9)
       if math.gcd(numerator, denominator) == 1:
           return Fraction(numerator, denominator)

def format_fraction_with_sign(numerator, denominator):
   sign = "-" if numerator < 0 else "+"
   return f"{sign}\\frac{{{abs(numerator)}}}{{{denominator}}}"
   
def generate_random_sign_fraction():
   fraction = generate_non_simplifiable_fraction()
   sign = random.choice([-1, 1])  
   return Fraction(sign * fraction.numerator, fraction.denominator)

def parse_fraction(fraction_str):
   try:
       fraction_str = fraction_str.replace("\\frac{", "").replace("}", "")
       numerator, denominator = fraction_str.split("/")
       return int(numerator) / int(denominator)
   except ValueError:
       return 0