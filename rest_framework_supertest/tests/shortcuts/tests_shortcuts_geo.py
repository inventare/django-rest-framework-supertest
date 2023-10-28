from django.test import TestCase
from rest_framework_supertest.shortcuts import geo
from .base import FakerMockMixin

class GeoShortcutsTests(FakerMockMixin, TestCase):
    def test_coordinate(self):
        center = 50
        radius = 20
        self.exec_test(['coordinate'], geo, 'coordinate', center=center, radius=radius)

    def test_unique_coordinate(self):
        center = 50
        radius = 20
        self.exec_test(['unique', 'coordinate'], geo, 'unique_coordinate', center=center, radius=radius)

    def test_latitude(self):
        self.exec_test(['latitude'], geo, 'latitude')

    def test_unique_latitude(self):
        self.exec_test(['unique', 'latitude'], geo, 'unique_latitude')

    def test_longitude(self):
        self.exec_test(['longitude'], geo, 'longitude')

    def test_unique_longitude(self):
        self.exec_test(['unique', 'longitude'], geo, 'unique_longitude')
