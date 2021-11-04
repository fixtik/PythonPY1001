import random
from collections import Counter
#Напишите функцию change(lst), которая принимает список и меняет
# местами его первый и последний элемент.
#В исходном списке минимум 2 элемента.


def change(lst):
    lst[0], lst[-1] = lst[-1], lst[0]
    return lst
list_ = list(range(10))
print(list_, change(list_))

#2. Функция to_list() принимает неограниченное количество параметров.
#Обработайте их так, чтобы на выходе получить список из этих элементов.

def to_list(*args):
    return list(args)

print(to_list(1,2,3,4,5,67,'',7))

#3. Требуется создать функцию list_sort(lst), которая сортирует список чисел по убыванию их абсолютного значения.

def list_sort(lst):

    lst.sort(key=abs, reverse=True)
    return lst

list_ = list(random.randint(-40, 40) for i in range(10))
print(list_sort(list_))

#4. На входе имеем список строк разной длины.
#Необходимо написать функцию all_eq(lst), которая вернет новый список из строк одинаковой длины.
#Длину итоговой строки определяем исходя из самой большой из них.
#Если конкретная строка короче самой длинной, дополнить ее нижними подчеркиваниями с правого края до требуемого количества символов.
#Расположение элементов начального списка не менять.

# def all_eq(lst):
#     lst_new = []
#     max_length = 0
#     for i in range(len(lst)):
#         if max_length < len(lst[i]):
#             max_length = len(lst[i])
#
#     def inc_len_str(str_):
#         if len(str_) < max_length:
#             str_1 = str_.ljust(max_length, "_")
#         else:
#             str_1 = str_
#         return str_1
#
#     lst_new = list(map(inc_len_str, lst))
#     return lst_new

def all_eq(lst: list) -> list:
    max_len = len(max(lst, key=lambda x: len(x)))
    return [item.ljust(max_len,'_') for item in lst]

stri = 'Люблю тебя Петра творенье'

print(all_eq((stri).split()))



#5. Напишите функцию to_dict(lst), которая принимает аргумент в
#виде списка и возвращает словарь, в котором каждый элемент списка является и ключом и значением.
#Предполагается, что элементы списка будут соответствовать правилам задания ключей в словарях.


def to_dict(lst):
    return {key: key for key in lst}

lst = ['1', '2', '4', '5']
print(to_dict(lst))



#6. Дана строка в виде случайной последовательности чисел от 0 до 9.
#Требуется создать словарь, который в качестве ключей будет принимать данные числа
#(т. е. ключи будут типом int), а в качестве значений – количество этих чисел в имеющейся последовательности.
#Для построения словаря создайте функцию count_it(sequence),
#принимающую строку из цифр. Функция должна возвратить словарь из 3-х самых часто встречаемых чисел.

str_ = '098756411912409887'

def count_it(sequence: str):
    dic_ = {int(item): sequence.count(item) for item in sequence}
    return dict(sorted(dic_.items(), key=lambda x: x[1], reverse=True)[:3])

print(count_it(str_))


# 7. Напишите функцию search_substr(subst, st), которая принимает 2 строки и определяет,
# имеется ли подстрока subst в строке st.
# В случае нахождения подстроки, возвращается фраза «Есть контакт!», а иначе «Мимо!».
# Должно быть найдено совпадение независимо от регистра обеих строк.

def search_substr(subst : str, st: str):
    return "Есть контакт!" if subst.lower() in st.lower() else "Мимо!"

print(search_substr("абв", "аВАбвгдей ка"))
print(search_substr("абв1", "аВАбвгдей ка"))

# 8. Требуется определить индексы первого и последнего вхождения буквы в строке.
# Для этого нужно написать функцию first_last(letter, st), включающую 2 параметра:
# letter – искомый символ, st – целевая строка.
# В случае отсутствия буквы в строке, нужно вернуть кортеж (None, None),
# если же она есть, то кортеж будет состоять из первого и последнего индекса этого символа.

def first_last(letter, st : str) -> tuple:
    try:
        return (st.index(letter), st.index(letter,-1))
    except ValueError:
        return (None,None)

def first_last_(letter, st : str) -> tuple:
    return (st.find(letter), st.find(letter,-1))

print(first_last('а', "аВАбвгдей ка"))
print(first_last('v', "аВАбвгдей ка"))

print(first_last_('а', "аВАбвгдей ка"))
print(first_last_('v', "аВАбвгдей ка"))

# 9. На вход функция more_than_five(lst) получает список из целых чисел.
# Результатом работы функции должен стать новый список, в котором
# содержатся только те числа, которые больше 5 по модулю.

def more_than_five(lst: list) -> list:
    return [item for item in lst if abs(item) > 5]

lst = list(random.randint(-40,40) for _ in range(10))
print(lst)
print(more_than_five(lst))