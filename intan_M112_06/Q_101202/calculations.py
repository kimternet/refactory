import random
from fractions import Fraction
from math import gcd 

def generate_fraction_components(result_numerator, result_denominator):
   gcd_value = gcd(result_numerator, result_denominator)

   if gcd_value > 1:
       simplified_numerator = result_numerator // gcd_value
       simplified_denominator = result_denominator // gcd_value
       
       if result_numerator > 0:
           result_latex = f"\\frac{{{result_numerator}}}{{{result_denominator}}} = "
           result_latex += f"\\frac{{{simplified_numerator}}}{{{simplified_denominator}}}"
       elif result_numerator == 0:
           result_latex = "0"
       elif simplified_denominator == 1:
           result_latex = f"-\\frac{{{abs(result_numerator)}}}{{{result_denominator}}} = {simplified_numerator}"
       else:
           result_latex = f"-\\frac{{{abs(result_numerator)}}}{{{result_denominator}}} = "
           result_latex += f"-\\frac{{{abs(simplified_numerator)}}}{{{simplified_denominator}}}"
   else:
       if result_numerator > 0:
           result_latex = f"\\frac{{{result_numerator}}}{{{result_denominator}}}"
       elif result_numerator == 0:
           result_latex = "0"
       else:
           result_latex = f"-\\frac{{{abs(result_numerator)}}}{{{result_denominator}}}"
   
   return result_latex