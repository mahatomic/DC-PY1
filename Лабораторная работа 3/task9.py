salary = 5000  # зарплата
spend = 6000  # траты
months = 10  # количество месяцев
increase = 0.03  # рост цен

need_money = 0  # количество денег, чтобы прожить 10 месяцев
delta = 0  # разница между тратами за месяц и зарплатой

for i in range(months):
    delta = spend - salary
    need_money += delta
    spend *= (increase + 1)

print(round(need_money))
