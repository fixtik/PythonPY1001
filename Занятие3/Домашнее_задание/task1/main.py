def get_num():
    list_num = []
    while True:
        try:
            x = int(input('Введите число (для окончания - введите отрицательное число): '))
            if x < 0:
                return list_num
            elif 3 <= x <= 13:
                print('Чило в заданном диапазоне')
                list_num.append(x)
            else:
                print('Чило вне заданного диапазона')
        except ValueError:
            print('Вводите число, а не символ.')

if __name__ == "__main__":
    # Write your solution here
    print(get_num())
