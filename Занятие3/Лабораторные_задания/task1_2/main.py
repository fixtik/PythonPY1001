def factorial(n):
    i = 1
    res = 1
    while i <= n:
        res *= i
        i += 1
    return res

if __name__ == "__main__":

    print(factorial(5))
