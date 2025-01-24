import random
from fractions import Fraction
from math import gcd 

def lcm(x, y):
   return abs(x * y) // gcd(x, y)

def format_number_to_mathjax(num):
   fraction = Fraction(num) if '/' in num else Fraction(int(num))
   if fraction.denominator == 1:
       return f"\\({fraction.numerator}\\)" if fraction.numerator >= 0 else f"\\(-{abs(fraction.numerator)}\\)"
   else:
       return (f"\\(\\frac{{{abs(fraction.numerator)}}}{{{fraction.denominator}}}\\)" 
               if fraction.numerator >= 0 
               else f"\\(-\\frac{{{abs(fraction.numerator)}}}{{{fraction.denominator}}}\\)")

def format_number_to_mathjax_abs(num):
   fraction = Fraction(num) if '/' in num else Fraction(int(num))
   if fraction.denominator == 1:
       return f"\\(|{fraction.numerator}|\\)" 
   else:
       return f"\\(|\\frac{{{abs(fraction.numerator)}}}{{{fraction.denominator}}}|\\)"

def convert_mathjax(stem, answer, comment):
   stem = stem.replace("\\(", "$$수식$$").replace("\\)", "$$/수식$$")
   answer = answer.replace("\\(", "$$수식$$").replace("\\)", "$$/수식$$") 
   comment = comment.replace("\\(", "$$수식$$").replace("\\)", "$$/수식$$")
   return stem, answer, comment