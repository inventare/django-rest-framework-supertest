from rest_framework_supertest.shortcuts import automotives

from . import ShortcutTestCase


class AutomotivesShortcutsTests(ShortcutTestCase):
    def test_license_plate(self) -> None:
        self.exec_test(['license_plate'], automotives, 'license_plate')

    def test_unique_license_plate(self) -> None:
        self.exec_test(['unique', 'license_plate'], automotives, 'unique_license_plate')

    def test_vin(self) -> None:
        self.exec_test(['vin'], automotives, 'vin')

    def test_unique_vin(self) -> None:
        self.exec_test(['unique', 'vin'], automotives, 'unique_vin')

__all__ = []
