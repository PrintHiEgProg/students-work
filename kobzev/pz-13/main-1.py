# 1. В двумерном списке найти суммы элементов каждого столбца и поместить их в
# новый массив. Выполнить замену элементов второй строки исходной матрицы на
# полученные суммы.

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print("Исходная матрица:")
for row in matrix:
    print(row)

column_sums = [sum(col) for col in zip(*matrix)]
matrix[1] = column_sums

print("\nМатрица после замены:")
for row in matrix:
    print(row)