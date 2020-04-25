import unittest
from src.design_patterns.behavioral.catalog import Catalog, CatalogInstance, CatalogClass, CatalogStatic

class CatalogTest(unittest.TestCase):
    def test_catalog_main_method(self):
        test = Catalog('param_value_2')
        self.assertEqual(test.main_method(), 'executed method 2!')

    def test_catalog_instance_main_method(self):
        test = CatalogInstance('param_value_1')
        self.assertEqual(test.main_method(), 'Value x1')

    def test_catalog_class_main_method(self):
        test = CatalogClass('_class_method_2')
        self.assertEqual(test.main_method(), 'Value x2')

    def test_catalog_static_main_method(self):
        test = CatalogStatic('param_value_1')
        self.assertEqual(test.main_method(), 'executed method 1!')
