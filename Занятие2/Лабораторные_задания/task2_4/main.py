if __name__ == "__main__":
    # постарайтесь не использовать "магические" числа,
    # а по возможности дать переменным осмысленные названия и использовать их
    # TODO Распечатать строку лесенкой
    tab_ = 5
    str_ = "Hello,world"

    for i in range(len(str_)):
        print(' ' * (tab_ + i), str_[i])