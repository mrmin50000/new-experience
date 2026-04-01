import math


def main(y, x, z):
    ans = 0
    n = len(y)
    for i in range(1, n + 1):
        ans += (
            46 * x[n - math.ceil(i / 2)] ** 2
            - y[n - i]
            - 93 * z[math.ceil(i / 2) - 1] ** 3
        ) ** 3
    return 45 * ans
