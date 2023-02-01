#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Есть строка с перечислением фильмов

my_favorite_movies = 'Терминатор, Пятый элемент, Аватар, Чужие, Назад в будущею'

# Выведите на консоль с помощью индексации строки, последовательно:
#   первый фильм
#   последний
#   второй
#   второй с конца

# Переопределять my_favorite_movies и использовать .split() нельзя.
# Запятая не должна выводиться.

# TODO здесь ваш

print ('Первый - ', my_favorite_movies[0:10])
print ('Последний - ', my_favorite_movies[-15:-1]+my_favorite_movies[-1])
print ('Второй - ', my_favorite_movies[12:25])
print ('Второй с конца - ', my_favorite_movies[27:33])