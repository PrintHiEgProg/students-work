# 2. Составить генератор (yield), который выводит из строки только буквы.

def letters_generator(text):
    for char in text:
        if char.isalpha():
            yield char

text = "Hello, World! 123"
print("Исходная строка:", text)
print("Буквы из строки:", list(letters_generator(text)))