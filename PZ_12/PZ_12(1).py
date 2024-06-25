#В последовательности на n целых элементов найти 
#количество пар, для которых произведение элементов 
#делится на 3 (элементы пары в последовательности являются соседними)
def count_divisible_pairs(sequence):
  """
  Подсчитывает количество пар в последовательности, для которых произведение делится на 3.

  Args:
    sequence: Список целых чисел.

  Returns:
    Количество пар, для которых произведение делится на 3.
  """

  def is_divisible_by_3(x):
    return x % 3 == 0

  def get_pairs(sequence):
    if len(sequence) <= 1:
      return []
    return [(sequence[i], sequence[i + 1]) for i in range(len(sequence) - 1)]

  def count_pairs(pairs):
    return sum(1 for pair in pairs if is_divisible_by_3(pair[0] * pair[1]))

  return count_pairs(get_pairs(sequence))

# Пример использования
sequence = [1, 2, 3, 4, 5, 6]
count = count_divisible_pairs(sequence)
print(f"Количество пар с произведением, делящимся на 3: {count}")

