#Дана строка-предложение с избыточными пробелами между словами.
#Преобразовать ее так, чтобы между словами был ровно один пробел.

s = input('Введите строку: ')
result = s.split()
print(" ".join(result))