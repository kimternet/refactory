import random

def generate_answer_dict():
    """Generate a dictionary for answer labels."""
    return {
        0: "①",
        1: "②",
        2: "③",
        3: "④",
        4: "⑤"
    }

def generate_random_x_value(possible_values):
    """Generate a random x value from the provided list."""
    return random.choice(possible_values)

def generate_random_equations(equations_list, count=5):
    """Generate a shuffled list of equations."""
    base_equations = random.sample(equations_list, count)
    shuffled_equations = base_equations.copy()
    random.shuffle(shuffled_equations)
    return base_equations, shuffled_equations