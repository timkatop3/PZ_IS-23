#Составить генератор (yield), который 
#преобразует все буквенные символы в
#заглавные.
def upper_case_generator(text):
  """
  Генератор, преобразующий все буквенные символы в строке в заглавные.

  Args:
    text: Строка.

  Yields:
    Символы из строки в заглавном регистре.
  """

  for char in text:
    if char.islower():
      yield char.upper()
    else:
      yield char

# Пример использования
text = "привет, мир!"
for char in upper_case_generator(text):
  print(char)
