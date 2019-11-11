#!/usr/bin/env python

import unittest
from acme import Product
from acme_report import generate_products, inventory_report, ADJECTIVES, NOUNS
from random import randint, sample, uniform, choice


class AcmeProductTests(unittest.TestCase):
    '''Making sure Acme products are the tops!'''

    def test_default_product_price(self):
        '''Test default product price being 10.'''

        prod = Product('Test Product')
        self.assertEqual(prod.price, 10)

    def test_explode(self):
        '''test if explode function works properly'''

        prod = Product('Test Product', weight=30, flammability=1)
        self.assertEqual(prod.explode(), '...boom!')
        prod2 = Product('Test Product', weight=50, flammability=1.5)
        self.assertEqual(prod2.explode(), '...BABOOM!!')

    def test_stealability(self):
        '''test if stealability function works properly'''

        prod = Product('Test Product', price=5, weight=10)
        self.assertEqual(prod.stealability(), 'Kinda stealable.')
        prod2 = Product('Test Product', price=15, weight=10)
        self.assertEqual(prod2.stealability(), 'Very stealable!')

class AcmeReportTests(unittest.TestCase):
    '''Making sure the inventory report works properly'''

    def test_default_num_products(self):
        '''Testing if the default number of products is 30'''

        # I'm not quite sure what to do, but you can see what I'm trying at least!
        prod_list = generate_products()
        len(prod_list[::4])
        self.assertEqual(len(prod_list[::4]), 30)


    def test_legal_names(self):
        '''Testing to make sure names are validly selected from specified lists'''

        # On this one, I am stuck.
        generate_products()
        self.asserIn(generate_products().Product.name, [ADJECTIVES, NOUNS])

if __name__ == '__main__':
    unittest.main()