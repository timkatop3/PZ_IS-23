#Дан список размера N. Найти количество участков, на которых его элементы
#монотонно возрастают.

def Func(lst):
    count = 0
    increase = lst[0]
    for num in lst[1:]:
        if num > increase:
            increase = num
            count += 1
    print(count)
Func(list(map(int, input("Input list of INT:").split())))