from rest_framework_supertest.shortcuts import currencies

from . import ShortcutTestCase


class CurrenciesShortcutsTests(ShortcutTestCase):
    def test_cryptocurrency_code(self) -> None:
        self.exec_test(['cryptocurrency_code'], currencies, 'cryptocurrency_code')

    def test_unique_cryptocurrency_code(self) -> None:
        self.exec_test(
            ['unique', 'cryptocurrency_code'],
            currencies,
            'unique_cryptocurrency_code',
        )

    def test_cryptocurrency_name(self) -> None:
        self.exec_test(['cryptocurrency_name'], currencies, 'cryptocurrency_name')

    def test_unique_cryptocurrency_name(self) -> None:
        self.exec_test(
            ['unique', 'cryptocurrency_name'],
            currencies,
            'unique_cryptocurrency_name',
        )

    def test_currency_code(self) -> None:
        self.exec_test(['currency_code'], currencies, 'currency_code')

    def test_unique_currency_code(self) -> None:
        self.exec_test(['unique', 'currency_code'], currencies, 'unique_currency_code')

    def test_currency_name(self) -> None:
        self.exec_test(['currency_name'], currencies, 'currency_name')

    def test_unique_currency_name(self) -> None:
        self.exec_test(['unique', 'currency_name'], currencies, 'unique_currency_name')

    def test_currency_symbol(self) -> None:
        code = "BRL"
        self.exec_test(['currency_symbol'], currencies, 'currency_symbol', code=code)

    def test_unique_currency_symbol(self) -> None:
        code = "BRL"
        self.exec_test(
            ['unique', 'currency_symbol'],
            currencies,
            'unique_currency_symbol',
            code=code,
        )

__all__ = []
