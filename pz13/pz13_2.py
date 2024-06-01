# В квадратной матрице все элементы, не лежащие на главной диагонали увеличить в
# 2 раза.
import random
arr = [[random.randint(1,10) for i in range(3)] for i in range(3)]
print(f'изначальная матрица: ')
for i in arr:
    print(i)

matrix = [[val * 2 if i != j else val for j, val in enumerate(row)] for i, row in enumerate(arr)]

print(f'увеличенная: ')
for i in matrix:
    print(i)
