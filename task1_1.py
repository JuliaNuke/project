# 1. Реализовать вывод информации о промежутке времени в зависимости от его
# продолжительности duration в секундах:
# a. до минуты: <s> сек;
# b. до часа: <m> мин <s> сек;
# c. до суток: <h> час <m> мин <s> сек;
# d. * в остальных случаях: <d> дн <h> час <m> мин <s> сек.

duration = int(input('Введите число в секундах: '))

if duration // 86400:
    print(duration // 86400, 'дн')
    duration = duration % 86400
if duration // 3600:
    print(duration // 3600, 'ч')
    duration = duration % 3600
if duration // 60:
    print(duration // 60, 'мин')
    duration = duration % 60

print(duration, 'сек')
