def rasklad(n):
    res_list = []
    i = 2
    if n == 1:
        res_list.append(n)
        return res_list
    while True:
        if n % i == 0 and n / i != 1:
            res_list.append(i)
            n //= i
        elif n / i == 1:
            res_list.append(i)
            return res_list
        else:
            i += 1

if __name__ == "__main__":
    # Write your solution here
    print(rasklad(63))
