#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Есть словарь кодов товаров

goods = {
    'Лампа': '12345',
    'Стол': '23456',
    'Диван': '34567',
    'Стул': '45678',
}

# Есть словарь списков количества товаров на складе.

store = {
    '12345': [
        {'quantity': 27, 'price': 42},
    ],
    '23456': [
        {'quantity': 22, 'price': 510},
        {'quantity': 32, 'price': 520},
    ],
    '34567': [
        {'quantity': 2, 'price': 1200},
        {'quantity': 1, 'price': 1150},
    ],
    '45678': [
        {'quantity': 50, 'price': 100},
        {'quantity': 12, 'price': 95},
        {'quantity': 43, 'price': 97},
    ],
}

# Рассчитать на какую сумму лежит каждого товара на складе
# например для ламп

lamps_cost = store[goods['Лампа']][0]['quantity'] * store[goods['Лампа']][0]['price']


# или проще (/сложнее ?)
lamp_code = goods['Лампа']
lamps_item = store[lamp_code][0]
lamps_quantity = lamps_item['quantity']
lamps_price = lamps_item['price']
lamps_cost = lamps_quantity * lamps_price
print('Лампа -', lamps_quantity, 'шт, стоимость', lamps_cost, 'руб')

stol_code = goods['Стол']
stol_item0 = store[stol_code][0]
stol_item1 = store[stol_code][1]
stol_quantity0 = stol_item0['quantity']
stol_quantity1 = stol_item1['quantity']
stol_price0 = stol_item0['price']
stol_price1 = stol_item1['price']
stol_cost = stol_price1*stol_quantity0 + stol_price1*stol_quantity1
print('Стол -', stol_quantity1+stol_quantity0, 'шт, стоимость', stol_cost, 'руб')

stul_code = goods['Стул']
stul_item0 = store[stul_code][0]
stul_item1 = store[stul_code][1]
stul_item2 = store[stul_code][2]
stul_qw0 = stul_item0['quantity']
stul_qw1 = stul_item1['quantity']
stul_qw2 = stul_item2['quantity']
stul_pr0 = stul_item0['price']
stul_pr1 = stul_item1['price']
stul_pr2 = stul_item2['price']

stul_cost = stul_pr1*stul_qw1 + stul_qw0*stul_pr1 + stul_pr2*stul_qw2
print('Стул -', stul_qw1+stul_qw0+stul_qw2, 'шт, стоимость', stul_cost, 'руб')

# Вывести стоимость каждого товара на складе: один раз распечать сколько всего столов, стульев и т.д. на складе
# Формат строки <товар> - <кол-во> шт, стоимость <общая стоимость> руб

# WARNING для знающих циклы: БЕЗ циклов. Да, с переменными; да, неэффективно; да, копипаста.
# Это задание на ручное вычисление - что бы потом понять как работают циклы и насколько с ними проще жить.

# TODO здесь ваш код

##########################################################################################
# ВНИМАНИЕ! После того как __ВСЯ__ домашняя работа сделана и запушена на сервер,         #
# нужно зайти в ЛМС (LMS - Learning Management System ) по адресу http://go.skillbox.ru  #
# и оформить попытку сдачи ДЗ! Без этого ДЗ не будет проверяться!                        #
# Как оформить попытку сдачи смотрите видео - https://youtu.be/qVpN0L-C3LU               #
##########################################################################################






