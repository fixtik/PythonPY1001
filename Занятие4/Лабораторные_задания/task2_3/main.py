if __name__ == "__main__":
    # Write your solution here
    pass
n = 1232999999999999999999

n_list = [int(i) for i in str(n)]

if len(str(sum(n_list))) == 2:
    print(True)
else:
    print(False)