#Вариант 15.3. Дан список размера N. Осуществить циклический сдвиг элементов списка влево на одну позицию (при этом AN перейдет в AN-1, AN-1 — в AN-2, . . ., A1 — в AN).

def left_cyclic_shift(A):
    if len(A) == 0:
        return A  # Если список пуст, возвращаем его
    
    last_element = A[0]  # Сохраняем первый элемент
    for i in range(len(A) - 1):
        A[i] = A[i + 1]  # Сдвигаем элементы влево
    A[-1] = last_element  # Перемещаем первый элемент в конец
    
    return A

def main():
    try:
        N = int(input("Введите размер списка N (N > 0): "))
        
        if N <= 0:
            print("Ошибка: размер списка должен быть положительным.")
            return
        
        A = []
        print(f"Введите {N} элементов списка:")
        for _ in range(N):
            element = int(input())
            A.append(element)
        
        result = left_cyclic_shift(A)
        print("Список после циклического сдвига влево на одну позицию:")
        print(result)
    except ValueError:
        print("Ошибка: введите корректные целые числа.")

if __name__ == "__main__":
    main()