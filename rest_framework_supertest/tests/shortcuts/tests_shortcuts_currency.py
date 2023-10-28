from django.test import TestCase
from rest_framework_supertest.shortcuts import currency
from .base import FakerMockMixin

class CurrencyShortcutsTests(FakerMockMixin, TestCase):
    def test_cryptocurrency_code(self):
        self.exec_test(['cryptocurrency_code'], currency, 'cryptocurrency_code')

    def test_unique_cryptocurrency_code(self):
        self.exec_test(['unique', 'cryptocurrency_code'], currency, 'unique_cryptocurrency_code')

    def test_cryptocurrency_name(self):
        self.exec_test(['cryptocurrency_name'], currency, 'cryptocurrency_name')

    def test_unique_cryptocurrency_name(self):
        self.exec_test(['unique', 'cryptocurrency_name'], currency, 'unique_cryptocurrency_name')

    def test_currency_code(self):
        self.exec_test(['currency_code'], currency, 'currency_code')

    def test_unique_currency_code(self):
        self.exec_test(['unique', 'currency_code'], currency, 'unique_currency_code')

    def test_currency_name(self):
        self.exec_test(['currency_name'], currency, 'currency_name')

    def test_unique_currency_name(self):
        self.exec_test(['unique', 'currency_name'], currency, 'unique_currency_name')

    def test_currency_symbol(self):
        code = "BRL"
        self.exec_test(['currency_symbol'], currency, 'currency_symbol', code=code)

    def test_unique_currency_symbol(self):
        code = "BRL"
        self.exec_test(['unique', 'currency_symbol'], currency, 'unique_currency_symbol', code=code)