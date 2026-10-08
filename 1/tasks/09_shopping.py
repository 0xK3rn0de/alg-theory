#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Есть словарь магазинов с распродажами

shops = {
    'ашан': [
        {'name': 'печенье', 'price': 10.99},
        {'name': 'конфеты', 'price': 34.99},
        {'name': 'карамель', 'price': 45.99},
        {'name': 'пирожное', 'price': 67.99}
    ],
    'пятерочка': [
        {'name': 'печенье', 'price': 9.99},
        {'name': 'конфеты', 'price': 32.99},
        {'name': 'карамель', 'price': 46.99},
        {'name': 'пирожное', 'price': 59.99}
    ],
    'магнит': [
        {'name': 'печенье', 'price': 11.99},
        {'name': 'конфеты', 'price': 30.99},
        {'name': 'карамель', 'price': 41.99},
        {'name': 'пирожное', 'price': 62.99}
    ],
}

# Создайте словарь цен на продукты следующего вида (писать прямо в коде)
# sweets = {
#     'печенье': [
#         {'shop': 'пятерочка', 'price': 9.99},
#         {'shop': 'ашан', 'price': 10.99},
#     ],
#     ...
# }
# Указать надо только по 2 магазина с минимальными ценами

def build_sweets(shops, shops_number=2):
    # Собираем по каждому продукту список магазинов с ценой
    sweets = {}

    for shop_name, shop_products in shops.items():
        for product in shop_products:
            offers = sweets.setdefault(product['name'], [])
            offers.append({'shop': shop_name, 'price': product['price']})

    # Сортируем предложения по цене и оставляем только самые дешёвые магазины
    return {
        product_name: sorted(offers, key=lambda offer: offer['price'])[:shops_number]
        for product_name, offers in sweets.items()
    }


# Заполняем словарь цен на продукты
sweets = build_sweets(shops)


def run():
    # Каждый продукт выводим отдельной строкой:
    #   печенье: [{'shop': 'пятерочка', 'price': 9.99}, {'shop': 'ашан', 'price': 10.99}]
    for product_name, offers in sweets.items():
        print(f'{product_name}: {offers}')


if __name__ == '__main__':
    run()
