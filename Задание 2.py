# Напишите функцию, которая проверяет: является ли слово палиндромом

s = (input('Введите строку: '))
n_s = s.replace(' ', '')


def palindrom():
    if n_s == n_s[::-1]:
        print('Cтрока палиндром')
    else:
        print('Не палиндром')


print(palindrom())
