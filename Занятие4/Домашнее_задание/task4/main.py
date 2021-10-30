if __name__ == "__main__":
    # Write your solution here
    def task_(n):
        n_l = [int(i) for i in str(n)]
        return True if sum(n_l[:3:1]) == sum(n_l[3::1]) else False

    print(task_(123133))