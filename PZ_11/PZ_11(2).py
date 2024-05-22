# Чтение содержимого текстового файла
with open('text18-8.txt', 'r') as file:
    text = file.read()

# Подсчет количества букв в тексте
num_letters = sum(l.isalpha() for l in text)

# Удаление буквы 'с' из текста
new_text = text.replace('c', '')

# Запись нового текста в стихотворной форме в файл
with open('poem.txt', 'w') as file:
    file.write(new_text)
