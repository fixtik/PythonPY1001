if __name__ == "__main__":
    # Write your solution here
    def task(n):
        return True if len(set(str(n))) == 1 else False


print(task(111111))
