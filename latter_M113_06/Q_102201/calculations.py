from fractions import Fraction

def verify_equation(eq, x_value):
    """Verify if the equation is satisfied for a given x value."""
    if eq == "\\(2x + 2 = x\\)":
        return 2 * x_value + 2 == x_value
    elif eq == "\\(x - 4 = 2\\)":
        return x_value - 4 == 2
    elif eq == "\\(3x + 5 = x - 9\\)":
        return 3 * x_value + 5 == x_value - 9
    elif eq == "\\(4(x - 1) = x + 7\\)":
        return 4 * (x_value - 1) == x_value + 7
    elif eq == "\\(6 - 5x = 2x - 8\\)":
        return 6 - 5 * x_value == 2 * x_value - 8
    elif eq == "\\(3x - 1 = x + 3\\)":
        return 3 * x_value - 1 == x_value + 3
    elif eq == "\\(2(x + 3) = 3x - 4\\)":
        return 2 * (x_value + 3) == 3 * x_value - 4
    elif eq == "\\(4x - 7 = x + 2\\)":
        return 4 * x_value - 7 == x_value + 2
    elif eq == "\\(5x + 2 = 2x + 11\\)":
        return 5 * x_value + 2 == 2 * x_value + 11
    elif eq == "\\(7 - 2x = 3x - 14\\)":
        return 7 - 2 * x_value == 3 * x_value - 14
    return False