def pow_func(base, pow_=2):
    # base ** pow_ -> реализовать через цикл while
    a = 1
    res = 1
    while a <= pow_:
        res *= base
        a += 1
    return res # TODO


if __name__ == "__main__":
    a = 2
    n = 6

    print(pow_func(a, n))
