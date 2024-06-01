# В последовательности на n целых элементов в последней ее половине найти
# сумму элементов.
import random

spi = [random.randint(5, 10) for i in range(10)]
print(f'список: {spi}')
n = len(spi)
half =  spi[n//2:]
sum_half = sum(half)
print(f'сумма второй половины его илементов: {sum_half}')