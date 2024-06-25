#Дан целочисленный список размера 10. Вывести все содержащиеся в данном списе
#четные числа в порядке убывания их индексов, а также их количество K.

def Func():
    try:
        lst = list(map(int, input("Input list of INT:").split()))
        even_indexes = []
        k = 0

        for i in range(len(lst)):
            if lst[i] % 2 == 0:
                even_indexes.append(i)

        even_indexes.sort(reverse=True)

        print("Even numbers:")
        for index in even_indexes:
            print(lst[index], end=" ")
    except ValueError:
        print('Only decimal')

Func()