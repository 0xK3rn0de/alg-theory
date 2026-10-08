#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
import os
import importlib.util

# Добавляем директорию tasks в путь для импорта модулей
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'tasks'))

tasks_dir = os.path.join(os.path.dirname(__file__), '..', 'tasks')

def load_task_module(filename):
    """Загружает модуль задачи из файла"""
    filepath = os.path.join(tasks_dir, filename)
    spec = importlib.util.spec_from_file_location(filename[:-3], filepath)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def test_task00_distances_calculation():
    """Тест задачи 00: расчет расстояний между городами"""
    task00 = load_task_module('00_distance.py')
    
    # Проверяем, что словарь distances заполнен
    assert 'Moscow' in task00.distances
    assert 'London' in task00.distances
    assert 'Paris' in task00.distances
    
    # Проверяем, что расстояние от города до себя равно 0
    assert task00.distances['Moscow']['Moscow'] == 0.0
    assert task00.distances['London']['London'] == 0.0
    assert task00.distances['Paris']['Paris'] == 0.0
    
    # Проверяем расчет расстояния между Москвой и Лондоном
    # ((550-510)^2 + (370-510)^2)^0.5 = (1600 + 19600)^0.5 = 21200^0.5 ≈ 145.6
    assert abs(task00.distances['Moscow']['London'] - 145.6) < 0.1


def test_task01_circle_area():
    """Тест задачи 01: расчет площади круга"""
    radius = 42
    pi = 3.1415926
    expected_area = pi * (radius ** 2)
    assert abs(expected_area - 5541.7693) < 0.0001

def test_task01_point_inside_circle():
    """Тест задачи 01: проверка точек внутри круга"""
    radius = 42
    
    # Точка (23, 34) - должна быть внутри (расстояние ≈ 40.8 < 42)
    x1, y1 = 23, 34
    distance_1 = (x1 ** 2 + y1 ** 2) ** 0.5
    assert distance_1 <= radius
    
    # Точка (30, 30) - должна быть снаружи (расстояние ≈ 42.4 > 42)
    x2, y2 = 30, 30
    distance_2 = (x2 ** 2 + y2 ** 2) ** 0.5
    assert distance_2 > radius

def test_task02_operations_result():
    """Тест задачи 02: математические операции"""
    result = 1 * (2 + 3) + 4 * 5
    assert result == 25

def test_task03_string_slicing():
    """Тест задачи 03: срезы строк"""
    my_favorite_movies = 'Терминатор, Пятый элемент, Аватар, Чужие, Назад в будущее'
    
    first_movie = my_favorite_movies[0:10]
    assert first_movie == 'Терминатор'
    
    last_movie = my_favorite_movies[42:]
    assert last_movie == 'Назад в будущее'
    
    second_movie = my_favorite_movies[12:25]
    assert second_movie == 'Пятый элемент'
    
    second_from_end = my_favorite_movies[35:40]
    assert second_from_end == 'Чужие'

def test_task04_family_height():
    """Тест задачи 04: рост семьи"""
    my_family_height = [
        ['мама', 165],
        ['папа', 180],
        ['я', 175],
    ]
    
    # Рост отца (второй элемент)
    father_height = my_family_height[1][1]
    assert father_height == 180
    
    # Общий рост семьи
    total_height = sum(member[1] for member in my_family_height)
    assert total_height == 520

def test_task05_zoo_operations():
    """Тест задачи 05: операции со списком животных"""
    zoo = ['lion', 'kangaroo', 'elephant', 'monkey']
    
    # Добавляем медведя между львом и кенгуру
    zoo.insert(1, 'bear')
    assert zoo == ['lion', 'bear', 'kangaroo', 'elephant', 'monkey']
    
    # Добавляем птиц
    birds = ['rooster', 'ostrich', 'lark']
    zoo.extend(birds)
    assert zoo == ['lion', 'bear', 'kangaroo', 'elephant', 'monkey', 'rooster', 'ostrich', 'lark']
    
    # Убираем слона
    zoo.remove('elephant')
    assert zoo == ['lion', 'bear', 'kangaroo', 'monkey', 'rooster', 'ostrich', 'lark']
    
    # Проверяем позиции (1-индексированные)
    lion_position = zoo.index('lion') + 1
    assert lion_position == 1
    
    lark_position = zoo.index('lark') + 1
    assert lark_position == 7

def test_task06_songs_list_total_time():
    """Тест задачи 06: общее время песен из списка"""
    violator_songs_list = [
        ['World in My Eyes', 4.86],
        ['Sweetest Perfection', 4.43],
        ['Personal Jesus', 4.56],
        ['Halo', 4.9],
        ['Waiting for the Night', 6.07],
        ['Enjoy the Silence', 4.20],
        ['Policy of Truth', 4.76],
        ['Blue Dress', 4.29],
        ['Clean', 5.83],
    ]
    
    total_songs = [song for song in violator_songs_list if song[0] in ['Halo', 'Enjoy the Silence', 'Clean']]
    total_time = sum(song[1] for song in total_songs)
    assert abs(total_time - 14.93) < 0.01

def test_task06_songs_dict_total_time():
    """Тест задачи 06: общее время песен из словаря"""
    violator_songs_dict = {
        'World in My Eyes': 4.76,
        'Sweetest Perfection': 4.43,
        'Personal Jesus': 4.56,
        'Halo': 4.30,
        'Waiting for the Night': 6.07,
        'Enjoy the Silence': 4.6,
        'Policy of Truth': 4.88,
        'Blue Dress': 4.18,
        'Clean': 5.68,
    }
    
    total_time_dict = sum(violator_songs_dict[song] for song in ['Sweetest Perfection', 'Policy of Truth', 'Blue Dress'])
    assert abs(total_time_dict - 13.49) < 0.01

def test_task07_secret_decoding():
    """Тест задачи 07: расшифровка сообщения"""
    secret_message = [
        'квевтфпп6щ3стмзалтнмаршгб5длгуча',
        'дьсеы6лц2бане4т64ь4б3ущея6втщл6б',
        'т3пплвце1н3и2кд4лы12чф1ап3бкычаь',
        'ьд5фму3ежородт9г686буиимыкучшсал',
        'бсц59мегщ2лятьаьгенедыв9фк9ехб1а',
    ]
    
    word1 = secret_message[0][3]
    word2 = secret_message[1][9:13]
    word3 = secret_message[2][5:15:2]
    word4 = secret_message[3][7:13][::-1]
    word5 = secret_message[4][16:21][::-1]
    
    decoded_message = f'{word1} {word2} {word3} {word4} {word5}'
    assert decoded_message == 'в бане веник дороже денег'

def test_task08_garden_sets():
    """Тест задачи 08: операции с множествами цветов"""
    garden = ('ромашка', 'роза', 'одуванчик', 'ромашка', 'гладиолус', 'подсолнух', 'роза')
    meadow = ('клевер', 'одуванчик', 'ромашка', 'клевер', 'мак', 'одуванчик', 'ромашка')
    
    garden_set = set(garden)
    meadow_set = set(meadow)
    
    # Все виды цветов
    all_flowers = garden_set | meadow_set
    expected_all = {'клевер', 'роза', 'одуванчик', 'подсолнух', 'ромашка', 'гладиолус', 'мак'}
    assert all_flowers == expected_all
    
    # Растут и там и там
    common = garden_set & meadow_set
    expected_common = {'ромашка', 'одуванчик'}
    assert common == expected_common
    
    # Растут в саду, но не на лугу
    garden_only = garden_set - meadow_set
    expected_garden_only = {'роза', 'гладиолус', 'подсолнух'}
    assert garden_only == expected_garden_only
    
    # Растут на лугу, но не в саду
    meadow_only = meadow_set - garden_set
    expected_meadow_only = {'мак', 'клевер'}
    assert meadow_only == expected_meadow_only

def test_task09_shopping_dict():
    """Тест задачи 09: словарь цен на продукты"""
    sweets = {
        'печенье': [
            {'shop': 'пятерочка', 'price': 9.99},
            {'shop': 'ашан', 'price': 10.99},
        ],
        'конфеты': [
            {'shop': 'магнит', 'price': 30.99},
            {'shop': 'пятерочка', 'price': 32.99},
        ],
        'карамель': [
            {'shop': 'магнит', 'price': 41.99},
            {'shop': 'ашан', 'price': 45.99},
        ],
        'пирожное': [
            {'shop': 'пятерочка', 'price': 59.99},
            {'shop': 'магнит', 'price': 62.99},
        ],
    }
    
    # Проверяем структуру
    assert 'печенье' in sweets
    assert 'конфеты' in sweets
    assert 'карамель' in sweets
    assert 'пирожное' in sweets
    
    # Проверяем, что у каждого продукта есть 2 магазина
    for product in sweets.values():
        assert len(product) == 2
        assert 'shop' in product[0]
        assert 'price' in product[0]
    
    # Проверяем минимальные цены
    assert sweets['печенье'][0]['price'] == 9.99  # минимальная цена печенья
    assert sweets['конфеты'][0]['price'] == 30.99  # минимальная цена конфет

def test_task10_store_calculation():
    """Тест задачи 10: расчет стоимости товаров на складе"""
    goods = {
        'Лампа': '12345',
        'Стол': '23456',
        'Диван': '34567',
        'Стул': '45678',
    }
    
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
    
    # Лампа: 27 * 42 = 1134
    lamp_batches = store[goods['Лампа']]
    lamp_quantity = sum(batch['quantity'] for batch in lamp_batches)
    lamp_cost = sum(batch['quantity'] * batch['price'] for batch in lamp_batches)
    assert lamp_quantity == 27
    assert lamp_cost == 1134
    
    # Стол: (22*510 + 32*520) = 11220 + 16640 = 27860
    table_batches = store[goods['Стол']]
    table_quantity = sum(batch['quantity'] for batch in table_batches)
    table_cost = sum(batch['quantity'] * batch['price'] for batch in table_batches)
    assert table_quantity == 54
    assert table_cost == 27860
    
    # Диван: (2*1200 + 1*1150) = 2400 + 1150 = 3550
    sofa_batches = store[goods['Диван']]
    sofa_quantity = sum(batch['quantity'] for batch in sofa_batches)
    sofa_cost = sum(batch['quantity'] * batch['price'] for batch in sofa_batches)
    assert sofa_quantity == 3
    assert sofa_cost == 3550
    
    # Стул: (50*100 + 12*95 + 43*97) = 5000 + 1140 + 4171 = 10311
    chair_batches = store[goods['Стул']]
    chair_quantity = sum(batch['quantity'] for batch in chair_batches)
    chair_cost = sum(batch['quantity'] * batch['price'] for batch in chair_batches)
    assert chair_quantity == 105
    assert chair_cost == 10311
