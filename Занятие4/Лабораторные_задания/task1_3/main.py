if __name__ == "__main__":
    # Write your solution here
    list_ = [i for i in range(0,9)]

    def task(list_1):
        return len([a for a in list_1 if a % 2 == 0])

print(task(list_))