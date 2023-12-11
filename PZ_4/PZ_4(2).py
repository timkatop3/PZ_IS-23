# Начальный вклад в банк равси 1000 руб. Через каждый месяц размер вклада
# увеличивается на Р процентов от имеющейся суммы (Р — вещественное число, 0 < Р
# < 25). По данному Р определить, через сколько месяцев размер вклада превысит 1100
# руб. и вывести найденное количество месяцев К (целое число) и итоговый размер
# вклала S (вещественное число).

s = 1000.0
k = 0

try:
    p = float(input('Введите на какой процент будет увеличиваться вклад: '))
    while s <= 1100.0:
        s = s + (s / 100) * p
        k+=1
    print('Через ', k, ' месяцев вклад превысит 1100')
    print('Через ', k, ' месяцев вклад будет составлять', s)
except ValueError:
    print('Incorrect type!')