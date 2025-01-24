import random

def generate_random_constants():
    """Generate random constants for the equations."""
    a = random.randint(2, 10)
    b = random.randint(1, 8)
    c = random.randint(2, 7)
    d = random.randint(2, 6)
    e = random.randint(3, 8)
    f = random.randint(2, 5)
    g = random.randint(4, 9)
    h = random.randint(1, 6)
    return a, b, c, d, e, f, g, h

def answer_labels():
    """Return the answer label mapping for options."""
    return {
        0: "①",
        1: "②",
        2: "③",
        3: "④",
        4: "⑤",
        5: "⑥",
        6: "⑦",
        7: "⑧"
    }