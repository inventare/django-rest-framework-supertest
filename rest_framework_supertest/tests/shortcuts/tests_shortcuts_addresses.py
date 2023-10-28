from django.test import TestCase
from rest_framework_supertest.shortcuts import addresses
from .base import FakerMockMixin

class AddressesShortcutsTests(FakerMockMixin, TestCase):
    def test_address(self):
        self.exec_test(['address'], addresses, 'address')

    def test_unique_address(self):
        self.exec_test(['unique', 'address'], addresses, 'unique_address')

    def test_building_number(self):
        self.exec_test(['building_number'], addresses, 'building_number')

    def test_unique_building_number(self):
        self.exec_test(['unique', 'building_number'], addresses, 'unique_building_number')

    def test_city(self):
        self.exec_test(['city'], addresses, 'city')

    def test_unique_city(self):
        self.exec_test(['unique', 'city'], addresses, 'unique_city')

    def test_country(self):
        self.exec_test(['country'], addresses, 'country')

    def test_unique_country(self):
        self.exec_test(['unique', 'country'], addresses, 'unique_country')

    def test_city_suffix(self):
        self.exec_test(['city_suffix'], addresses, 'city_suffix')

    def test_country_code(self):
        representation = 'alpha-2'
        self.exec_test(['country_code'], addresses, 'country_code', representation=representation)

    def test_current_country(self):
        self.exec_test(['current_country'], addresses, 'current_country')

    def test_unique_country_code(self):
        representation = 'alpha-2'
        self.exec_test(['unique', 'country_code'], addresses, 'unique_country_code', representation=representation)

    def test_current_country_code(self):
        self.exec_test(['current_country_code'], addresses, 'current_country_code')

    def test_postcode(self):
        self.exec_test(['postcode'], addresses, 'postcode')

    def test_unique_postcode(self):
        self.exec_test(['unique', 'postcode'], addresses, 'unique_postcode')

    def test_street_address(self):
        self.exec_test(['street_address'], addresses, 'street_address')

    def test_unique_street_address(self):
        self.exec_test(['unique', 'street_address'], addresses, 'unique_street_address')

    def test_street_name(self):
        self.exec_test(['street_name'], addresses, 'street_name')

    def test_unique_street_name(self):
        self.exec_test(['unique', 'street_name'], addresses, 'unique_street_name')

    def test_street_suffix(self):
        self.exec_test(['street_suffix'], addresses, 'street_suffix')
