# 아래 라이브러리를 로컬 서버로 반드시 추가해주세요
import random
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np
import math
import io
# import sympy as sp
from fractions import Fraction
import sys

# # Dictionary.html_function의 파일 경로 설정
# # 예: "C:/path/to/your/module"
# module_path = "/home/aig/aig2/directDownload/html_function.py"  # 실제 파일 경로로 변경하세요
# if module_path not in sys.path:
#     sys.path.append(module_path)

from Dictionary.html_function import *

# # 이제 Dictionary.html_function을 불러옵니다
# from Dictionary.html_function import *

	# 이미지 로드 함수
def load_img(file_path):
	img = mpimg.imread(file_path)
	return img

# SVG 적용 함수 (08/06 변경)
def save_svg_resize(ratio = 60):
    # ratio : 그림 확대 / 축소를 위한 파라미터, 기본값 100      
    file = io.StringIO()
    plt.savefig(file, format='svg', dpi=300, bbox_inches='tight', pad_inches=0.1) # Additional option to remove the rest parts
    file.seek(0)
    svg_data = file.getvalue()
    svg_data = svg_data.replace('<svg ', f'<svg width="{ratio}%" height="{ratio}%"  ') # style="display: block; margin: auto;"
    return svg_data

'''#########################

# QSNO 101200

'''#########################

from .refactory.intan_M112_06.Q_101200.calculations import *
from .refactory.intan_M112_06.Q_101200.utils import *

def intandrationalMM112_Stem_06_001():
   base_path = 'Middle/Grade1_1/img/'
   img_name = 'intandrationalMM112_Stem_06_001'
   img = load_img(base_path + img_name + '.png')
   coordinates = [(32, 75), (185, 74), (263, 74)]

   left_move, right_move, net_move = generate_moves()
   options, correct_answer = generate_options(left_move, right_move, net_move)

   stem = "다음 그림으로 설명할 수 있는 계산식은?"
   options_text = "\n".join([f"① \\({options[0]}\\)", f"② \\({options[1]}\\)", f"③ \\({options[2]}\\)", f"④ \\({options[3]}\\)", f"⑤ \\({options[4]}\\)"])
   stem += f"\n\n{options_text}"

   answer_index = options.index(correct_answer) + 1
   answer_symbol = ["①", "②", "③", "④", "⑤"][answer_index - 1]
   answer = f"(정답) {answer_symbol}"

   comment = (f"(해설) 주어진 그림은 원점에서 왼쪽으로 \\({abs(left_move)}\\)만큼 이동한 다음"
             f" 다시 오른쪽으로 \\({right_move}\\)만큼 이동한 것이 원점에서 오른쪽으로 \\({net_move}\\)만큼 이동한 것과 같음을 나타내므로"
             f" \\({left_move} + (+{right_move}) = {net_move}\\)")

   img_coord = add_coordinates_to_image(img, coordinates, left_move, right_move, net_move)
   svg = save_svg_resize(70)
   plt.close()

   return stem, answer, comment, svg


'''#########################

# QSNO 101201

'''#########################

from .refactory.intan_M112_06.Q_101201.utils import *


def intandrationalMM112_Stem_06_002():
   expression_types = ['integer', 'fraction', 'decimal']
   correct_type = random.choice(expression_types)
   
   if correct_type == 'integer':
       a, b, result, correct_answer, explanation = generate_integer_expression()
   elif correct_type == 'fraction':
       a, b, result, correct_answer, explanation = generate_fraction_expression()
   else:
       a, b, result, correct_answer, explanation = generate_decimal_expression()

   options = [correct_answer]
   explanations = [explanation]

   while len(options) < 5:
       wrong_type = random.choice(expression_types)
       if wrong_type == 'integer':
           _, _, _, wrong_answer, wrong_explanation = generate_integer_expression()
       elif wrong_type == 'fraction':  
           _, _, _, wrong_answer, wrong_explanation = generate_fraction_expression()
       else:
           _, _, _, wrong_answer, wrong_explanation = generate_decimal_expression()
           
       if wrong_answer not in options:
           options.append(wrong_answer)
           explanations.append(wrong_explanation)

   original_options = options[:]
   random.shuffle(options)
   
   stem = "다음 중 옳은 것은?\n\n"
   stem += "\n".join([f"{['①', '②', '③', '④', '⑤'][i]} {options[i]}" for i in range(5)])
   
   answer_index = options.index(correct_answer)
   answer = f"(정답) {['①', '②', '③', '④', '⑤'][answer_index]}"
   
   ordered_explanations = [f"{['①', '②', '③', '④', '⑤'][i]} {explanations[original_options.index(options[i])]}" for i in range(5)]
   comment = "(해설)\n" + "\n".join(ordered_explanations)

   return stem, answer, comment



'''#########################

# QSNO 101202

'''#########################


from .refactory.intan_M112_06.Q_101202.calculations import *
from .refactory.intan_M112_06.Q_101202.utils import *

def intandrationalMM112_Stem_06_003():
   number_options = ["3/2", "-1", "-5/4", "11/6", "-5/3", "7/4", "-3/2", "2/3", "-4/3", "5/6"]
   selected_numbers = random.sample(number_options, 5)
   
   mathjax_numbers = [format_number_to_mathjax(num) for num in selected_numbers]
   mathjax_numbers_for_abs = [format_number_to_mathjax_abs(num) for num in selected_numbers]
   
   values = {num: Fraction(num) if '/' in num else Fraction(int(num)) for num in selected_numbers}
   a = min(selected_numbers, key=lambda x: values[x])
   b = max(selected_numbers, key=lambda x: abs(values[x]))
   
   result = values[a] + values[b]
   
   options = [result]
   while len(options) < 5:
       wrong_answer = Fraction(random.randint(-10, 10), random.randint(1, 10))
       if wrong_answer != result and wrong_answer not in options:
           options.append(wrong_answer)
           
   random.shuffle(options)
   options_latex = []
   for opt in options:
       if opt.denominator == 1:
           options_latex.append(f"\\({opt.numerator}\\)" if opt.numerator >= 0 else f"\\(-{abs(opt.numerator)}\\)")
       else:
           options_latex.append(f"\\(\\frac{{{abs(opt.numerator)}}}{{{opt.denominator}}}\\)" 
                              if opt.numerator >= 0 else f"\\(-\\frac{{{abs(opt.numerator)}}}{{{opt.denominator}}}\\)")
   
   stem = "다음 수 중에서 가장 작은 수를 \\(a\\), 절댓값이 가장 큰 수를 \\(b\\)라 할 때, \\(a+b\\)의 값을 구하시오.\n\n"
   text_list = mathjax_numbers
   box_stem = make_box_stem(text_list, type=1, mark_title=True, col_count=5)
   stem += insert_html_code(box_stem)
   
   stem += f"\n① {options_latex[0]}  ② {options_latex[1]}  ③ {options_latex[2]}  ④ {options_latex[3]}  ⑤ {options_latex[4]}  "
   
   correct_index = options.index(result)
   answer = f"(정답) {['①', '②', '③', '④', '⑤'][correct_index]}"
   
   sorted_values = sorted(selected_numbers, key=lambda x: values[x])
   abs_sorted_values = sorted(selected_numbers, key=lambda x: abs(values[x]))
   
   lcm_denominator = lcm(values[a].denominator, values[b].denominator)
   numerator1 = values[a].numerator * (lcm_denominator // values[a].denominator)
   numerator2 = values[b].numerator * (lcm_denominator // values[b].denominator)
   
   explane_latex1 = f"\\frac{{{numerator1}}}{{{lcm_denominator}}}" if numerator1 >= 0 else f"-\\frac{{{abs(numerator1)}}}{{{lcm_denominator}}}"
   explane_latex2 = f"\\frac{{{numerator2}}}{{{lcm_denominator}}}" if numerator2 >= 0 else f"-\\frac{{{abs(numerator2)}}}{{{lcm_denominator}}}"
   
   result_numerator = numerator1 + numerator2
   result_latex = generate_fraction_components(result_numerator, lcm_denominator)
   
   explanation_steps = [
       "{} 이므로".format(" \\(\\lt\\) ".join([format_number_to_mathjax(num) for num in sorted_values])),
       f"가장 작은 수 \\(a =\\) {format_number_to_mathjax(sorted_values[0])}",
       "{} 이므로".format(" \\(\\lt\\) ".join([mathjax_numbers_for_abs[selected_numbers.index(num)] for num in abs_sorted_values])),
       f"절대값이 가장 큰 수 \\(b = \\) {format_number_to_mathjax(b)}",
       f"따라서, \\(a + b = \\){format_number_to_mathjax(sorted_values[0])} \\(+\\) {format_number_to_mathjax(abs_sorted_values[-1])}"
       f"\\( = {explane_latex1} + {explane_latex2} \\)"
       f"\\(=\\) \\({result_latex}\\)"
   ]
   
   comment = f"(해설)\n" + "\n".join(explanation_steps)
   return convert_mathjax(stem, answer, comment)


