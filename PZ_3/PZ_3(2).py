# Вапмант 8: Едипицы длипы пропумеровапы следующим образом: 1 — дециметр, 2 — километр,
# 3 — метр, 4 — миллиметр, 5 — сантиметр. Дан номер единицы длины (целое число
# в диапазоне 1-5) и длина отрезка в этих единицах (вещественное число). Найти
# длину отрезка в метрах.

len_num = int(input())
length = float(input())

if len_num == 1:
    print(length / 10.0)
elif len_num == 2:
    print(length * 1000.0)
elif len_num == 3:
    print(length)
elif len_num == 4:
    print(length / 1000.0)
elif len_num == 5:
    print(length / 100)