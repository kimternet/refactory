import random
from fractions import Fraction
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np
import io
from Dictionary.html_function import *
import itertools
from Dictionary.reference import *
from itertools import combinations
import math
from math import gcd
from fractions import Fraction
import pandas as pd
import random
import sys

sys.path.append('/home/aig2/directDownload/Middle/Grade1_1')
# Reference class initialization
ref = Reference()

# 이미지 파일 불러오는 함수
def load_img(file_path):
    # Load the image using Matplotlib
    img = mpimg.imread(file_path)
    return img

def save_svg_resize(ratio):
    # ratio : 그림 확대 / 축소를 위한 파라미터, 기본값 100      
    file = io.StringIO()
    plt.savefig(file, format='svg', dpi=300, bbox_inches='tight', pad_inches=0.1) # Additional option to remove the rest parts
    file.seek(0)
    svg_data = file.getvalue()
    svg_data = svg_data.replace('<svg ', f'<svg width="{ratio}%" height="{ratio}%"  ') # style="display: block; margin: auto;"

    return svg_data


# QSNO 101220

import random
from .refactory.intan_M112_07.Q_101220.calculations import *
from .refactory.intan_M112_07.Q_101220.utils import *


def intandrationalM112_Stem_07_001():

	
    stem = "다음을 계산하시오.\n"
    problem_type = random.choice(["정수-정수", "소수-소수", "분수-분수", "정수-소수", "정수-분수"])
    
    if problem_type == "정수-정수":
        exp, res, calc = integer_integer_calculation()
    elif problem_type == "소수-소수":
        exp, res, calc = decimal_decimal_calculation()
    elif problem_type == "분수-분수":
        exp, res, calc = fraction_fraction_calculation_with_proper_parentheses_corrected()
    elif problem_type == "정수-소수":
        exp, res, calc = integer_decimal_calculation_modified()
    elif problem_type == "정수-분수":
        exp, res, calc = integer_fraction_calculation_with_multiplication()
    stem += f"{exp}\n"

    answer = f"(정답) {res}\n"
    comment = f"(해설) {calc}\n"

    return stem, answer, comment




# QSNO 101221
import random
from .refactory.intan_M112_07.Q_101221.calculations import *
from .refactory.intan_M112_07.Q_101221.utils import *

def intandrationalM112_Stem_07_002():
   expr1, res1, calc1 = integer_fraction_calculation_with_multiplication()
   expr2, res2, calc2 = integer_fraction_calculation_with_multiplication()
   expr3, res3, calc3 = integer_fraction_calculation_with_multiplication()
   expr4, res4, calc4 = integer_fraction_calculation_with_multiplication()
   expr5, res5, calc5 = integer_fraction_calculation_with_multiplication()

   options = [
       (expr1, res1, calc1),
       (expr2, res2, calc2),
       (expr3, res3, calc3),
       (expr4, res4, calc4),
       (expr5, res5, calc5)
   ]

   random.shuffle(options)

   labels = ['①', '②', '③', '④', '⑤']
   stem = "다음 중 계산 결과가 가장 큰 것은?\n"
   for label, option in zip(labels, options):
       stem += f"{label} {option[0]}\n"

   results = []
   for option in options:
       if 'frac' in option[1]:
           results.append(parse_fraction(option[1]))
       else:
           results.append(float(option[1]))

   max_value = max(results)
   max_index = results.index(max_value)

   answer = f"(정답) {labels[max_index]}\n"
   comment = "(해설)\n"
   for label, option in zip(labels, options):
       comment += f"{label} {option[2]}\n"
   comment += f"따라서 계산 결과가 가장 큰 것은 {labels[max_index]}이다.\n"

   return stem, answer, comment

# QSNO 101222
import random
from .refactory.intan_M112_07.Q_101222.calculations import *
from .refactory.intan_M112_07.Q_101222.utils import *

def intandrationalM112_Stem_07_003(): #메인함수 문제
   expr1, res1, correct_calc1, incorrect_calc1 = integer_integer_calculation()
   expr2, res2, correct_calc2, incorrect_calc2 = decimal_decimal_calculation()
   expr3, res3, correct_calc3, incorrect_calc3 = fraction_fraction_calculation_with_proper_parentheses_corrected()
   expr4, res4, correct_calc4 = integer_fraction_calculation_with_multiplication()

   options = [(expr1, res1, correct_calc1), (expr2, res2, correct_calc2), (expr3, res3, correct_calc3), (expr4, res4, correct_calc4)]

   incorrect_expr1, incorrect_res1, incorrect_correct_calc1, incorrect_incorrect_calc1 = integer_integer_calculation()
   incorrect_expr2, incorrect_res2, incorrect_correct_calc2, incorrect_incorrect_calc2 = decimal_decimal_calculation()
   incorrect_expr3, incorrect_res3, incorrect_correct_calc3, incorrect_incorrect_calc3 = fraction_fraction_calculation_with_proper_parentheses_corrected()

   incorrect_options = [
       (incorrect_expr1, incorrect_res1, incorrect_correct_calc1, incorrect_incorrect_calc1),
       (incorrect_expr2, incorrect_res2, incorrect_correct_calc2, incorrect_incorrect_calc2),
       (incorrect_expr3, incorrect_res3, incorrect_correct_calc3, incorrect_incorrect_calc3)
   ]

   incorrect_expr, incorrect_res, correct_calc, incorrect_calc = random.choice(incorrect_options)

   random_index = random.randint(0, 4)
   options.insert(random_index, (incorrect_expr, incorrect_res, correct_calc, incorrect_calc))

   labels = ['①', '②', '③', '④', '⑤']
   stem = "다음 중 옳지 않은 것은?\n"
   
   for i, (label, option) in enumerate(zip(labels, options)):
       if i == random_index:
           stem += f"{label} {option[3]}\n"
       else:
           stem += f"{label} {option[0]} = {option[1]}\n"

   answer = f"(정답) {labels[random_index]}\n"
   comment = "(해설) "
   for i, (label, option) in enumerate(zip(labels, options)):
       comment += f"{label} {option[2]}\n"

   return stem, answer, comment

# QSNO 101223 
import random
from itertools import combinations
from .refactory.intan_M112_07.Q_101223.calculations import *
from .refactory.intan_M112_07.Q_101223.utils import *

def intandrationalM112_Stem_07_004():
    expressions = [
        integer_integer_calculation(),
        decimal_decimal_calculation(),
        fraction_fraction_calculation_with_proper_parentheses_corrected(),
        integer_fraction_calculation_with_multiplication()
    ]

    selected_expressions = random.sample(expressions, 4)
    labels = ['(ㄱ)', '(ㄴ)', '(ㄷ)', '(ㄹ)']
    labeled_options = list(zip(labels, selected_expressions))

    correct_labels = [label for label, (expr, result, calc) in labeled_options if '-' in result]
    correct_labels_sorted = sorted(correct_labels)
    correct_answer = ", ".join(correct_labels_sorted)

    possible_choices = []
    for i in range(1, 5):
        for combo in combinations(labels, i):
            choice = ", ".join(sorted(combo))
            possible_choices.append(choice)

    possible_choices = list(set(possible_choices))
    if correct_answer in possible_choices:
        possible_choices.remove(correct_answer)
    random.shuffle(possible_choices)
    answer_choices_list = [correct_answer] + possible_choices[:4]
    answer_choices_list = answer_choices_list[:5]
    answer_choices_list = sorted(answer_choices_list, key=lambda x: (len(x.split(',')), x))

    choices_symbols = ['①', '②', '③', '④', '⑤']
    correct_index = answer_choices_list.index(correct_answer)

    stem = "계산 결과가 음수인 것을 보기에서 모두 고른 것은?\n\n"
    text_list = [f"{label}  {expr}" for label, (expr, result, calc) in labeled_options]
    box_stem = make_box_stem(text_list, type=1, mark_title=True, col_count=2) 
    stem += insert_html_code(box_stem)
    stem += "\n\n" + "\n".join([f"{choices_symbols[idx]} {choice}" for idx, choice in enumerate(answer_choices_list)]) + "\n"

    answer = f"(정답) {choices_symbols[correct_index]}\n"
    comment = '(해설)\n'
    for label, (expr, result, calc) in labeled_options:
        comment += f"{label} {calc}\n"
    comment += f"\n이상에서 음수인 것은 {correct_answer}이다.\n"

    return stem, answer, comment


# QSNO 101224
import random
from .refactory.intan_M112_07.Q_101224.calculations import *
from .refactory.intan_M112_07.Q_101224.utils import *

def intandrationalM112_Stem_07_005():
   expressions = [
       integer_integer_calculation(),
       decimal_decimal_calculation(),
       integer_decimal_calculation_modified(),
       fraction_fraction_calculation_with_proper_parentheses_corrected(),
       integer_fraction_calculation_with_multiplication()
   ]

   options = list(expressions)
   random.shuffle(options)

   labels = ['①', '②', '③', '④', '⑤']
   stem = "다음 중 계산 결과가 가장 작은 것은?\n"
   for label, option in zip(labels, options):
       stem += f"{label} {option[0]}\n"

   results = []
   for option in options:
       if 'frac' in option[1]:
           results.append(parse_fraction(option[1]))
       else:
           results.append(float(option[1]))

   min_value = min(results)
   min_index = results.index(min_value)

   answer = f"(정답) {labels[min_index]}\n"
   comment = "(해설) "
   for label, option in zip(labels, options):
       comment += f"{label} {option[2]}\n"
   comment += f"따라서 계산 결과가 가장 작은 것은 {labels[min_index]}이다.\n"

   return stem, answer, comment



# Q 101225
# 보인 변경 (24/12/11) - [메모] 수정 사항 많아서, 우선 서비스 제외
import random
from .refactory.intan_M112_07.Q_101225.calculations import *
from .refactory.intan_M112_07.Q_101225.utils import *

def intandrationalM112_Stem_07_006():
   generated_numbers = []
   while len(generated_numbers) < 5:
       new_number = generate_random_number(generated_numbers)
       generated_numbers.append(new_number)

   sorted_numbers_list = sorted(generated_numbers)
   random_numbers = [f'\\({format_number(num)}\\)' for num in generated_numbers]
   sorted_numbers_str = " \\(\\lt\\) ".join([f'\\({format_number(num)}\\)' for num in sorted_numbers_list])

   a = sorted_numbers_list[0]
   b = sorted_numbers_list[-1]
   operations = ['a + b']
   selected_operation = random.choice(operations)

   result, calculation, fraction_addition = calculate_operation(a, b, selected_operation)
   result_str = format_result(result)

   stem = f"다음 중 가장 큰 수를 \\(a\\), 가장 작은 수를 \\(b\\)라 할 때, \\({selected_operation}\\)의 값을 구하시오.\n"
   text_list = random_numbers
   box_stem = make_box_stem(text_list, type=1, mark_title=True, col_count=7)
   stem += insert_html_code(box_stem)

   answer = f"(정답) \\({result_str}\\)\n"
   comment = f"(해설) {sorted_numbers_str}이므로\n\\(a = {format_number(a)}\\),  \\(b = {format_number(b)}\\)\n"

   if fraction_addition:
       comment += f"\\({selected_operation} = {calculation}\\)\n"
   comment += f"\\(∴ {calculation}\\)\n"

   return stem, answer, comment



# QSNO 101226
import random
from .refactory.intan_M112_07.Q_101226.utils import generate_expression

def intandrationalM112_Stem_07_007():
   correct_num1, correct_num2, correct_expr, correct_result = None, None, None, None
   while correct_result != -5:
       correct_num1, correct_num2, correct_expr, correct_result = generate_expression()

   incorrect_problems = []
   while len(incorrect_problems) < 4:
       num1, num2, expr, result = generate_expression()
       if result != -5:
           incorrect_problems.append((num1, num2, expr, result))

   problems = incorrect_problems + [(correct_num1, correct_num2, correct_expr, correct_result)]
   random.shuffle(problems)

   options = [f"① \\( {problems[0][2]} \\)", 
             f"② \\( {problems[1][2]} \\)",
             f"③ \\( {problems[2][2]} \\)",
             f"④ \\( {problems[3][2]} \\)",
             f"⑤ \\( {problems[4][2]} \\)"]

   stem = "다음 중 계산 결과가 \\(-5\\)인 것은?\n"
   stem += "\n".join(options)

   correct_index = problems.index((correct_num1, correct_num2, correct_expr, correct_result)) + 1
   answer = f"(정답) {'①②③④⑤'[correct_index-1]}\n"

   comment = "(해설) "
   for i, (num1, num2, expr, result) in enumerate(problems):
       sign_conversion = f"\\(({num1:+}) - ({num2:+})\\) \\(= ({num1:+}) + ({-num2:+})\\) \\(= {num1 + (-num2):+}\\)"
       comment += f"{['①', '②', '③', '④', '⑤'][i]} {sign_conversion}\n"

   return stem, answer, comment


# QSNO 101227

import random
from .refactory.intan_M112_07.Q_101227.utils import *

def intandrationalM112_Stem_07_008():
   generated_numbers = []
   while len(generated_numbers) < 5:
       new_number = generate_random_number(generated_numbers)
       generated_numbers.append(new_number)

   sorted_numbers_list = sorted(generated_numbers, key=lambda x: abs(x))
   absolute_values_list = " < ".join([f"|{format_number(num)}|" for num in sorted_numbers_list])

   min_val = sorted_numbers_list[0]
   max_val = sorted_numbers_list[-1]
   result = max_val - min_val

   stem = "다음 수 중에서 절댓값이 가장 큰 수를 \\(A\\), 절댓값이 가장 작은 수를 \\(B\\)라 할 때, \\(B - A\\)의 값을 구하시오.\n"
   numbers_list = ", ".join([f"\\({format_number(num)}\\)" for num in generated_numbers])
   box_stem = make_box_stem(numbers_list, type=1, mark_title=True)
   stem += insert_html_code(box_stem)
   stem += "\n"

   answer = f"(정답) \\({format_result(result)}\\)\n"
   comment = f"(해설) \\(|{format_number(max_val)}| > {absolute_values_list} > |{format_number(min_val)}|\\) 이므로\nA = {format_number(max_val)}, B = {format_number(min_val)}\n따라서 \\(B - A = {format_number(min_val)} - {format_number(max_val)} = {format_result(result)}\\)\n"

   return stem, answer, comment



# QSNO 101228
from .refactory.intan_M112_07.Q_101228.utils import *
import random

def intandrationalM112_Stem_07_009():
   ref.places()
   cities = random.sample(ref.place_city_korea, 5)

   max_temperatures = [round(random.uniform(0, 15), 1) for _ in range(5)]
   min_temperatures = [round(random.uniform(-10, 0), 1) for _ in range(5)]

   temperature_differences = [max_temp - min_temp for max_temp, min_temp in zip(max_temperatures, min_temperatures)]
   max_difference_index = temperature_differences.index(max(temperature_differences))
   max_difference_city = cities[max_difference_index]

   table_stem = generate_table_stem(cities, max_temperatures, min_temperatures)

   stem = ("다음 표는 어느 날 5개의 도시의 최고 기온과 최저 기온을 나타낸 것이다. "
           "5개의 도시 중 일교차가 가장 큰 도시는?\n\n"
           f"{insert_html_code(table_stem)}\n"
           f"① {cities[0]}  ② {cities[1]}  ③ {cities[2]}  \n④ {cities[3]}  ⑤ {cities[4]}")

   circled_numbers = ["①", "②", "③", "④", "⑤"]
   correct_answer = circled_numbers[max_difference_index]
   answer = f"(정답) {correct_answer}"

   comment = "(해설) \n"
   for i, city in enumerate(cities):
       comment += (
           f"{city}: \\( ({convert_to_str_with_sign(max_temperatures[i])}) - ({convert_to_str_with_sign(min_temperatures[i])}) \\)"
           f"\\( = ({convert_to_str_with_sign(max_temperatures[i])}) + ({convert_to_str_with_sign(-min_temperatures[i])}) \\) "         
           f"\\( = {convert_to_str_with_sign_answer(temperature_differences[i])} (°C)\\)\n"
       )
   comment += f"\n따라서 {max_difference_city}의 일교차가 가장 큽니다."

   return stem, answer, comment




# 문항 오류: 문항 교체 후, 검수파일 제출 시 생성하여 제출하겠습니다.
# QSNO 101229
def intandrationalM112_Stem_07_010():

	# 문제
	stem = (f"\n")
	stem += 'intandrationalM112_Stem_07_010'
	# 정답
	answer = "(정답) \n "

	# 해설
	comment = "(해설) \n "

	# 이미지 부분
	svg = "이미지 부분"

	return stem, answer, comment, svg

