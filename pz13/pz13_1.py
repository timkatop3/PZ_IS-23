#В матрице найти максимальный положительный элемент, кратный 4.
import random
arr = [[random.randint(1,10) for i in range(3)] for i in range(3)]

print('изначальная матрица:')
for i in arr:
    print(i)

matrix = [element for row in arr for element in row]

man = filter(lambda x: x %  4== 0 and x > 0, matrix)


print('максмальный положительный эллемен кратный 4:',max(man))