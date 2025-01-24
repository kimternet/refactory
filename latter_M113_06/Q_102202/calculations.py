def verify_equation(eq, x):
    if eq == "\\(4x - 7 = -3\\)":
        return x == 1
    elif eq == "\\(\\frac{1}{2}x + 3 = 2\\)":
        return False  # 항상 해가 없음
    elif eq == "\\(4(x + 1) = 6x\\)":
        return x == 2
    elif eq == "\\(5x - 6 = 3(2x - 2)\\)":
        return x == 0
    elif eq == "\\(-5 - (2x - 3) = 0\\)":
        return x == -1
    elif eq == "\\(3x + 2 = x - 4\\)":
        return x == -3
    elif eq == "\\(2(x - 1) = 4x - 6\\)":
        return x == 2
    elif eq == "\\(\\frac{x}{3} + 2 = -1\\)":
        return x == -9
    elif eq == "\\(7x - 4 = 3(2x + 1)\\)":
        return x == -1
    elif eq == "\\(-2(x + 3) = 4 - x\\)":
        return x == -2
    return False