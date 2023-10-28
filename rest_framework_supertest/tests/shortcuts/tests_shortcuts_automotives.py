from django.test import TestCase
from rest_framework_supertest.shortcuts import automotives
from .base import FakerMockMixin

class AutomotivesShortcutsTests(FakerMockMixin, TestCase):
    def test_license_plate(self):
        self.exec_test(['license_plate'], automotives, 'license_plate')

    def test_unique_license_plate(self):
        self.exec_test(['unique', 'license_plate'], automotives, 'unique_license_plate')

    def test_vin(self):
        self.exec_test(['vin'], automotives, 'vin')

    def test_unique_vin(self):
        self.exec_test(['unique', 'vin'], automotives, 'unique_vin')
