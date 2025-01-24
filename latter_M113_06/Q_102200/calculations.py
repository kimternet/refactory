from .utils import generate_random_constants, answer_labels

def generate_equations(x_value):
    """Generate a list of equations with random constants and x_value."""
    a, b, c, d, e, f, g, h = generate_random_constants()
    equations = [
        f"\\(x + {b} = {b + x_value}\\)",
        f"\\({a}x = {a * x_value}\\)",
        f"\\(\\frac{{x}}{{{c}}} = {x_value/c}\\)",
        f"\\({d}x + {e} = x + {d * x_value + e - x_value}\\)",
        f"\\({f}(x + {g}) = {h} - x\\)",
        f"\\({a}x - {b} = {a * x_value - b}\\)",
        f"\\(\\frac{{x + {c}}}{{{d}}} = {(x_value + c)/d}\\)",
        f"\\({e}x = {e * x_value}\\)"
    ]
    return equations

def verify_equation(idx, x_value, constants):
    """Verify if a given equation satisfies x_value."""
    a, b, c, d, e, f, g, h = constants
    x = x_value
    if idx == 0:
        return x + b == b + x_value
    elif idx == 1:
        return a * x == a * x_value
    elif idx == 2:
        return x / c == x_value / c
    elif idx == 3:
        return d * x + e == x + (d * x_value + e - x_value)
    elif idx == 4:
        return f * (x + g) == h - x
    elif idx == 5:
        return a * x - b == a * x_value - b
    elif idx == 6:
        return (x + c) / d == (x_value + c) / d
    elif idx == 7:
        return e * x == e * x_value
    return False