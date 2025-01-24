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


# QSNO 102220
def latterandexpressMM113_Stem_07_001():

	# 문제
	stem = (f"\n")
	stem += 'latterandexpressMM113_Stem_07_001'
	# 정답
	answer = "(정답) answer "

	# 해설
	comment = "(해설) \n "

	# 이미지 부분
	svg = "이미지 부분"

	return stem, answer, comment, svg

# QSNO 102221
def latterandexpressMM113_Stem_07_002():

	# 문제
	stem = (f"\n")
	stem += 'latterandexpressMM113_Stem_07_002'
	# 정답
	answer = "(정답) answer "

	# 해설
	comment = "(해설) \n "

	# 이미지 부분
	svg = "이미지 부분"

	return stem, answer, comment, svg

# QSNO 102222
def latterandexpressMM113_Stem_07_003():
   # 객관식 번호 딕셔너리 정의
   answer_dict = {
       0: "①",
       1: "②",
       2: "③",
       3: "④",
       4: "⑤"
   }

   while True:
       ###### Step 1. 문제 생성 부분 #####
       # 옳은 명제들 (고정)
       correct_statements = [
           {"premise": "\\(a = b\\)이면", "operation": "양변에 \\(4\\)를 더하면", "conclusion": "\\(a + 4 = b + 4\\)이다"},
           {"premise": "\\(a = b\\)이면", "operation": "양변에 \\(-1\\)을 곱하면", "conclusion": "\\(-a = -b\\)이다"},
           {"premise": "\\(a + 3 = b + 3\\)이면", "operation": "양변에서 \\(3\\)을 빼면", "conclusion": "\\(a = b\\)이다"},
           {"premise": "\\(a + 7 = b + 7\\)이면", "operation": "양변에서 \\(7\\)을 빼면", "conclusion": "\\(a = b\\)이다"},
           {"premise": "\\(5a = 5b\\)이면", "operation": "양변을 \\(5\\)로 나누면", "conclusion": "\\(a = b\\)이다"},
           {"premise": "\\(a - 2 = b - 2\\)이면", "operation": "양변에 \\(2\\)를 더하면", "conclusion": "\\(a = b\\)이다"},
           {"premise": "\\(2a + 4 = 2b + 4\\)이면", "operation": "양변에서 \\(4\\)를 빼면", "conclusion": "\\(2a = 2b\\)이다"},
           {"premise": "\\(a^2 = b^2\\)이면", "operation": "양변을 제곱근으로 나누면", "conclusion": "\\(a = b\\) 또는 \\(a = -b\\)이다"}
       ]

       # 옳지 않은 명제들 (2개)
       # 보인 변경(24/12/11) - 1번째 operation 9를 곱하면 -> 6을 곱하면
       incorrect_statements = [
           {"premise": "\\(\\frac{a}{3} = \\frac{b}{2}\\)이면", "operation": "양변에 \\(6\\)를 곱하면", "conclusion": "\\(3a = 2b\\)이다", "correct": "\\(2a = 3b\\)이다"},
           # 보인 변경(24/12/11) 틀린 해설로 제외
        #    {"premise": "\\(a = b\\)이면", "operation": "양변에 \\(2\\)를 더하면", "conclusion": "\\(2a = 2b\\)이다", "correct": "\\(a + 2 = b + 2\\)이다"} 
       ]

       # 옳지 않은 명제 하나 랜덤 선택
       wrong_statement = random.choice(incorrect_statements)

       # 모든 문항을 리스트로 만들고 옳지 않은 문항의 위치를 랜덤하게 선택
       all_statements = correct_statements.copy()
       wrong_position = random.randint(0, 4)  # 0부터 4까지의 랜덤한 위치
       all_statements.insert(wrong_position, wrong_statement)

       ###### Step 2. 문제 생성 #####
       stem = "다음 중 옳지 않은 것은?\n\n"
       for i in range(5):
           stem += f"{answer_dict[i]} {all_statements[i]['premise']} {all_statements[i]['conclusion']}\n"

       ###### Step 3. 정답 및 해설 생성 #####
       answer = f"(정답) {answer_dict[wrong_position]}"

       comment = "(해설)\n"
       for i in range(5):
           stmt = all_statements[i]
           if i == wrong_position:
               comment += f"{answer_dict[i]} {stmt['premise']} {stmt['operation']} {stmt['correct']}\n"
           else:
               comment += f"{answer_dict[i]} {stmt['premise']} {stmt['operation']} {stmt['conclusion']}\n"

       return stem, answer, comment


# QSNO 102223
def latterandexpressMM113_Stem_07_004():
    # 객관식 번호 딕셔너리
    answer_dict = {
        0: "①",
        1: "②",
        2: "③",
        3: "④",
        4: "⑤"
    }
    while True:
        ###### Step 1. 랜덤 변수 설정 #####
        # 각 보기별 랜덤 변수 설정
        num1 = random.randint(2, 5)  # 1번 보기의 숫자 범위: 2~5
        num2 = random.randint(4, 6)  # 2번 보기의 숫자 범위: 4~6
        num3 = random.randint(2, 5)  # 3번 보기의 숫자 범위: 2~5
        num4 = random.randint(1, 3)  # 4번 보기의 숫자 범위: 1~3
        num5 = random.randint(5, 9)  # 5번 보기의 숫자 범위: 5~9
        
        # 방정식 리스트 생성 (이항 결과 수정)
        base_equations = [
            {"before": f"\\({num1}x + 2 = {num1}\\)", "after": f"\\({num1}x = {num1} - 2\\)", "correct": True},
            {"before": f"\\(-2x = 4x + {num2}\\)", "after": f"\\(-2x - 4x = {num2}\\)", "correct": False},  # 부호 오류
            {"before": f"\\(5x + 1 = {num3} - x\\)", "after": f"\\(5x + x = {num3} - 1\\)", "correct": True},
            {"before": f"\\(9x + {num4} = -7x\\)", "after": f"\\(9x + 7x = -{num4}\\)", "correct": True},
            {"before": f"\\(x + {num5} = 10x - 1\\)", "after": f"\\(x - 10x = -1 - {num5}\\)", "correct": True}
        ]

        # 방정식 리스트를 랜덤하게 섞기
        equations = base_equations.copy()
        random.shuffle(equations)

        # 섞인 후의 원래 방정식 인덱스 찾기
        shuffled_indices = [base_equations.index(eq) for eq in equations]

        # 정답 찾기 (올바른 이항을 한 것)
        correct_answer = [i for i, eq in enumerate(equations) if eq["correct"]][0]

        ###### Step 2. 문제 생성 #####
        stem = "다음 중 이항을 바르게 한 것은?\n\n"
        for i in range(5):
            stem += f"{answer_dict[i]} {equations[i]['before']} \\(\\rightarrow\\) {equations[i]['after']}\n"

        ###### Step 3. 정답 및 해설 생성 #####
        answer = f"(정답) {answer_dict[correct_answer]}"

        # 해설 생성 (보기 순서대로)
        comment = "(해설)\n"
        for i in range(5):
            eq = equations[i]  # 현재 보기의 방정식
            comment += f"{answer_dict[i]} {eq['before']}에서\n"
            
            if base_equations.index(eq) == 0:
                comment += f"   2를 우변으로 이항하면 {eq['after']}"
            elif base_equations.index(eq) == 1:
                comment += f"   4x를 좌변으로 이항하면 부호가 바뀌어 -4x가 되므로 {eq['after']}은 틀림"
            elif base_equations.index(eq) == 2:
                comment += f"   1을 우변으로, -x를 좌변으로 이항하면 {eq['after']}"
            elif base_equations.index(eq) == 3:
                comment += f"   {num4}를 우변으로, -7x를 좌변으로 이항하면 {eq['after']}"
            elif base_equations.index(eq) == 4:
                comment += f"   {num5}를 우변으로, 10x를 좌변으로 이항하면 {eq['after']}"
            
            comment += "이다.\n"

        return stem, answer, comment

# QSNO 102224
def latterandexpressMM113_Stem_07_005():
    answer_dict = {
        0: "①",
        1: "②",
        2: "③",
        3: "④",
        4: "⑤"
    }
    while True:
        ###### Step 1. 랜덤 변수 설정 #####
        k = random.choice([2, 3, 4, 5])  # 계수
        b = random.choice([1, 2, 3])     # 상수항
        c = random.choice([2, 3, 4, 5])  # 우변

        # 기본 방정식
        base_eq = f"\\({k}a + {b} = {c}\\)"

        # 기본 방정식 리스트 생성
        base_equations = [
            {"eq": f"\\({k}a - {b} = 0\\)",
             "explanation": f"\\({k}a + {b} = {c}\\)의 양변에서 \\({c}\\)를 빼면",
             "process": f"\\({k}a - {b} = 0\\)",
             "is_correct": True},
            
            {"eq": f"\\({k}a + {b+3} = {c+3}\\)",
             "explanation": f"\\({k}a + {b} = {c}\\)의 양변에 \\(3\\)을 더하면",
             "process": f"\\({k}a + {b+3} = {c+3}\\)",
             "is_correct": True},
             
            {"eq": f"\\({2*k}a + {2*b} = {2*c}\\)",
             "explanation": f"\\({k}a + {b} = {c}\\)의 양변에 \\(2\\)를 곱하면",
             "process": f"\\({2*k}a + {2*b} = {2*c}\\)",
             "is_correct": True},
             
            {"eq": f"\\(a + \\frac{{{b}}}{{{k}}} = \\frac{{{c}}}{{{k}}}\\)",
             "explanation": f"\\({k}a + {b} = {c}\\)의 양변을 \\({k}\\)로 나누면",
             "process": f"\\(a + \\frac{{{b}}}{{{k}}} = \\frac{{{c}}}{{{k}}}\\)",
             "is_correct": True},
             
            # 보인 변경(2024/12/11) - 해설 문구 자연스럽게 수정
            {"eq": f"\\(-{k}a + 1 = -2\\)",
             "explanation": f"\\({k}a + {b} = {c}\\)의 양변에 \\(-1\\)을 곱하면",
             "process": f"\\(-{k}a + 1 = -2\\)이고",
             "add_explanation": f"다시 양변에 \\(2\\)를 더하면 \\(-{k}a + 1 = 0\\)이다. \n따라서 원래 방정식과 다른 해를 가지므로",
             "is_correct": False}
        ]

        # 랜덤으로 4개의 올바른 방정식 선택
        correct_eqs = [eq for eq in base_equations if eq["is_correct"]]
        random.shuffle(correct_eqs)
        selected_correct_eqs = correct_eqs[:4]

        # 틀린 방정식 추가
        wrong_eq = [eq for eq in base_equations if not eq["is_correct"]][0]

        # 모든 방정식 합치고 섞기
        all_equations = selected_correct_eqs + [wrong_eq]
        random.shuffle(all_equations)

        # 틀린 방정식의 위치 찾기
        wrong_position = all_equations.index(wrong_eq)

        ###### Step 2. 문제 생성 #####
        stem = f"{base_eq}일 때, 다음 중 옳지 않은 것은?\n\n"
        for i in range(5):
            stem += f"{answer_dict[i]} {all_equations[i]['eq']}\n"

        ###### Step 3. 정답 및 해설 생성 #####
        answer = f"(정답) {answer_dict[wrong_position]}"
        comment = "(해설)\n"
        for i in range(5):
            comment += f"{answer_dict[i]} {all_equations[i]['explanation']}\n"
            comment += f" {all_equations[i]['process']}\n"
            if i == wrong_position:  # 틀린 답에 대한 추가 설명
                comment += f" {all_equations[i]['add_explanation']}\n"
                comment += " ∴ 옳지 않다.\n"

        return stem, answer, comment