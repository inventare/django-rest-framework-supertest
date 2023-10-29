from rest_framework_supertest.shortcuts import geographicals

from . import ShortcutTestCase


class GeographicalsShortcutsTests(ShortcutTestCase):
    def test_coordinate(self) -> None:
        center = 50
        radius = 20
        self.exec_test(
            ['coordinate'],
            geographicals,
            'coordinate',
            center=center,
            radius=radius,
        )

    def test_unique_coordinate(self) -> None:
        center = 50
        radius = 20
        self.exec_test(
            ['unique', 'coordinate'],
            geographicals,
            'unique_coordinate',
            center=center,
            radius=radius,
        )

    def test_latitude(self) -> None:
        self.exec_test(['latitude'], geographicals, 'latitude')

    def test_unique_latitude(self) -> None:
        self.exec_test(['unique', 'latitude'], geographicals, 'unique_latitude')

    def test_longitude(self) -> None:
        self.exec_test(['longitude'], geographicals, 'longitude')

    def test_unique_longitude(self) -> None:
        self.exec_test(['unique', 'longitude'], geographicals, 'unique_longitude')

__all__ = []
