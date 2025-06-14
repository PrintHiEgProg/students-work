# 2. В двумерном списке найти минимальный элемент в предпоследней строке.

matrix = [
    [5, 3, 8],
    [2, 6, 1],
    [9, 4, 7],
    [3, 0, 2]
]

print("Исходная матрица:")
for row in matrix:
    print(row)

pre_last_row = matrix[-2]
min_element = min(pre_last_row)

print(f"\nМинимальный элемент в предпоследней строке: {min_element}")