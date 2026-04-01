def main(n):
    ans = 0.23

    if n >= 1:
        return (main(n - 1) ** 2 + main(n - 1)) / 95
    else:
        return ans
