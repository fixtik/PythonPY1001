
    # Write your solution here

size = int(input("Введите размер таблицы: "))
matrix = list([] for _ in range(1, size+1))

length = len(str(size ** 2)) + 3
width = len(str(size)) + 4

def matrix_fill(inner_m):
    return list(i for i in range(1, size+1))

matrix_ = list(map(matrix_fill, matrix))

num = list(range(size))

header = ' ' * width + ' ' + ''.join([str(j).rjust(length) for j in range(1, size+1)])
print(header)

for indx_i in range(len(matrix_)):
    print(f'{num[indx_i]+1:>5}', "|", end=' ')
    for indx_j in range(len(matrix_[0])):
        matrix_[indx_i][indx_j] = (indx_j + 1)  * (indx_i + 1)
        print(f'{matrix_[indx_i][indx_j]:>5}', end=' ')
    print()












