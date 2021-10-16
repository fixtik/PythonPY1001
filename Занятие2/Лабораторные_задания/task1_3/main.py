A = int(input("Enter A: "))
B = int(input("Enter B: "))

if A ** 2 + B ** 2 > (A + B) ** 2:
    print("Больше сумма квадратов")
elif A ** 2 + B ** 2 < (A + B) ** 2:
    print('Больше квадрат суммы')
else:
    print("Они равны")