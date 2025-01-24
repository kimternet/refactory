import random

def generate_expression():
   while True:
       num1 = random.randint(-10, 10)
       num2 = random.randint(-10, 10)
       if num1 != 0 and num2 != 0:
           break
   expr = f"({num1:+}) - ({num2:+})"
   result = num1 - num2
   return num1, num2, expr, result