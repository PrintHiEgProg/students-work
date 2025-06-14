# Сгенерировать словарь вида {0: 0, 1: 1, 2: 8, 3: 27, 4: 64, 5: 125, 6: 216},
# Удалить из него первый и последний элементы. Отобразить исходный и
# получающийся словарь, использовать for, range.

original = {i: i**3 for i in range(7)}
print("Исходный словарь:", original)

keys = list(original.keys())
if keys:
    del original[keys[0]]
if keys:
    del original[keys[-1]]

print("Словарь после удаления:", original)