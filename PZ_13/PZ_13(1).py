#В матрице элементы столбца N 
#(N задать с клавиатуры) увеличить в два раза
import numpy as np

def replace_last_row(matrix):
  """
  Заменяет элементы последней строки матрицы на 0.

  Args:
    matrix: Матрица numpy.

  Returns:
    Матрица numpy с измененной последней строкой.
  """

  # Проверка наличия хотя бы одной строки
  if matrix.shape[0] == 0:
    raise ValueError("Матрица пуста")

  # Замена элементов последней строки на 0
  matrix[-1, :] = 0

  return matrix

# Пример использования
matrix = np.array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
])

result_matrix = replace_last_row(matrix.copy())
print("Исходная матрица:")
print(matrix)
print("Матрица с замененной последней строкой:")
print(result_matrix)

