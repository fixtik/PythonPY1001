if __name__ == "__main__":
    # Write your solution here
    def task_(n):
        return True if (len(set(str(n))) != len(str(n))) else False

    print(task_(123))