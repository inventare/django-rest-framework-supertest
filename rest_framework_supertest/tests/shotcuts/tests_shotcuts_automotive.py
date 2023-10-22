from django.test import TestCase
from rest_framework_supertest.shotcuts import automotive
from .base import FakerMockMixin

class AutomotiveShotcuts(FakerMockMixin, TestCase):
    def test_license_plate(self):
        self.exec_test(['license_plate'], automotive, 'license_plate')

    def test_unique_license_plate(self):
        self.exec_test(['unique', 'license_plate'], automotive, 'unique_license_plate')

    def test_vin(self):
        self.exec_test(['vin'], automotive, 'vin')

    def test_unique_vin(self):
        self.exec_test(['unique', 'vin'], automotive, 'unique_vin')
