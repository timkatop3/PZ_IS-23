# Вапмант 8: Даны два целых числа: А, В. Проверить истинность высказывания: «Каждое из чисел
# АиВ нечетное»
try:
    a = int(input())
    b = int(input())

    if a % 2 != 0 and b % 2 != 0:
        print(True)
    else:
        print(False) 
except ValueError:
    print('Only decimal')





