salary = 5000  # зарплата
spend = 6000  # траты
months = 10  # количество месяцев
increase = 0.03  # рост цен

need_money = 0  # количество денег, чтобы прожить 10 месяцев

all_salary = salary * months  # вся зарплата за 10 месяцев, больше не будет :(
need_money = spend  # за первый месяц 6000 р

for i in range(2, months + 1):
    spend += spend * increase
    need_money += spend

need_money -= all_salary

print(round(need_money))
