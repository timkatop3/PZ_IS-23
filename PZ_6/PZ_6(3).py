#Дан список размера N. Заменить каждый элемент списка на среднее арифметическое
#этого элемента и его соседей.
def Func():
    try:
        lst = list(map(int, input("Input list of INT:").split()))
        result = [] 
        result.append((lst[0] + lst[1]) / 2) 
        for i in range(1, len(lst) - 1):
            result.append((lst[i - 1] + lst[i] + lst[i + 1]) / 3)
        result.append((lst[-2] + lst[-1]) / 2) 
        print('Result:', result) 
    except ValueError:
        print('Only decimal')
Func()