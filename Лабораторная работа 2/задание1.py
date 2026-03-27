salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
months = 10  # Количество месяцев, которое планируется протянуть без долгов
increase = 0.03  # Ежемесячный рост цен
debtfree_month = 10
debt = 0

while debtfree_month > 0:
   debt = debt + salary - spend
   debtfree_month += -1
   spend = spend * (1 + increase)
money_capital = debt * -1
print(f"Подушка безопасности, чтобы протянуть {months} месяцев без долгов:", round(money_capital))

