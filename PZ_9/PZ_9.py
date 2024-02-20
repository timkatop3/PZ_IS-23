# Вариант 8. Дана строка 'апельсины 45 991 63 100 12 яблоки 13 47 26 0 16',
# отражающая продажи продукции по дням в кг. Преобразовать информацию из
# строки в словари, с использованием функции найти среднее значение продаж по
# каждому виду продукции, результаты вывести на экран
def calculate_average_sales(data_string):
    data_list = data_string.split()  # Разбиваем строку данных на список
    data_dict = {}  # Создаем пустой словарь для хранения данных
    current_key = None  # Переменная для хранения текущего ключа
    current_values = []  # Переменная для хранения текущих значений

    for item in data_list:
        if item.isdigit():  # Если элемент является числом
            current_values.append(int(item))  # Добавляем его в список текущих значений
        else:
            if current_key is not None:  # Если текущий ключ не пустой
                data_dict[current_key] = sum(current_values) / len(current_values)  # Вычисляем среднее значение продаж и добавляем в словарь
            current_key, current_values = item, []  # Обновляем текущий ключ и очищаем список текущих значений

    if current_key is not None:  # Проверяем, что последний ключ не пустой
        data_dict[current_key] = sum(current_values) / len(current_values)  # Вычисляем среднее значение продаж и добавляем в словарь

    return data_dict  # Возвращаем словарь с данными

data_string = 'апельсины 45 991 63 100 12 яблоки 13 47 26 0 16'
sales_data = calculate_average_sales(data_string)

for product, average_sales in sales_data.items():
    print(f"Среднее значение продаж для {product}: {average_sales}")  # Выводим результаты на экран
