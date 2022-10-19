money_capital = 10000
salary = 5000
spend = 6000
increase = 0.05

month = 0  # количество месяцев, которое можно прожить

all_money = money_capital + salary  # все денежки, зарплата просчитана в цикле
while all_money > 0:
    all_money = all_money - spend
    spend += spend * increase
    month += 1

print(month)
