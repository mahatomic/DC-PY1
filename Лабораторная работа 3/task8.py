money_capital = 10000
salary = 5000
spend = 6000
increase = 0.05

month = 0  # количество месяцев, которое можно прожить
delta = 0  # разница между тратами за месяц и зарплатой

while money_capital >= spend:
    delta = spend - salary
    money_capital -= delta
    month += 1
    spend *= (increase + 1)

print(month)
