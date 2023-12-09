# Даны два пелых числа А иВ (А < В). Найти сумму квадратов всех целых чисел от А
# до В включительно.

c = 0

try:
    a = int(input())
    b = int(input())

    for i in range(a, b+1):
        c = c + i**2
    print(c)

except ValueError:
    print('Only decimal')