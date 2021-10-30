if __name__ == "__main__":
    # Write your solution here
    num = 2108

    n_str = set(str(num))

    if ('4' in n_str) and ('8' in n_str) or ('9' in n_str):
        print(True)
    else:
        print(False)