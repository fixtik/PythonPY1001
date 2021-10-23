def func(epsilon=0.0001):
    znam = 2
    res = 0
    while (1 / znam) > epsilon:
        res += 1 / znam
        znam *= 2
    return res, znam

if __name__ == "__main__":
    print(func())
