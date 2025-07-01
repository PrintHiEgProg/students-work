import sqlite3
from sqlite3 import Error


def create_connection(db_file):
    """Создание соединения с базой данных SQLite"""
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        print(f"Подключено к SQLite версии {sqlite3.version}")
        return conn
    except Error as e:
        print(f"Ошибка при подключении к базе данных: {e}")
    return conn


def create_table(conn):
    """Создание таблицы Расходы"""
    try:
        cursor = conn.cursor()
        cursor.execute('''CREATE TABLE IF NOT EXISTS Расходы
                          (Дата TEXT NOT NULL,
                          Код_продукта TEXT NOT NULL,
                          Наименование_продукта TEXT NOT NULL,
                          Расходы TEXT NOT NULL,
                          Сумма REAL NOT NULL);''')
        print("Таблица 'Расходы' создана успешно")
    except Error as e:
        print(f"Ошибка при создании таблицы: {e}")


def insert_data(conn):
    """Добавление 10 записей в таблицу"""
    expenses = [
        ('2023-01-10', 'P001', 'Хлеб', 'Мука, дрожжи', 1500.50),
        ('2023-01-12', 'P002', 'Молоко', 'Тара, сырье', 2000.75),
        ('2023-01-15', 'P003', 'Сыр', 'Сырье, упаковка', 3500.00),
        ('2023-01-18', 'P004', 'Колбаса', 'Мясо, специи', 5000.25),
        ('2023-01-20', 'P005', 'Печенье', 'Мука, сахар', 1800.50),
        ('2023-01-22', 'P006', 'Сок', 'Фрукты, тара', 2200.00),
        ('2023-01-25', 'P007', 'Консервы', 'Овощи, банки', 3000.75),
        ('2023-01-28', 'P008', 'Шоколад', 'Какао, сахар', 2500.50),
        ('2023-01-30', 'P009', 'Чай', 'Листья, упаковка', 4000.00),
        ('2023-02-01', 'P010', 'Кофе', 'Зерна, упаковка', 4500.25)
    ]
    
    try:
        cursor = conn.cursor()
        cursor.executemany("INSERT INTO Расходы VALUES (?, ?, ?, ?, ?)", expenses)
        conn.commit()
        print("Данные успешно добавлены")
    except Error as e:
        print(f"Ошибка при добавлении данных: {e}")


def search_expenses(conn):
    """Поиск данных в таблице с использованием WHERE"""
    print("\n--- Поиск расходов ---")
    
    # Запрос 1: Поиск по коду продукта
    code = input("Введите код продукта для поиска: ")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Расходы WHERE Код_продукта = ?", (code,))
    rows = cursor.fetchall()
    print(f"\nРезультаты поиска по коду продукта '{code}':")
    for row in rows:
        print(row)
    
    # Запрос 2: Поиск по наименованию продукта
    name = input("\nВведите часть наименования продукта для поиска: ")
    cursor.execute("SELECT * FROM Расходы WHERE Наименование_продукта LIKE ?", (f"%{name}%",))
    rows = cursor.fetchall()
    print(f"\nРезультаты поиска по наименованию продукта '{name}':")
    for row in rows:
        print(row)
    
    # Запрос 3: Поиск по сумме (больше указанной)
    amount = float(input("\nВведите минимальную сумму расходов для поиска: "))
    cursor.execute("SELECT * FROM Расходы WHERE Сумма > ?", (amount,))
    rows = cursor.fetchall()
    print(f"\nРезультаты поиска по сумме больше {amount}:")
    for row in rows:
        print(row)


def update_expense(conn):
    """Обновление данных в таблице"""
    print("\n--- Редактирование расходов ---")
    
    # Показать все записи для удобства выбора
    cursor = conn.cursor()
    cursor.execute("SELECT rowid, * FROM Расходы")
    rows = cursor.fetchall()
    print("\nСписок всех расходов:")
    for row in rows:
        print(row)
    
    # Запрос 1: Обновление по rowid
    row_id = input("\nВведите ID записи для редактирования: ")
    new_amount = float(input("Введите новую сумму расходов: "))
    cursor.execute("UPDATE Расходы SET Сумма = ? WHERE rowid = ?", (new_amount, row_id))
    conn.commit()
    print(f"Запись с ID {row_id} обновлена")
    
    # Запрос 2: Обновление по коду продукта
    code = input("\nВведите код продукта для обновления: ")
    new_expenses = input("Введите новые виды расходов: ")
    cursor.execute("UPDATE Расходы SET Расходы = ? WHERE Код_продукта = ?", (new_expenses, code))
    conn.commit()
    print(f"Расходы для продукта с кодом {code} обновлены")
    
    # Запрос 3: Обновление по дате
    date = input("\nВведите дату для обновления (ГГГГ-ММ-ДД): ")
    new_name = input("Введите новое наименование продукта: ")
    cursor.execute("UPDATE Расходы SET Наименование_продукта = ? WHERE Дата = ?", (new_name, date))
    conn.commit()
    print(f"Наименования продуктов для даты {date} обновлены")


def delete_expense(conn):
    """Удаление данных из таблицы"""
    print("\n--- Удаление расходов ---")
    
    # Показать все записи для удобства выбора
    cursor = conn.cursor()
    cursor.execute("SELECT rowid, * FROM Расходы")
    rows = cursor.fetchall()
    print("\nСписок всех расходов:")
    for row in rows:
        print(row)
    
    # Запрос 1: Удаление по rowid
    row_id = input("\nВведите ID записи для удаления: ")
    cursor.execute("DELETE FROM Расходы WHERE rowid = ?", (row_id,))
    conn.commit()
    print(f"Запись с ID {row_id} удалена")
    
    # Запрос 2: Удаление по коду продукта
    code = input("\nВведите код продукта для удаления: ")
    cursor.execute("DELETE FROM Расходы WHERE Код_продукта = ?", (code,))
    conn.commit()
    print(f"Записи с кодом продукта {code} удалены")
    
    # Запрос 3: Удаление по сумме (меньше указанной)
    amount = float(input("\nВведите максимальную сумму для удаления: "))
    cursor.execute("DELETE FROM Расходы WHERE Сумма < ?", (amount,))
    conn.commit()
    print(f"Записи с суммой меньше {amount} удалены")


def show_all_expenses(conn):
    """Отображение всех записей в таблице"""
    print("\n--- Все записи в таблице Расходы ---")
    cursor = conn.cursor()
    cursor.execute("SELECT rowid, * FROM Расходы")
    rows = cursor.fetchall()
    for row in rows:
        print(row)


def main():
    database = "expenses.db"
    
    # Создание соединения с базой данных
    conn = create_connection(database)
    if conn is not None:
        # Создание таблицы
        create_table(conn)
        
        # Добавление данных (раскомментировать для первоначального заполнения)
        # insert_data(conn)
        
        while True:
            print("\nМеню управления базой данных 'Расходы по видам продукции':")
            print("1. Показать все записи")
            print("2. Добавить новые данные")
            print("3. Поиск данных")
            print("4. Редактировать данные")
            print("5. Удалить данные")
            print("0. Выход")
            
            choice = input("Выберите действие: ")
            
            if choice == "1":
                show_all_expenses(conn)
            elif choice == "2":
                insert_data(conn)
            elif choice == "3":
                search_expenses(conn)
            elif choice == "4":
                update_expense(conn)
            elif choice == "5":
                delete_expense(conn)
            elif choice == "0":
                print("Выход из программы")
                break
            else:
                print("Неверный ввод, попробуйте снова")
        
        # Закрытие соединения
        conn.close()
    else:
        print("Ошибка! Не удалось установить соединение с базой данных.")


if __name__ == '__main__':
    main()
