# Описать функцию AddLeftDigit(D, K). добавляющую к целому положительному
# числу К слева цифру D (D — входной параметр целого типа, лежащий в диапазоне
# 1-9, К — параметр целого типа, являющийся одновременно входным и выходным).
# С помощью этой функции последовательно добавить к данному числу К слева
# данные цифры D1 и D2, выводя результат каждого добавления.

def AddLeftDigit():
    K = input()
    D1 = input()
    D2 = input()

    K = D1 + K
    print(K)

    K = D2 + K
    print(K)

AddLeftDigit()