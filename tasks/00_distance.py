#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Есть словарь координат городов

sites = {
    'Moscow': (550, 370),
    'London': (510, 510),
    'Paris': (480, 480),
}

# Составим словарь словарей расстояний между ними
# расстояние на координатной сетке - ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5

distances = {}

# TODO здесь заполнение словаря
def calculate_distances(sites):
    for city1 in sites:
        distances[city1] = {}
        for city2 in sites:
            x1, y1 = sites[city1]
            x2, y2 = sites[city2]
            distance = ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5
            distances[city1][city2] = distance

    return distances

# Заполняем словарь расстояний
calculate_distances(sites)

def run():
    print(calculate_distances(sites))


if __name__ == '__main__':
    run()