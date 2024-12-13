# Напиши программу, которая ищет максимально часто встречающийся символ в тексте,
# и минимально часто встречающийся. Если максимальных несколько, вывести все. Если минимальных несколько,
# то нужно тоже вывести все.
# На выходе должны быть 2 списка с максимально часто встречающимися символами и минимально часто встречающимися.
# Например [' ', 'а'], ['ъ', 'ь', 'ы']
from typing import Tuple, List, Any


def task(s: str) -> tuple[list[str]]:
    dct: dict = dict()
    for char in s:
        if char in dct:
            dct[char] += 1
        else:
            dct[char] = 1

    max_freq: list[str] = [letter for letter, value in dct.items() if value == max(dct.values())]
    min_freq: list[str] = [letter for letter, value in dct.items() if value == min(dct.values())]

    return max_freq, min_freq

'''
Есть функция:
def append_to(element, to=[]):
    to.append(element)
    return to

print(append_to(1)) # [1]
print(append_to(2)) # [2]
print(append_to(3, [4])) # [4, 3]
Что с ней не так? Как починить?
'''

# Как НУЖНО было сделать
def append_to(element, to=None):
    if to is not None:
        to.append(element)
        return to
    else:
        return [element]

# Как сделал я
def append_to(element, *args):
    if args:
        to = list(args[0])
    else:
        to = []

    to.append(element)
    return to


print(append_to(1)) # [1]
print(append_to(2)) # [2]
print(append_to(3, [4])) # [4, 3]









a, b, c = 1, 5, 9

a = b

b += 6

print(a)

