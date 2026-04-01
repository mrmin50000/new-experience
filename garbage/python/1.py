import math


def main(z, y, x):
    a = math.sqrt(x ** 7 + 23 * (y - 3 * z ** 3) ** 2)
    b = math.ceil(x ** 3 + y ** 2) ** 4
    c = math.acos(z) ** 6
    return a + b - c

