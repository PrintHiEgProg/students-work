#Вариант 15.1. Составить функцию, которая выведет на экран строку, содержащую задаваемое с клавиатуры число символов

def print_string_with_length(N):
    if N <= 0:
        print("Ошибка: N должно быть больше 0.")
        return
    
    # Создаем строку из N символов (например, пробелов)
    result_string = '*' * N  # Можно заменить '*' на любой другой символ
    print(result_string)

def main():
    try:
        N = int(input("Введите целое число N (> 0): "))
        print_string_with_length(N)
    except ValueError:
        print("Ошибка: введите корректное целое число.")

if __name__ == "__main__":
    main()