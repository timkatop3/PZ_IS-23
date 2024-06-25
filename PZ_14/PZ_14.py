# В исходном текстовом файле(Dostoevsky.txt) найти все произведения писателя.
# Посчитать количество полученных элементов.
import re

def find_works(text_file):
    with open(text_file, encoding='utf-8') as f:
        text = f.read()

    # Регулярное выражение для поиска названий произведений
    # (основано на том, что названия заключены в кавычки)
    pattern = r'«(.*?)»'

    # Поиск всех совпадений
    matches = re.findall(pattern, text)
    print(f"Список произведений Достоевского, найденных в файле '{text_file}':")
    for match in matches:
        print(f"- {match}")

    print(f"Общее количество произведений: {len(matches)}")
    # Извлечение названий произведений из совпадений
    return matches

# Вызов функции и вывод результатов
works = find_works('Dostoevsky.txt')

