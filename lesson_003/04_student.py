# -*- coding: utf-8 -*-

# (цикл while)

# Ежемесячная стипендия студента составляет educational_grant руб., а расходы на проживание превышают стипендию
# и составляют expenses руб. в месяц. Рост цен ежемесячно увеличивает расходы на 3%, кроме первого месяца
# Составьте программу расчета суммы денег, которую необходимо единовременно попросить у родителей,
# чтобы можно было прожить учебный год (10 месяцев), используя только эти деньги и стипендию.
# Формат вывода:
#   Студенту надо попросить ХХХ.ХХ рублей

educational_grant, expenses = 10000, 12000

# TODO здесь ваш код
month = 1
summa_rashod = 0
while month <= 10:
    if month == 1:
        summa_rashod = summa_rashod + expenses
    else:
        expenses = expenses + expenses * 0.03
        summa_rashod = summa_rashod + expenses
    month += 1

print('Проси', summa_rashod - (educational_grant*10))