import random

def generate_random_x_range():
    range_type = random.choice(['range1', 'range2'])
    if range_type == 'range1':
        return [-1, 0, 1, 2], "\\(-1\\) 이상 \\(3\\) 미만의 정수"
    else:
        return [-3, -2, -1, 0, 1, 2], "\\(-3\\) 이상 \\(3\\) 미만의 정수"

def generate_random_equations():
    return [
        "\\(4x - 7 = -3\\)",
        "\\(\\frac{1}{2}x + 3 = 2\\)",
        "\\(4(x + 1) = 6x\\)",
        "\\(5x - 6 = 3(2x - 2)\\)",
        "\\(-5 - (2x - 3) = 0\\)",
        "\\(3x + 2 = x - 4\\)",
        "\\(2(x - 1) = 4x - 6\\)",
        "\\(\\frac{x}{3} + 2 = -1\\)",
        "\\(7x - 4 = 3(2x + 1)\\)",
        "\\(-2(x + 3) = 4 - x\\)"
    ]

def shuffle_and_label_equations(equations):
    shuffled = equations.copy()
    random.shuffle(shuffled)
    return shuffled

def generate_answer_dict():
    return {
        0: "①",
        1: "②",
        2: "③",
        3: "④",
        4: "⑤"
    }