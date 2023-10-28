from django.test import TestCase
from rest_framework_supertest.shortcuts import person
from .base import FakerMockMixin

class PersonShortcutsTests(FakerMockMixin, TestCase):
    def test_first_name(self):
        self.exec_test(['first_name'], person, 'first_name')

    def test_unique_first_name(self):
        self.exec_test(['unique', 'first_name'], person, 'unique_first_name')

    def test_first_name_female(self):
        self.exec_test(['first_name_female'], person, 'first_name_female')

    def test_unique_first_name_female(self):
        self.exec_test(['unique', 'first_name_female'], person, 'unique_first_name_female')

    def test_first_name_male(self):
        self.exec_test(['first_name_male'], person, 'first_name_male')

    def test_unique_first_name_male(self):
        self.exec_test(['unique', 'first_name_male'], person, 'unique_first_name_male')

    def test_first_name_nonbinary(self):
        self.exec_test(['first_name_nonbinary'], person, 'first_name_nonbinary')

    def test_unique_first_name_nonbinary(self):
        self.exec_test(['unique', 'first_name_nonbinary'], person, 'unique_first_name_nonbinary')

    def test_language_name(self):
        self.exec_test(['language_name'], person, 'language_name')

    def test_last_name(self):
        self.exec_test(['last_name'], person, 'last_name')

    def test_unique_last_name(self):
        self.exec_test(['unique', 'last_name'], person, 'unique_last_name')

    def test_last_name_female(self):
        self.exec_test(['last_name_female'], person, 'last_name_female')

    def test_unique_last_name_female(self):
        self.exec_test(['unique', 'last_name_female'], person, 'unique_last_name_female')

    def test_last_name_male(self):
        self.exec_test(['last_name_male'], person, 'last_name_male')

    def test_unique_last_name_male(self):
        self.exec_test(['unique', 'last_name_male'], person, 'unique_last_name_male')

    def test_last_name_nonbinary(self):
        self.exec_test(['last_name_nonbinary'], person, 'last_name_nonbinary')

    def test_unique_last_name_nonbinary(self):
        self.exec_test(['unique', 'last_name_nonbinary'], person, 'unique_last_name_nonbinary')

    def test_name(self):
        self.exec_test(['name'], person, 'name')

    def test_unique_name(self):
        self.exec_test(['unique', 'name'], person, 'unique_name')

    def test_name_female(self):
        self.exec_test(['name_female'], person, 'name_female')

    def test_unique_name_female(self):
        self.exec_test(['unique', 'name_female'], person, 'unique_name_female')

    def test_name_male(self):
        self.exec_test(['name_male'], person, 'name_male')

    def test_unique_name_male(self):
        self.exec_test(['unique', 'name_male'], person, 'unique_name_male')

    def test_name_nonbinary(self):
        self.exec_test(['name_nonbinary'], person, 'name_nonbinary')

    def test_unique_name_nonbinary(self):
        self.exec_test(['unique', 'name_nonbinary'], person, 'unique_name_nonbinary')

    def test_prefix(self):
        self.exec_test(['prefix'], person, 'prefix')

    def test_prefix_female(self):
        self.exec_test(['prefix_female'], person, 'prefix_female')

    def test_prefix_male(self):
        self.exec_test(['prefix_male'], person, 'prefix_male')

    def test_prefix_nonbinary(self):
        self.exec_test(['prefix_nonbinary'], person, 'prefix_nonbinary')

    def test_suffix(self):
        self.exec_test(['suffix'], person, 'suffix')

    def test_suffix_female(self):
        self.exec_test(['suffix_female'], person, 'suffix_female')

    def test_suffix_male(self):
        self.exec_test(['suffix_male'], person, 'suffix_male')

    def test_suffix_nonbinary(self):
        self.exec_test(['suffix_nonbinary'], person, 'suffix_nonbinary')
