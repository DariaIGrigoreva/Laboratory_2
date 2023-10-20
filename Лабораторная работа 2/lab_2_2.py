salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
months = 10  # Количество месяцев, которое планируется протянуть без долгов
increase = 0.03  # Ежемесячный рост цен

month = 0
piggy_bank = 0

while True:
    minus = spend - salary
    if month >= 10:
        break

    spend *= 1 + increase
    piggy_bank += minus
    month += 1

print(f"Подушка безопасности, чтобы протянуть {months} месяцев без долгов:", round(piggy_bank, 2))