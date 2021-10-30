if __name__ == "__main__":
    # Write your solution here
    N = 812345
    n_list = [int(i) for i in str(N)]

    print(n_list)
    print(sum(n_list))
    print(sum([i for i in n_list if i % 2 == 0]))
    print(len(n_list))
    print(f'min {min(n_list)} max {max(n_list)}')
    print([i for i in n_list if i % 2 != 0])
    print(n_list[0] - n_list[-1])

    print (min(n_list), n_list.index(min(n_list)))