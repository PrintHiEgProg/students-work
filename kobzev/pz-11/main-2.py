# 2. Из предложенного текстового файла (text18-15.txt) вывести на экран его содержимое,
# количество букв в нижнем регистре. Сформировать новый файл, в который поместить текст
# в стихотворной форме предварительно заменив символы нижнего регистра на верхний.

with open('text18-15.txt', encoding='utf-8') as f:
    content = f.read()
    print("Содержимое файла:")
    print(content)
    
    lower_count = sum(1 for c in content if c.islower())
    print(f"Количество букв в нижнем регистре: {lower_count}")

with open('uppercase_poem.txt', 'w', encoding='utf-8') as f:
    f.write(content.upper())

print("Файл uppercase_poem.txt создан")