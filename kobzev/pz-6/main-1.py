#Вариант 15.1. Дан список A размера N. Вывести его элементы в следующем порядке: A1, A2, AN, AN-1, A3, A4, AN-2, AN-3, … .

def rearrange_list(A):
    N = len(A)
    result = []
    
    for i in range((N + 1) // 2):
        result.append(A[i])  # Добавляем A[i]
        if i != N - i - 1:  # Проверяем, чтобы не добавлять один и тот же элемент
            result.append(A[N - i - 1])  # Добавляем A[N - i - 1]
    
    return result

def main():
    try:
        N = int(input("Введите размер списка N: "))
        
        if N <= 0:
            print("Ошибка: размер списка должен быть положительным.")
            return
        
        A = []
        print(f"Введите {N} элементов списка:")
        for _ in range(N):
            element = input()  # Можно использовать input() для ввода строк или чисел
            A.append(element)
        
        result = rearrange_list(A)
        print("Элементы списка в новом порядке:")
        print(result)
    except ValueError:
        print("Ошибка: введите корректные значения.")

if __name__ == "__main__":
    main()