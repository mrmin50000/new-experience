import math


def main(z):
    if z < -23:
        return z ** 4 / 93
    elif z < 38:
        return 5 * z ** 10
    elif z < 92:
        return (9 + 37 * z ** 3) ** 3 / 90
    else:
        return 52 * math.log10(z ** 3 + 31)
