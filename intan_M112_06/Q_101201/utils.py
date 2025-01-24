import random
from fractions import Fraction

def format_with_sign(value):
   return f"+{value}" if value > 0 else str(value)

def generate_unique_fraction():
   while True:
       a = Fraction(random.choice([i for i in range(-5, 6) if i != 0]), random.randint(2, 4))
       b = Fraction(random.choice([i for i in range(-5, 6) if i != 0]), random.randint(2, 4))
       
       if (a.denominator != b.denominator and
           not (a.numerator % a.denominator == 0 or b.numerator % b.denominator == 0) and
           not ({a.denominator, b.denominator} == {2, 4})):
           return a, b

def format_fraction_str(fraction, with_sign=True):
   if fraction.denominator == 1:
       if with_sign:
           return format_with_sign(fraction.numerator)
       return str(fraction.numerator)
   if fraction < 0:
       return f"-\\frac{{{abs(fraction.numerator)}}}{{{fraction.denominator}}}"
   return f"+\\frac{{{fraction.numerator}}}{{{fraction.denominator}}}" if with_sign else f"\\frac{{{fraction.numerator}}}{{{fraction.denominator}}}"

# calculations.py
def generate_integer_expression():
   a = random.choice([i for i in range(-5, 6) if i != 0])
   b = random.choice([i for i in range(-5, 6) if i != 0])
   result = a + b
   
   expression = f"\\( ({format_with_sign(a)}) + ({format_with_sign(b)}) = {result} \\)"
   explanation = f"\\( ({format_with_sign(a)}) + ({format_with_sign(b)}) = ({a} {'+ ' + str(b) if b > 0 else str(b)}) = {result} \\)"
   
   return a, b, result, expression, explanation

def generate_fraction_expression():
   a, b = generate_unique_fraction()
   result = a + b
   
   a_str = format_fraction_str(a)
   b_str = format_fraction_str(b)
   result_str = format_fraction_str(result, with_sign=False)
   
   expression = f"\\( ({a_str}) + ({b_str}) = {result_str} \\)"
   
   frac1 = (f"\\frac{{{a.numerator * b.denominator}}}{{{a.denominator * b.denominator}}}" 
            if a.numerator * b.denominator > 0 
            else f"(-\\frac{{{abs(a.numerator * b.denominator)}}}{{{a.denominator * b.denominator}}})")
   
   frac2 = (f"\\frac{{{b.numerator * a.denominator}}}{{{a.denominator * b.denominator}}}" 
            if b.numerator * a.denominator > 0 
            else f"(-\\frac{{{abs(b.numerator * a.denominator)}}}{{{a.denominator * b.denominator}}})")
   
   explanation = f"\\( ({a_str}) + ({b_str}) = {frac1} + {frac2} = {result_str} \\)"
   
   return a, b, result, expression, explanation

def generate_decimal_expression():
   a = round(random.choice([i for i in range(-5, 6) if i != 0]) + random.uniform(-0.9, 0.9), 1)
   b = round(random.choice([i for i in range(-5, 6) if i != 0]) + random.uniform(-0.9, 0.9), 1)
   result = round(a + b, 1)
   result = int(result) if result.is_integer() else result
   
   expression = f"\\( ({format_with_sign(a)}) + ({format_with_sign(b)}) = {result} \\)"
   explanation = f"\\( ({format_with_sign(a)}) + ({format_with_sign(b)}) = ({round(a, 1)} {'+ ' + str(round(b, 1)) if b > 0 else str(round(b, 1))}) = {result} \\)"
   
   return a, b, result, expression, explanation