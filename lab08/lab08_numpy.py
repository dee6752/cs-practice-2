import numpy as np

print("\n--- Задание 1 ---")

hours = np.arange(0, 22, 3)

line = np.linspace(0, 1, 5)

zeros = np.zeros(6, dtype=int)

unknown_table = np.full((2, 3), -1)

identity = np.eye(3)

print("hours:", hours)
print("shape:", hours.shape, "ndim:", hours.ndim, "size:", hours.size, "dtype:", hours.dtype)

print("\n--- Задание 2 ---")

print("Третий элемент (индекс 2):", hours[2])
print("Последний элемент:", hours[-1])
print("Элементы с индексами 2-5:", hours[2:6])
print("Каждый второй элемент:", hours[::2])
print("В обратном порядке:", hours[::-1])

print("\n--- Задание 3 ---")

temperatures = np.array([
    [12, 14, 13, 15],
    [11, 13, 16, 17],
    [10, 12, 15, 18],
])

print("Форма:", temperatures.shape)
print("Число измерений:", temperatures.ndim)
print("Число элементов:", temperatures.size)
print("Вторая строка, третий столбец:", temperatures[1, 2])
print("Первая строка:", temperatures[0, :])
print("Последний столбец:", temperatures[:, -1])
print("Первые две строки без первого столбца:\n", temperatures[:2, 1:])
print("Центральный фрагмент 2x2:\n", temperatures[0:2, 1:3])

print("\n--- Задание 4 ---")

matrix = np.arange(1, 26).reshape(5, 5)
print("Исходная матрица:\n", matrix)

print("\nПервые три строки:\n", matrix[:3, :], "\nShape:", matrix[:3, :].shape)
print("\nПоследние две строки:\n", matrix[-2:, :], "\nShape:", matrix[-2:, :].shape)
print("\nПервые два столбца:\n", matrix[:, :2], "\nShape:", matrix[:, :2].shape)
print("\nСтроки 1-3, столбцы 2-4:\n", matrix[1:4, 2:5], "\nShape:", matrix[1:4, 2:5].shape)
print("\nПравый нижний угол 2x2:\n", matrix[-2:, -2:], "\nShape:", matrix[-2:, -2:].shape)

print("\n--- Задание 5 ---")
changed_hours = hours.copy()
changed_hours[2:5] = 99
changed_hours[1::2] = -1
print("changed_hours:", changed_hours)
print("Исходный hours:", hours)

changed_matrix = matrix.copy()
changed_matrix[1, :] = 0
changed_matrix[:, -1] = -1
changed_matrix[1:4, 1:4] = 100
print("\nИтоговая матрица:\n", changed_matrix)
print("\nИсходная матрица (не изменилась):\n", matrix)

print("\n--- Задание 6 ---")

numbers = np.arange(12)
table = numbers.reshape(3, 4)
transposed = table.T

print("Форма numbers:", numbers.shape)
print("Форма table:", table.shape)
print("Форма transposed:", transposed.shape)
