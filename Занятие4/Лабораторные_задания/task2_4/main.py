if __name__ == "__main__":

    n = 3400

    n_list = [int(i) for i in str(n)]

    if sum(n_list) % 7 == 0:
        print(True)
    else:
        print(False)
