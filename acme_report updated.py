#!/usr/bin/env python

from random import randint, uniform, choice
from acme import Product

# Useful to use with random.sample to generate names
ADJECTIVES = ['Awesome', 'Shiny', 'Impressive', 'Portable', 'Improved']
NOUNS = ['Anvil', 'Catapult', 'Disguise', 'Mousetrap', '???']

def generate_products(num_products=30):
    products = []

    for i in range(num_products):
        name = f'{choice(ADJECTIVES)} {choice(NOUNS)}'
        price = randint(5, 100)
        weight = randint(5, 100)
        flammability = uniform(0.0, 2.5)
        prod = Product(name=name, price=price, weight=weight, flammability=flammability)
        products.append(list(prod.__dict__.values()))

    return products


def inventory_report(products):
    '''Outputs the inventory report based on the general report function'''
    names = []
    avg_price = []
    avg_weight = []
    avg_flammability = []

    for product in products:
        names.append(product[0])
        prices.append(product[1])
        weights.append(product[2])
        flames.append(product[3])

    # average price calculation
    total_p = 0
    for i in prices:
        total_p += i
    avg_price = total_p / len(prices)

    # average weight calculation
    total_w = 0
    for i in weights:
        total_p += i
    avg_weight = total_p / len(weights)

    # average flammability calculation
    total_f = 0
    for i in flames:
        total_p += i
    avg_flammability = total_p / len(flames)

    # output strings
    print('ACME CORPORATION OFFICIAL INVENTORY REPORT')
    print(f'Unique product names: {len(set(names))}')
    print(f'Average price: {avg_price}')
    print(f'Average weight: {avg_weight}')
    print(f'Average flammability: {avg_flammability}')


if __name__ == '__main__':
    inventory_report(generate_products())

