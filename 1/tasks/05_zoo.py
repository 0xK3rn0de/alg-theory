#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Есть список животных в зоопарке
zoo = ['lion', 'kangaroo', 'elephant', 'monkey']

# Посадите медведя (bear) между львом и кенгуру
# и выведите список на консоль
# TODO здесь ваш код

# Добавьте птиц из списка birds в последние клетки зоопарка
birds = ['rooster', 'ostrich', 'lark']
# и выведите список на консоль
# TODO здесь ваш код

# Уберите слона (elephant) из зоопарка
# и выведите список на консоль
# TODO здесь ваш код

# Выведите на консоль в какой клетке сидит лев (lion) и жаворонок (lark).
# Номера при выводе должны быть 1-индексированными (первая клетка - номер 1).
# TODO здесь ваш код

def run():
    zoo.insert(1, 'bear')
    print(zoo)

    zoo.extend(birds)
    print(zoo)

    zoo.remove('elephant')
    print(zoo)

    print(f'Лев - клетка {zoo.index("lion") + 1}')
    print(f'Жаворонок - клетка {zoo.index("lark") + 1}')


if __name__ == '__main__':
    run()
