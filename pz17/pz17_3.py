# Задание предполагает, что у студента есть проект с практическими работами (№№ 2-13),
# оформленный согласно требованиям. Все задания выполняются c использованием модуля
# OS:
#  перейдите в каталог PZ11. Выведите список всех файлов в этом каталоге. Имена
# вложенных подкаталогов выводить не нужно.
#  перейти в корень проекта, создать папку с именем test. В ней создать еще одну папку
# test1. В папку test переместить два файла из ПЗ6, а в папку test1 - один файл из ПЗ7.
# Файл из ПЗ7 переименовать в test.txt. Вывести в консоль информацию о размере
# файлов в папке test.
#  перейти в папку с PZ11, найти там файл с самым коротким именем, имя вывести в
# консоль. Использовать функцию basename () (os.path.basename()).
#  перейти в любую папку где есть отчет в формате .pdf и «запустите» файл в
# привязанной к нему пр


#  перейдите в каталог PZ11. Выведите список всех файлов в этом каталоге. Имена
# вложенных подкаталогов выводить не нужно.

import os
print('-' * 100)
print("Пункт 1")

os.chdir("./pz11")  
files = [] 


for obj in os.listdir():

    if os.path.isfile(obj):

        files.append(obj)


print(files)


#  перейти в корень проекта, создать папку с именем test. В ней создать еще одну папку
# test1. В папку test переместить два файла из ПЗ6, а в папку test1 - один файл из ПЗ7.
# Файл из ПЗ7 переименовать в test.txt. Вывести в консоль информацию о размере
# файлов в папке test.

print('-' * 100)
print("Пункт 2")


os.chdir("..") 
os.mkdir("test")  # создаем папку test
os.mkdir("test/test1")  # создаем папку test1 внутри папки test

# копируем файлы из ПЗ6 в папку test
with open("./pz6/pz6.pdf", "rb") as src_file:
    with open("test/pz6.pdf", "wb") as dst_file:
        dst_file.write(src_file.read())

with open("./pz6/pz6_1.py", "r", encoding="utf-8") as src_file:
    with open("test/pz6_1.py", "w", encoding="utf-8") as dst_file:
        dst_file.write(src_file.read())

# копируем файл из ПЗ7 в папку test1 и переименовываем его в test.txt
with open("./pz7/pz7_1.py", "r", encoding="utf-8") as src_file:
    with open("test/test1/test.txt", "w", encoding="utf-8") as dst_file:
        dst_file.write(src_file.read())

# получаем размеры всех файлов в папке test
sizes = []
for file in os.listdir("test"):
    if os.path.isfile(os.path.join("test", file)):
        sizes.append(os.path.getsize(os.path.join("test", file)))

print(sizes)




#  перейти в папку с PZ11, найти там файл с самым коротким именем, имя вывести в
# консоль. Использовать функцию basename () (os.path.basename()).
print('-' * 100)

print("Пункт 3")



os.chdir("./pz11")

shortest_filename = ""
for filename in os.listdir():
    if len(filename) < len(shortest_filename) or shortest_filename == "":
        shortest_filename = filename

print(os.path.basename(shortest_filename))



print('-' * 100)
print("Пункт 4")



pdf_folder = './pz2'

pdf_filename = 'pz2.pdf'

pdf_path = os.path.join(pdf_folder, pdf_filename)

if os.path.isfile(pdf_path):
    # Открытие функции os.startfile()
    os.startfile(pdf_path)
else:
    print("такого файла нет")




print('-' * 100)
print("Пункт 5")


os.chdir = '../test/test1'

file_path = os.path.join(os.chdir, 'test.txt')

if os.path.isfile(file_path):
    # удаляем файл
    os.remove(file_path)
    print('Файл успешно удален.')
else:
    print('Файл не найден.')

print('-' * 100)