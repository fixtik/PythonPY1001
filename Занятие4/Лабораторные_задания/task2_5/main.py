if __name__ == "__main__":
    # Write your solution here
    def task_(n):
        n_list = [i for i in str(n)]
        return True if n_list == n_list[::-1] else False

    print(task_(12321))
