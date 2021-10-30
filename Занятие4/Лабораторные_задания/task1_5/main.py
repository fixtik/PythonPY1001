if __name__ == "__main__":
    list_ = [4, -1, 10, -1, 3, -3, -6, 8, 6, 9]

if  len([item for item in list_ if item % 2 ==0]) > len([item for item in list_ if item % 2 !=0]):
     print('Четных')
else:
     print('Нечетных')