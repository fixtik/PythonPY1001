def sum_list():
    def get_num():
        enter_list = []
        while True:
            try:
                b = int(input('Введите число для сложения: '))
                if b == 0:
                    return enter_list
                elif b < 0:
                    continue
                else:
                    enter_list.append(b)
            except ValueError:
                print('Введите число! Для окончания - 0')
    print(sum(get_num()))

if __name__ == "__main__":
    # Write your solution here
    sum_list()
