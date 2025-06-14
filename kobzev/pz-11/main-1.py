# 1. Средствами языка Python сформировать текстовый файл (.txt), содержащий
# последовательность из целых положительных и отрицательных чисел. Сформировать
# новый текстовый файл (.txt) следующего вида, предварительно выполнив требуемую
# обработку элементов:

import random

# Создаем исходный файл
with open('numbers.txt', 'w') as f:
    numbers = [random.randint(-10, 10) for _ in range(10)]
    f.write(' '.join(map(str, numbers)))

# Обрабатываем данные
with open('numbers.txt') as f:
    numbers = list(map(int, f.read().split()))
    
first = numbers[0]
min_index = len(numbers) - 1 - numbers[::-1].index(min(numbers))
product = [x * first for x in numbers]

with open('result.txt', 'w') as f:
    f.write("Исходные данные: " + ' '.join(map(str, numbers)) + '\n')
    f.write(f"Количество элементов: {len(numbers)}\n")
    f.write(f"Индекс последнего минимального элемента: {min_index}\n")
    f.write("Умножаем все элементы на первый элемент: " + ' '.join(map(str, product)))

print("Файлы созданы: numbers.txt и result.txt")