# Приложение РАСХОДЫ ПО ВИДАМ ПРОДУКЦИИ для автоматизированного
# контроля затрат на производство продукции. БД должна содержать таблицу Расходы со
# следующей структурой записи: Дата, Код продукта, Наименование продукта, Расходы,
# Сумма.

import sqlite3

conn = sqlite3.connect('production_expenses.db')
cursor = conn.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS Расходы (
    Дата TEXT,
    Код_продукта INTEGER,
    Наименование_продукта TEXT,
    Расходы TEXT,
    Сумма REAL
)
''')

# Пример добавления данных
cursor.execute("INSERT INTO Расходы VALUES ('2023-05-15', 1, 'Продукт А', 'Материалы', 1500.50)")
cursor.execute("INSERT INTO Расходы VALUES ('2023-05-16', 2, 'Продукт Б', 'Зарплата', 3200.75)")

conn.commit()
print("База данных создана, таблица 'Расходы' содержит данные:")
for row in cursor.execute("SELECT * FROM Расходы"):
    print(row)

conn.close()