#Вариант 15.1. Даны три целых числа: A, B, C. Проверить истинность высказывания: «Ровно одно из чисел A, B, C положительное».

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