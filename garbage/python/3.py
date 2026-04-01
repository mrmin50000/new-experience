import math


def main(b, n, m):
    ans = 0
    for j in range(1, m + 1):
        for i in range(1, n + 1):
            for k in range(1, b + 1):
                ans += math.ceil(i) ** 6 + 76 * k ** 2 + j ** 3
    return ans
