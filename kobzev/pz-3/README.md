# Отчет по практическому занятию

**Студент группы ИС-26 Кобзев Е. М.**

**Практическое занятие № 3**

**Тема:** Составление программ с использованием условных и логических конструкций в IDE PyCharm Community.

**Цель:** Закрепить усвоенные знания, понятия, алгоритмы, основные принципы составления программ, приобрести навыки составления программ с использованием условных и логических конструкций в IDE PyCharm Community.

---

## **Первый код**

**Постановка задачи:**  
Даны три целых числа: A, B, C. Проверить истинность высказывания: «Ровно одно из чисел A, B, C положительное».

**Тип алгоритма:** Условный с использованием логических операций.

**Блок-схема алгоритма:**

![Блок-схема](https://ltdfoto.ru/images/2025/02/08/SNIMOK-EKRANA-2025-02-08-V-6.08.36PM.png)

**Текст программы:**

```python
# Вариант 15.1. Даны три целых числа: A, B, C. Проверить истинность высказывания: «Ровно одно из чисел A, B, C положительное».

def check_positive_numbers(A, B, C):
    """
    Функция проверяет, что ровно одно из чисел A, B, C положительное.
    :param A: первое число
    :param B: второе число
    :param C: третье число
    :return: True, если ровно одно число положительное, иначе False
    """
    # Проверяем, что ровно одно число положительное
    if (A > 0 and B <= 0 and C <= 0) or \
       (B > 0 and A <= 0 and C <= 0) or \
       (C > 0 and A <= 0 and B <= 0):
        return True
    else:
        return False


def main():
    """
    Основная функция программы.
    """
    try:
        # Ввод чисел
        A = int(input("Введите число A: "))
        B = int(input("Введите число B: "))
        C = int(input("Введите число C: "))

        # Проверка условия
        result = check_positive_numbers(A, B, C)

        # Вывод результата
        print(f"Ровно одно из чисел положительное: {result}")

    except ValueError:
        print("Ошибка: введите целые числа.")


if __name__ == "__main__":
    main()
```

**Протокол работы программы:**

```bash
Введите число A: 5
Введите число B: -3
Введите число C: 0
Ровно одно из чисел положительное: True

Программа успешно завершена!
Process finished with exit code 0
```

**Второй код**

**Постановка задачи:**
Даны целочисленные координаты точки на плоскости. Если точка совпадает с началом координат, то вывести 0. Если точка не совпадает с началом координат, но лежит на оси OX или OY, то вывести соответственно 1 или 2. Если точка не лежит на координатных осях, то вывести 3.

**Тип алгоритма:** Условный с использованием вложенных условий.

**Блок-схема алгоритма:**

![Блок-схема](https://ltdfoto.ru/images/2025/02/08/SNIMOK-EKRANA-2025-02-08-V-6.12.00PM.png)


**Текст программы:**

```python 
# Вариант 15.2. Даны целочисленные координаты точки на плоскости. Если точка совпадает с началом координат, то вывести 0. Если точка не совпадает с началом координат, но лежит на оси OX или OY, то вывести соответственно 1 или 2. Если точка не лежит на координатных осях, то вывести 3.

def check_point_position(x, y):
    if x == 0 and y == 0:
        return 0
    elif y == 0 and x != 0:
        return 1
    elif x == 0 and y != 0:
        return 2
    else:
        return 3

def main():
    try:
        x = int(input("Введите координату x: "))
        y = int(input("Введите координату y: "))
        result = check_point_position(x, y)
        print(result)
    except ValueError:
        print("Ошибка: введите целочисленные значения.")

if __name__ == "__main__":
    main()
```

**Протокол работы программы:**

```bash
Введите координату x: 0
Введите координату y: 5
2

Программа успешно завершена!
Process finished with exit code 0
```

**Вывод:**

В процессе выполнения практического занятия я выработал(а) навыки составления программ с использованием условных и логических конструкций в IDE PyCharm Community. Были использованы языковые конструкции if-elif-else, логические операторы, а также обработка исключений с помощью try-except. Выполнены разработка кода, отладка, тестирование и оптимизация программного кода. Оба задания успешно решены: первая программа корректно проверяет условие на наличие ровно одного положительного числа, а вторая программа определяет положение точки на координатной плоскости. Готовые программные коды выложены на GitHub.