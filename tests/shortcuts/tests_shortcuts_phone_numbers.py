from rest_framework_supertest.shortcuts import phone_numbers

from . import ShortcutTestCase


class PhoneNumbersShortcutsTests(ShortcutTestCase):
    def test_phone_number(self) -> None:
        self.exec_test(['phone_number'], phone_numbers, 'phone_number')

    def test_unique_phone_number(self) -> None:
        self.exec_test(['unique', 'phone_number'], phone_numbers, 'unique_phone_number')

    def test_country_calling_code(self) -> None:
        self.exec_test(['country_calling_code'], phone_numbers, 'country_calling_code')

    def test_unique_country_calling_code(self) -> None:
        self.exec_test(
            ['unique', 'country_calling_code'],
            phone_numbers,
            'unique_country_calling_code',
        )

__all__ = []
