import random
from fractions import Fraction
from Dictionary.html_function import *
import matplotlib.pyplot as plt
import io
import math
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import sys

module_path = "/home/aig/aig2/directDownload/html_function.py"  # 실제 파일 경로로 변경하세요
if module_path not in sys.path:
    sys.path.append(module_path)

from Dictionary.html_function import *

# 이미지 로드 함수
def load_img(file_path):
    img = plt.imread(file_path)
    return img

# SVG 저장 함수
def save_svg():
    file = io.StringIO()
    plt.savefig(file, format='svg', dpi=300, bbox_inches='tight', pad_inches=0.01)
    file.seek(0)
    svg_data = file.getvalue()
    return svg_data

'''

# QSNO 102200

'''

from .refactory.latter_M113_06.Q_102200.utils import generate_random_constants, answer_labels
from .refactory.latter_M113_06.Q_102200.calculations import generate_equations, verify_equation

def latterandexpressMM113_Stem_06_001():
    answer_dict = answer_labels()

    while True:
        # Step 1: 랜덤 변수 설정
        x_value = random.choice([-1, 1])  # x값을 -1 또는 1 중에서 랜덤하게 선택
        constants = generate_random_constants()
        equations = generate_equations(x_value)

        # 방정식 랜덤 선택 (5개)
        selected_indices = random.sample(range(len(equations)), 5)
        selected_equations = [equations[i] for i in selected_indices]

        # Step 2: 문제 생성
        stem = f"다음 중 해가 \\(x = {x_value}\\)인 방정식은?\n\n"
        for i in range(5):
            stem += f"{answer_dict[i]} {selected_equations[i]}\n"

        # Step 3: 정답 및 해설
        solutions = [verify_equation(idx, x_value, constants) for idx in selected_indices]
        correct_indices = [i for i, is_solution in enumerate(solutions) if is_solution]

        # 최소 1개 이상의 정답이 있는지 확인
        if len(correct_indices) > 0:
            break

    answer = f"(정답) {', '.join(answer_dict[i] for i in correct_indices)}"

    # 해설 생성
    comment = "(해설)\n"
    for i, equation in enumerate(selected_equations):
        if solutions[i]:
            comment += f"{answer_dict[i]} {equation}에서 \\(x = {x_value}\\)를 대입하면 만족합니다.\n"
        else:
            comment += f"{answer_dict[i]} {equation}에서 \\(x = {x_value}\\)를 대입하면 만족하지 않습니다.\n"

    return stem, answer, comment


'''

# QSNO 102201

'''

from .refactory.latter_M113_06.Q_102201.utils import generate_answer_dict, generate_random_x_value, generate_random_equations
from .refactory.latter_M113_06.Q_102201.calculations import verify_equation

def latterandexpressMM113_Stem_06_002():
    all_equations = [
        "\\(2x + 2 = x\\)",
        "\\(x - 4 = 2\\)",
        "\\(3x + 5 = x - 9\\)",
        "\\(4(x - 1) = x + 7\\)",
        "\\(6 - 5x = 2x - 8\\)",
        "\\(3x - 1 = x + 3\\)",
        "\\(2(x + 3) = 3x - 4\\)",
        "\\(4x - 7 = x + 2\\)",
        "\\(5x + 2 = 2x + 11\\)",
        "\\(7 - 2x = 3x - 14\\)"
    ]

    answer_dict = generate_answer_dict()
    x_value = generate_random_x_value([-2, 2, 6])
    base_equations, shuffled_equations = generate_random_equations(all_equations)

    stem = (
        f"다음 방정식 중 \\(x = {x_value}\\)가 해인 것은?\n\n"
        + "\n".join([f"{answer_dict[i]} {eq}" for i, eq in enumerate(shuffled_equations)])
    )

    # 선택된 방정식들의 검증 결과
    solutions = [verify_equation(eq, x_value) for eq in shuffled_equations]
    correct_indices = [i for i, is_correct in enumerate(solutions) if is_correct]

    # 정답 및 해설 생성
    answer = f"(정답) {', '.join([answer_dict[i] for i in correct_indices])}"
    comment = "(해설)\n" + "\n".join([
        f"{answer_dict[i]} {eq}는 {'만족합니다' if solutions[i] else '만족하지 않습니다'}."
        for i, eq in enumerate(shuffled_equations)
    ])

    return stem, answer, comment


'''

# QSNO 102202

'''
import random
from .refactory.latter_M113_06.Q_102202.utils import generate_random_x_range, generate_random_equations, shuffle_and_label_equations, generate_answer_dict
from .refactory.latter_M113_06.Q_102201.calculations import verify_equation

def latterandexpressMM113_Stem_06_003():
    while True:
        # Step 1: Generate x range and equations
        x_range, range_description = generate_random_x_range()
        x_value = random.choice(x_range)
        
        all_equations = generate_random_equations()
        base_equations = random.sample(all_equations, 5)
        equations = shuffle_and_label_equations(base_equations)
        
        # Answer dictionary for labeling options
        answer_dict = generate_answer_dict()
        
        # Identify equation with no solution
        no_solution_eq = "\\(\\frac{1}{2}x + 3 = 2\\)"
        correct_answer = equations.index(no_solution_eq)

        # Step 2: Generate question stem
        stem = f"x가 {range_description}일 때, 다음 방정식 중 해가 없는 것은?\n\n"
        for i, eq in enumerate(equations):
            stem += f"{answer_dict[i]} {eq}\n"

        # Step 3: Generate answer and explanation
        answer = f"(정답) {answer_dict[correct_answer]}"
        comment = f"(해설)\nx가 {range_description}이므로\n"
        
        for i, eq in enumerate(equations):
            comment += f"{answer_dict[i]} {eq}에서\n"
            x_values = x_range.copy()
            has_solution = False
            
            for x in x_values:
                if verify_equation(eq, x):
                    comment += f"   x = {x}일 때 성립함\n"
                    has_solution = True
                    break
            
            if not has_solution:
                comment += "   주어진 범위의 모든 x값을 대입해도 성립하지 않음\n"
                comment += "   따라서 해가 없다.\n"

        return stem, answer, comment