# Задача 1: Подсчет латинских и русских букв
text = "Привет, Hello!"
latin = sum(1 for c in text if c.isalpha() and c.isascii())
russian = sum(1 for c in text if c.isalpha() and not c.isascii())
print(f"1. Латинских: {latin}, Русских: {russian}")

# Задача 2: Подсчет знаков препинания
punctuation = sum(1 for c in text if c in '.,!?;:')
print(f"2. Знаков препинания: {punctuation}")