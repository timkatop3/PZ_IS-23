# Создание текстового файла с последовательностью чисел
with open('numbers.txt', 'w') as file:
    numbers = [5, -3, 12, -8, 15, 6, -2, 10]
    file.write('\n'.join(map(str, numbers)))

# Чтение изначально созданного файла и обработка данных
with open('numbers.txt', 'r') as file:
    data = file.readlines()
    numbers = list(map(int, [num.strip() for num in data]))

    # Нахождение индекса последнего минимального элемента
    min_index = numbers.index(min(numbers))

    # Вычисление суммы элементов больших 10 во второй половине
    second_half_sum = sum([num for num in numbers[len(numbers)//2:] if num > 10])

# Создание нового текстового файла с обработанными данными
with open('processed_data.txt', 'w') as file:
    file.write(f"Gived data: {' '.join(map(str, numbers))}\n")
    file.write(f"Length of data: {len(numbers)}\n")
    file.write(f"index of min last given element: {min_index}\n")
    file.write(f"Sum of second part tat > 10: {second_half_sum}\n")
