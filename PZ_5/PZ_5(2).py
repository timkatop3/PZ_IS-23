# Описать функцию AddLeftDigit(D, K). добавляющую к целому положительному
# числу К слева цифру D (D — входной параметр целого типа, лежащий в диапазоне
# 1-9, К — параметр целого типа, являющийся одновременно входным и выходным).
# С помощью этой функции последовательно добавить к данному числу К слева
# данные цифры D1 и D2, выводя результат каждого добавления.

def AddLeftDigit(K, D):
    K = D + K
    print(K)

    D = input('Введие число которое хотите добавить слева: ')

    K = D + K
    print(K)

AddLeftDigit(input('Введите число: '), input('Введие число которое хотите добавить слева: '))