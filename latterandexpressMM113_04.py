import random
from fractions import Fraction
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np
import io
# from Dictionary.html_function import *
import itertools
from Dictionary.reference import *
from itertools import combinations
import math
from sympy import symbols, Rational, simplify, nsimplify
from math import gcd


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



'''#################

# QSNO 102060

'''##################

from .refactory.latter_M113_04.Q_102060.utils import get_random_variable, get_nonzero_random_int
from .refactory.latter_M113_04.Q_102060.calculations import generate_problem1, generate_problem2, generate_problem3


def latterandexpress_StemM113_04_001():
    variable = get_random_variable()
    constant1 = get_nonzero_random_int()
    constant2 = get_nonzero_random_int()

    problem_generating_functions = [
        lambda: generate_problem1(constant1, constant2, variable),
        lambda: generate_problem2(constant1, constant2, variable),
        lambda: generate_problem3(constant1, constant2, variable)
    ]

    selected_function = random.choice(problem_generating_functions)
    problem, result, _ = selected_function()

    stem = f"{problem}을 계산하시오.\n"
    answer = f"(정답) {result}\n"
    comment = f"(해설) 생략\n"
    
    return stem, answer, comment

'''#################

# QSNO 102061

'''##################

from .refactory.latter_M113_04.Q_102061.utils import (
    get_random_nonzero_integer,
    get_random_variable,
    fraction_to_latex
)

from .refactory.latter_M113_04.Q_102061.calculations import (
    generate_problem1,
    generate_problem2, 
    generate_problem3
)

def latterandexpress_StemM113_04_002():
    problems = [generate_problem1, generate_problem2, generate_problem3]
    selected_problems = [random.choice(problems)() for _ in range(5)]
    correct_index = random.randint(0, 4)

    options = []
    for i, (expression, correct_result, incorrect_result) in enumerate(selected_problems):
        if i == correct_index:
            options.append((expression, correct_result, True))
        else:
            options.append((expression, incorrect_result, False))

    option_labels = ['①', '②', '③', '④', '⑤']
    options_with_labels = list(zip(option_labels, options))
    correct_option_label = option_labels[correct_index]

    stem = "다음 중 옳은 것은?\n"
    options_text = "\n".join([f"{label} {expression} \\(=\\){result}" 
                            for label, (expression, result, _) in options_with_labels])
    stem += options_text + "\n"

    answer = f"(정답) {correct_option_label}\n"

    comment = "(해설) "
    for label, (expression, result, is_correct) in options_with_labels:
        if is_correct:
            continue
        for expr, correct_res, _ in selected_problems:
            if expr == expression:
                correct_result = correct_res
                break
        comment += f"{label} {expression} \\(=\\) {correct_result}\n"

    return stem, answer, comment


# QSNO 102062
from refactory.latter_M113_04.Q_102062.utils import (
    get_random_variable
)

from refactory.latter_M113_04.Q_102062.calculations import (
    generate_problem1,
    generate_problem2,
    generate_problem3
)
import random

def latterandexpress_StemM113_04_003():
    variable = get_random_variable()
    problem_functions = [generate_problem1, generate_problem2, generate_problem3]
    selected_function = random.choice(problem_functions)
    problem, result = selected_function(variable)

    stem = f"\\({problem}\\)을 계산하시오.\n"
    answer = f"(정답) \\({result}\\)\n"
    comment = f"(해설) 생략\n"

    return stem, answer, comment

'''#################

# QSNO 102063

'''##################
from refactory.latter_M113_04.Q_102063.utils import get_random_variable
from refactory.latter_M113_04.Q_102063.calculations import (
    generate_problem1,
    generate_problem5
)
import random

def latterandexpress_StemM113_04_004():
    variable = get_random_variable()
    problem_functions = [generate_problem1, generate_problem5]
    selected_function = random.choice(problem_functions)

    if selected_function == generate_problem5:
        problem, answer, calculation = selected_function()
        comment = f"(해설) \\({calculation}\\)\n"
    else:
        problem, answer = selected_function(variable)
        comment = "(해설) 생략\n"

    stem = f"\\({problem}\\)을 계산하시오.\n"
    answer = f"(정답) \\({answer}\\)\n"

    return stem, answer, comment

# QSNO 102064
from refactory.latter_M113_04.Q_102064.calculations import problem1_or_2, problem3, problem4
import random

def latterandexpress_StemM113_04_005():
    problem_generating_functions = [problem1_or_2, problem3, problem4]
    selected_function = random.choice(problem_generating_functions)

    problem, answer, calculation = selected_function()

    stem = f"\\({problem}\\)을 계산하시오.\n"
    answer = f"(정답) \\({answer}\\)\n"
    comment = f"(해설) \\({calculation}\\)\n"

    return stem, answer, comment


# QSNO 102065
from refactory.latter_M113_04.Q_102065.calculations import problem1, problem2, problem3, problem4
import random

def latterandexpress_StemM113_04_006():
    problem_generating_functions = [problem1, problem2, problem3, problem4]
    selected_function = random.choice(problem_generating_functions)

    problem, answer, calculation = selected_function()

    stem = f"\\({problem}\\)을 계산하시오.\n"
    answer = f"(정답) \\({answer}\\)\n"
    comment = f"(해설) \\({calculation}\\)\n"

    return stem, answer, comment
'''##################

# QSNO 102066

'''##################
from refactory.latter_M113_04.Q_102066.calculations import problem1, problem2, problem3
import random

def latterandexpress_StemM113_04_007():
    problems = [problem1, problem2, problem3]
    selected_problems = [random.choice(problems)() for _ in range(5)]

    correct_index = random.randint(0, 4)
    option_labels = ['①', '②', '③', '④', '⑤']
    options_with_labels = []

    for i, (expression, correct_result, incorrect_result, step) in enumerate(selected_problems):
        if i == correct_index:
            options_with_labels.append((option_labels[i], expression, correct_result, True))
        else:
            options_with_labels.append((option_labels[i], expression, incorrect_result, False))

    stem = "다음 중 옳은 것은?\n" + "\n".join([f"{label} {expression} = {result}" for label, expression, result, _ in options_with_labels])
    answer = f"(정답) {option_labels[correct_index]}\n"

    comment = "(해설)\n"
    for label, expression, result, is_correct in options_with_labels:
        if not is_correct:
            comment += f"{label} {result}\n"

    return stem, answer, comment

'''#################

# QSNO 102067

'''##################
from refactory.latter_M113_04.Q_102067.calculations import generate_problem
from refactory.latter_M113_04.Q_102067.utils import fraction_to_latex

def latterandexpress_StemM113_04_008():
    """문제와 정답을 생성"""
    problem, result_variable, result_constant, explanation = generate_problem()

    variable = problem.split("{")[1][0]  # 변수 추출 (문제에서 'a', 'x' 등)
    stem = f'\\({problem}\\)를 계산한 식에서 \\({variable}\\)의 계수와 상수항의 합을 구하시오.'

    # 정답 계산 (계수와 상수항의 합)
    result = result_variable + result_constant
    result_str = fraction_to_latex(result)

    # 정답 출력
    answer = f"(정답) \\({result_str}\\)\n"

    # 해설 생성
    comment = f"(해설) \\({explanation}\\)\n따라서 \\({variable}\\)의 계수는 \\({fraction_to_latex(result_variable)}\\), 상수항은 \\({fraction_to_latex(result_constant)}\\)이므로\n"
    if result_variable > 0 and result_constant < 0:
        result_constant_str = f"({fraction_to_latex(result_constant)})"
        comment += f"\\({fraction_to_latex(result_variable)} + {result_constant_str} = {result_str}\\)"
    elif result_variable > 0 and result_constant > 0:
        comment += f"\\({fraction_to_latex(result_variable)} + {fraction_to_latex(result_constant)} = {result_str}\\)\n"
    elif result_variable < 0 and result_constant > 0:
        comment += f"\\(({fraction_to_latex(result_variable)}) + {fraction_to_latex(result_constant)} = {result_str}\\)\n"
    elif result_variable < 0 and result_constant < 0:
        comment += f"\\(({fraction_to_latex(result_variable)}) + ({fraction_to_latex(result_constant)}) = {result_str}\\)\n"

    return stem, answer, comment

# QSNO 102068
from refactory.latter_M113_04.Q_102068.calculations import generate_problem
from refactory.latter_M113_04.Q_102068.utils import fraction_to_latex
import random

def latterandexpress_StemM113_04_009():
    """문제와 정답을 생성"""
    problem, result_variable, result_constant, explanation = generate_problem()

    calc = random.choice(['a + b', 'a - b', 'ab'])
    variable = problem.split("{")[1][0]  # 변수 추출 (문제에서 'x', 'y', 'z')

    stem = f'\\({problem}\\)을 계산하면 \\(ax + b\\)일 때, 상수 \\(a\\), \\(b\\)에 대하여 \\({calc}\\)의 값을 구하시오.\n'

    a = result_variable
    a_str = f"({fraction_to_latex(a)})" if a < 0 else f"{fraction_to_latex(a)}"
    b = result_constant
    b_str = f"({fraction_to_latex(b)})" if b < 0 else f"{fraction_to_latex(b)}"

    if calc == 'a + b':
        sign = '+'
        result = a + b
    elif calc == 'a - b':
        sign = '-'
        result = a - b
    elif calc == 'ab':
        sign = '×'
        result = a * b

    result_str = fraction_to_latex(result)
    answer = f"(정답) \\({result_str}\\)\n"

    # 해설 생성
    comment = f"(해설) \\({explanation}\\)\n따라서 \\(a = {a_str}\\), \\(b = {b_str}\\)이므로\n"
    comment += f"\\({calc} = {a_str} {sign} {b_str} = {result_str}\\)\n"

    return stem, answer, comment

'''#################

# QSNO 102069

'''##################
from refactory.latter_M113_04.Q_102069.calculations import generate_problem
from refactory.latter_M113_04.Q_102069.utils import fraction_to_latex
import random

def latterandexpress_StemM113_04_010():
    """문제와 정답 생성"""
    variables = ['a', 'x', 'y', 'z', 'b']
    variable = random.choice(variables)

    problem, result_variable, result_constant, explanation = generate_problem(variable)

    # 정답 계산
    correct_result = result_variable + result_constant
    correct_result_latex = fraction_to_latex(correct_result)

    # 문제 출력
    stem = f"다음 중 계산 결과가 \\({correct_result_latex}\\)과 같은 것은?\n"

    # 정답 생성
    correct_option = f"\\({problem}\\) = {correct_result_latex}"

    # 오답 생성
    incorrect_options = []
    for _ in range(4):
        while True:
            _, incorrect_variable, incorrect_constant, _ = generate_problem(variable)
            if incorrect_variable + incorrect_constant != correct_result:
                incorrect_result = fraction_to_latex(incorrect_variable + incorrect_constant)
                incorrect_options.append(f"\\({problem}\\) = {incorrect_result}")
                break

    # 정답과 오답을 섞기
    options = [correct_option] + incorrect_options
    random.shuffle(options)

    # 선택지 출력
    option_labels = ['①', '②', '③', '④', '⑤']
    for label, option in zip(option_labels, options):
        stem += f"{label} {option}\n"

    # 정답 번호
    correct_option_index = options.index(correct_option)
    answer = f"(정답) {option_labels[correct_option_index]}\n"

    # 해설 생성
    comment = f"(해설) 정답은 \\({correct_result_latex}\\)이며, 계산 과정은 아래와 같습니다:\n"
    comment += f"{explanation}\n"

    return stem, answer, comment

'''#################

# QSNO 102070

'''##################
from refactory.latter_M113_04.Q_102070.calculations import generate_problem
from refactory.latter_M113_04.Q_102070.utils import format_term, format_constant_term, clean_combined_expression

def latterandexpress_StemM113_04_011():
    """Generate and solve the problem."""
    problem_data = generate_problem()
    c_numerator = problem_data["c_numerator"]
    c_denominator = problem_data["c_denominator"]
    f_numerator = problem_data["f_numerator"]
    f_denominator = problem_data["f_denominator"]
    a = problem_data["a"]
    b = problem_data["b"]
    d = problem_data["d"]
    e = problem_data["e"]
    g = problem_data["g"]
    u = problem_data["u"]
    c_term_x = problem_data["c_term_x"]
    c_term_constant = problem_data["c_term_constant"]

    # Problem statement
    stem = f"도로 위의 네 장소 A, B, C, D가 있습니다.\n"
    stem += f"A에서 C까지의 거리는 \\( ({a}x + {b}) \\) \\( m \\), "
    stem += f"A에서 D까지의 거리는 \\( \\frac{{{c_numerator}}}{{{c_denominator}}}({d}x + {e}) \\) \\( m \\), "
    stem += f"B에서 D까지의 거리는 \\( \\frac{{{f_numerator}}}{{{f_denominator}}}({g}x - {u}) \\) \\( m \\)입니다.\n"
    stem += "B에서 C까지의 거리를 \\( x \\)를 사용한 식으로 나타내시오.\n"

    # Calculations
    expanded = f"\\(= {format_term(c_numerator * d // c_denominator, 'x')} + {c_numerator * e // c_denominator} - {format_term(a, 'x')} - {b} \\)"
    final = f"\\(= {format_term(c_numerator * d // c_denominator - a, 'x')} {format_constant_term(c_numerator * e // c_denominator - b)} \\)"

    # Answer
    answer = f"(정답) {clean_combined_expression(final)} \\( m \\)\n"

    # Explanation
    comment = "(해설)\n"
    comment += f"(A에서 D까지의 거리 - A에서 C까지의 거리): \\( {expanded} \\)\n"
    comment += f"결과: \\( {clean_combined_expression(final)} \\)\n"

    return stem, answer, comment


