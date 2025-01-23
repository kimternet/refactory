# utils.py
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