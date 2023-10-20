money_capital = 20000  # Подушка безопасности
salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
increase = 0.05  # Ежемесячный рост цен

piggy_bank = money_capital + salary
new_spend = spend
count = 0

while new_spend < piggy_bank:
    piggy_bank -= new_spend
    piggy_bank += salary
    new_spend *= 1 + increase
    count += 1

print("Количество месяцев, которое можно протянуть без долгов:", count)
