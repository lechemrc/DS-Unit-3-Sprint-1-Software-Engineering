#!/usr/bin/env python

from random import randint, sample, uniform
from acme import Product

# Useful to use with random.sample to generate names
ADJECTIVES = ['Awesome', 'Shiny', 'Impressive', 'Portable', 'Improved']
NOUNS = ['Anvil', 'Catapult', 'Disguise', 'Mousetrap', '???']


names = []
prices = []
weights = []
flames = []

def generate_products(num_products=30):
    products = []

    for i in range(num_products):
        Product.name = f'{choice(ADJECTIVES)} {choice(NOUNS)}'
        products.append(Product.name)

        Product.price = randint(5, 100)
        products.append(Product.price)

        Product.weight = randint(5, 100)
        products.append(Product.weight)

        Product.flammability = uniform(0.0, 2.5)
        products.append(Product.flammability)

    return products


def inventory_report(products):
    '''Outputs the inventory report based on the general report function'''
    # creating list from previous function
    prod_list = generate_products()
    temp_list = prod_list.copy()

    print('ACME CORPORATION OFFICIAL INVENTORY REPORT')
    names = temp_list[::4]
    temp_list.pop(0)
    print(f'Unique product names: {len(set(names))}')

    prices = temp_list[::4]
    temp_list.pop(0)
    total_p = 0
    for i in range(0, len(prices)):
        total_p = total_p + prices[i]
    print(f'Average price: {total_p / len(prices)}')

    weights = temp_list[::4]
    temp_list.pop(0)
    total_w = 0
    for i in range(0, len(weights)):
        total_w = total_w + weights[i]
    print(f'Average weight: {total_w / len(weights)}')

    flames = temp_list[::4]
    temp_list.pop(0)
    total_f = 0
    for i in range(0, len(flames)):
        total_f = total_f + flames[i]
    print(f'Average flammability: {total_f / len(flames)}')


if __name__ == '__main__':
    inventory_report(generate_products())

