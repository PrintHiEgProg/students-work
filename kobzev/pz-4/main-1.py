#Вариант 15.1. Дано вещественное число A и целое число N (>0). Используя один цикл, найти сумму 1 + A + A2 + A3 + ... + AN.

def calculate_sum(A, N):
    sum = 1  # Начинаем с 1, так как это первый член ряда
    current_term = 1  # Это A^0, который равен 1

    for i in range(1, N + 1):
        current_term *= A  # Вычисляем A^i
        sum += current_term  # Добавляем A^i к сумме

    return sum

def main():
    try:
        A = float(input("Введите вещественное число A: "))
        N = int(input("Введите целое число N (> 0): "))
        
        if N <= 0:
            print("Ошибка: N должно быть больше 0.")
            return
        
        result = calculate_sum(A, N)
        print(f"Сумма 1 + A + A^2 + ... + A^{N} = {result}")
    except ValueError:
        print("Ошибка: введите корректные значения.")

if __name__ == "__main__":
    main()