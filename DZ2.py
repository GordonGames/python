"""
Перемножение и сложение матриц 3х3

Программа написана с использованием модудя NumPy
"""
import numpy as np
matrix1 = np.random.randint(0, 5, (3, 3))
matrix2 = np.random.randint(0, 5, (3, 3))
print("Первая матрица: ")
print(matrix1)
print("Вторая матрица: ")
print(matrix2)
print("Сумма матриц: ")
print(matrix1+matrix2)
print("Произведение матриц: ")
print(matrix1.dot(matrix2))
