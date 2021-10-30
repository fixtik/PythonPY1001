if __name__ == "__main__":
    # Write your solution here
    def task_(list_):
        return [item for item in list_ if item > sum(list_) / len(list_)]

print(task_([i for i in range(0,20)]))