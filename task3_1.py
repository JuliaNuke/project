# 1. Написать функцию num_translate(), переводящую числительные от 0 до 10 c английского на
# русский язык. Например:
# >>> num_translate("one")
# "один"
# >>> num_translate("eight")
# "восемь"
# Если перевод сделать невозможно, вернуть None. Подумайте, как и где лучше хранить
# информацию, необходимую для перевода: какой тип данных выбрать, в теле функции или
# снаружи.

translate = {'zero': 'ноль', 'one': 'один', 'two': 'два', 'three': 'три', 'four': 'четыре', 'five': 'пять', 'six': 'шесть', 'seven': 'семь', 'eight': 'восемь', 'nine': 'девять', 'ten': 'десять'}


def num_translate(values):
    if key in translate:
        print(translate[values])
    elif key == 'Выход':
        print('exit')
    else:
        print(None)


key = None


while key != 'Выход':
    key = input('Введите значение: ')
    num_translate(key)

