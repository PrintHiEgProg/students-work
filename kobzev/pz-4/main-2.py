#Вариант 15.2. Дано целое число N (>0), являющееся некоторой степенью числа 2: N = 2K. Найти целое число K — показатель этой степени.

def find_power_of_two(N):
    if N <= 0:
        return "Ошибка: N должно быть больше 0."
    
    K = 0
    temp = N
    
    while temp > 1:
        if temp % 2 != 0:  # Если temp нечетное
            return "Ошибка: N не является степенью 2."
        temp //= 2  # Делим temp на 2
        K += 1  # Увеличиваем K на 1
    
    return K

def main():
    try:
        N = int(input("Введите целое число N (> 0): "))
        
        result = find_power_of_two(N)
        print(result)
    except ValueError:
        print("Ошибка: введите корректное целое число.")

if __name__ == "__main__":
    main()