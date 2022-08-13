import enum
from getopt import getopt


def good():
    return ["Harry", "Ron", "Hermione"]


print(good())  # 9.1


def get_odds():
    for i in range(10):
        if i % 2 == 1:
            yield i


for index, i in enumerate(get_odds()):
    if index == 2:
        print(i)  # 9.2
        break
