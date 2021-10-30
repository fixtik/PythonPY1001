if __name__ == "__main__":
    # Write your solution here
    def task_(n, m):
        return [i ** 2 for i in range(n,m+1) if i % 2 != 0]

    print(task_(1,9))