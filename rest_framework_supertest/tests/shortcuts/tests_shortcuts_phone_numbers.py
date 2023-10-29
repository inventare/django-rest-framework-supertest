from django.test import TestCase

from rest_framework_supertest.shortcuts import phone_numbers

from .base import FakerMockMixin


class PhoneNumbersShortcutsTests(FakerMockMixin, TestCase):
    def test_phone_number(self):
        self.exec_test(['phone_number'], phone_numbers, 'phone_number')

    def test_unique_phone_number(self):
        self.exec_test(['unique', 'phone_number'], phone_numbers, 'unique_phone_number')

    def test_country_calling_code(self):
        self.exec_test(['country_calling_code'], phone_numbers, 'country_calling_code')

    def test_unique_country_calling_code(self):
        self.exec_test(['unique', 'country_calling_code'], phone_numbers, 'unique_country_calling_code')
