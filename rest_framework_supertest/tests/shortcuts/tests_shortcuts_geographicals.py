from django.test import TestCase
from rest_framework_supertest.shortcuts import geographicals
from .base import FakerMockMixin

class GeographicalsShortcutsTests(FakerMockMixin, TestCase):
    def test_coordinate(self):
        center = 50
        radius = 20
        self.exec_test(['coordinate'], geographicals, 'coordinate', center=center, radius=radius)

    def test_unique_coordinate(self):
        center = 50
        radius = 20
        self.exec_test(['unique', 'coordinate'], geographicals, 'unique_coordinate', center=center, radius=radius)

    def test_latitude(self):
        self.exec_test(['latitude'], geographicals, 'latitude')

    def test_unique_latitude(self):
        self.exec_test(['unique', 'latitude'], geographicals, 'unique_latitude')

    def test_longitude(self):
        self.exec_test(['longitude'], geographicals, 'longitude')

    def test_unique_longitude(self):
        self.exec_test(['unique', 'longitude'], geographicals, 'unique_longitude')
