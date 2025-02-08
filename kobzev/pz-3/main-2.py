#Вариант 15.2. Даны целочисленные координаты точки на плоскости. Если точка совпадает с началом координат, то вывести 0. Если точка не совпадает с началом координат, но лежит на оси OX или OY, то вывести соответственно 1 или 2. Если точка не лежит на координатных осях, то вывести 3.

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