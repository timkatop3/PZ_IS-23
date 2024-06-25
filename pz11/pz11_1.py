# Средствами языка Python сформировать два текстовых файла (.txt), содержащих по одной
# последовательности из целых положительных и отрицательных чисел. Сформировать
# новый текстовый файл (.txt) следующего вида, предварительно выполнив требуемую
# обработку элементов:
# Содержимое первого файла:
# Четные элементы:
# Произведение четных элементов:
# Минимальный элемент:
# Содержимое второго файла:
# Нечетные элементы:
# Количество нечетных элементов:
# Сумма нечетных элементов:
a = [2, 3, 6, 1, 9, 12, 111, 54, 21, 146, 21, 7, 325]
b = []
c = []
for i in a:
    if i % 2 == 0:
        b.append(i)
    else:
        c.append(i)

with open('pz11/file1.txt', 'w') as file:
    for i in b:
        file.write(str(i))
        file.write(' ')
   
    
   

with open('pz11/file2.txt', 'w') as file:
    for i in c:
        file.write(str(i))
        file.write(' ')
    
    


file_1 = open('pz11/file1.txt', 'r')
file_1 = file_1.read()
file_1 = file_1.split()
b = []
for i in file_1:
    b.append(int(i))


file_2 = open('pz11/file2.txt', 'r')
file_2 = file_2.read()
file_2 = file_2.split()
c = []
for i in file_2:
    c.append(int(i))

with open('pz11/file_final.txt', 'w', encoding='utf-8') as file:
    file.write('произведение четных елментов:\n')
    file.write(str(b)+ '\n')
    file.write('четные элементы:\n')
    b1 = 1
    for y in b:
        b1 *= y
    file.write(str(b1)+ '\n')
    file.write('минимальный элемент:\n')
    file.write(str(min(b))) 
    
    
    file.write('нечетные элементы:\n')
    file.write(str(c)+ '\n')
    file.write('количество нечетные элементы:\n')
    file.write(str(len(c)) + '\n')
    file.write('сумма нечетные элементы:\n')
    file.write(str(sum(c)) + '\n')
    