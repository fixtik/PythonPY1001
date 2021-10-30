import collections
from collections import Counter

if __name__ == "__main__":
    main_str = """
        Данное предложение будет разбиваться на отдельные слова. 
        В качестве разделителя для встроенного метода split будет выбран символ пробела. На выходе мы получим список отдельных слов. 
        Далее нужно отсортировать слова в алфавитном порядке, а после сортировки склеить их с помощью метода строк join. Приступим!!!!
    """
def create_dict(str_):
    str_1 = str_.lower()
    main_set = set(str_1)
    dict_ = {i : 0 for i in main_set}
    for i in str_1:
         dict_[i] += 1
    return dict_

def create_alpha_str(str_):
    str_1 = str_.lower()
    str_2 = ''
    for i in str_1:
        if i.isalpha():
            str_2 += i
    return str_2

def create_alpha_dict(str_):
    main_set = set(str_)
    dict_ = {i: 0 for i in main_set}
    for i in str_:
        dict_[i] += 1
    return dict_

def create_with_counter(str_):
    return dict(collections.Counter(str_))

def percent_alpha(dict_):
    new_dict = {}
    for key in dict_:
        new_dict[key] = round((dict_[key] / len(dict_)) * 100, 2)
    return new_dict


print(create_dict(main_str))
str_temp = create_alpha_str(main_str)
print(percent_alpha(create_alpha_dict(str_temp)))
print(create_alpha_dict(str_temp))
print(create_with_counter(str_temp))