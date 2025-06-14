# Создать класс «bank», который имеет атрибуты суммы, срок и процентной ставки.
# Добавить методы: расчет начисленных процентов, расчет суммы денег на счете.

class Bank:
    def __init__(self, amount, term, rate):
        self.amount = amount
        self.term = term
        self.rate = rate
    
    def calculate_interest(self):
        return self.amount * self.rate * self.term / 100
    
    def calculate_total(self):
        return self.amount + self.calculate_interest()

account = Bank(1000, 2, 5)
print(f"Сумма: {account.amount}, срок: {account.term} года, ставка: {account.rate}%")
print(f"Начисленные проценты: {account.calculate_interest()}")
print(f"Итоговая сумма: {account.calculate_total()}")