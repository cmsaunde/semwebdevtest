"""
Description
This code reads in the wine_queries and tests them

Created by Carla Saunders
15 June 2021
"""

import unittest
import rdflib
from wine_queries import * 

class test_list_regions(unittest.TestCase):

    def test_regions_list(self):
        self.assertEqual(list_regions(), [' Burgundy', ' Chablis', ' France', ' Italy', ' Piedmont', ' Puglia'])

class test_list_varietals(unittest.TestCase):

    def test_varietals_list(self):
        self.assertEqual(list_varietals(), [' Canaiolo', ' Chardonnay', ' Malvasia_bianca', ' Nebbiolo', ' Sangiovesse', ' Zinfandel'])

class test_list_classes_of_wines(unittest.TestCase):

    def test_classes_of_wines_list(self):
        self.assertEqual(list_classes_of_wines(), [' Barbaresco', ' Barolo', ' Chablis_wine', ' Chianti_wine'])

class test_query_wines(unittest.TestCase):

    def test_color(self):
        self.assertEqual(query_wines(colour='red'), [' Barbaresco', ' Barolo', ' Chianti_wine', ' Barolo_Villero_2015'])

    def test_varietal(self):
        self.assertEqual(query_wines(varietal='Chardonnay'), [' Chablis_wine'])

    def test_region(self):
        self.assertEqual(query_wines(region='Chianti'), [' Chianti_wine'])


    def test_null(self):
        self.assertEqual(query_wines(colour='red', varietal='Chardonnay', region='Chianti'), None)

if __name__ == '__main__':
    unittest.main()