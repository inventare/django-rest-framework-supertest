from rest_framework_supertest.shortcuts import persons

from . import ShortcutTestCase


class PersonShortcutsTests(ShortcutTestCase):
    def test_first_name(self) -> None:
        self.exec_test(['first_name'], persons, 'first_name')

    def test_unique_first_name(self) -> None:
        self.exec_test(['unique', 'first_name'], persons, 'unique_first_name')

    def test_first_name_female(self) -> None:
        self.exec_test(['first_name_female'], persons, 'first_name_female')

    def test_unique_first_name_female(self) -> None:
        self.exec_test(
            ['unique', 'first_name_female'],
            persons,
            'unique_first_name_female',
        )

    def test_first_name_male(self) -> None:
        self.exec_test(['first_name_male'], persons, 'first_name_male')

    def test_unique_first_name_male(self) -> None:
        self.exec_test(['unique', 'first_name_male'], persons, 'unique_first_name_male')

    def test_first_name_nonbinary(self) -> None:
        self.exec_test(['first_name_nonbinary'], persons, 'first_name_nonbinary')

    def test_unique_first_name_nonbinary(self) -> None:
        self.exec_test(
            ['unique', 'first_name_nonbinary'],
            persons,
            'unique_first_name_nonbinary',
        )

    def test_language_name(self) -> None:
        self.exec_test(['language_name'], persons, 'language_name')

    def test_last_name(self) -> None:
        self.exec_test(['last_name'], persons, 'last_name')

    def test_unique_last_name(self) -> None:
        self.exec_test(['unique', 'last_name'], persons, 'unique_last_name')

    def test_last_name_female(self) -> None:
        self.exec_test(['last_name_female'], persons, 'last_name_female')

    def test_unique_last_name_female(self) -> None:
        self.exec_test(
            ['unique', 'last_name_female'],
            persons,
            'unique_last_name_female',
        )

    def test_last_name_male(self) -> None:
        self.exec_test(['last_name_male'], persons, 'last_name_male')

    def test_unique_last_name_male(self) -> None:
        self.exec_test(['unique', 'last_name_male'], persons, 'unique_last_name_male')

    def test_last_name_nonbinary(self) -> None:
        self.exec_test(['last_name_nonbinary'], persons, 'last_name_nonbinary')

    def test_unique_last_name_nonbinary(self) -> None:
        self.exec_test(
            ['unique', 'last_name_nonbinary'],
            persons,
            'unique_last_name_nonbinary',
        )

    def test_name(self) -> None:
        self.exec_test(['name'], persons, 'name')

    def test_unique_name(self) -> None:
        self.exec_test(['unique', 'name'], persons, 'unique_name')

    def test_name_female(self) -> None:
        self.exec_test(['name_female'], persons, 'name_female')

    def test_unique_name_female(self) -> None:
        self.exec_test(['unique', 'name_female'], persons, 'unique_name_female')

    def test_name_male(self) -> None:
        self.exec_test(['name_male'], persons, 'name_male')

    def test_unique_name_male(self) -> None:
        self.exec_test(['unique', 'name_male'], persons, 'unique_name_male')

    def test_name_nonbinary(self) -> None:
        self.exec_test(['name_nonbinary'], persons, 'name_nonbinary')

    def test_unique_name_nonbinary(self) -> None:
        self.exec_test(['unique', 'name_nonbinary'], persons, 'unique_name_nonbinary')

    def test_prefix(self) -> None:
        self.exec_test(['prefix'], persons, 'prefix')

    def test_prefix_female(self) -> None:
        self.exec_test(['prefix_female'], persons, 'prefix_female')

    def test_prefix_male(self) -> None:
        self.exec_test(['prefix_male'], persons, 'prefix_male')

    def test_prefix_nonbinary(self) -> None:
        self.exec_test(['prefix_nonbinary'], persons, 'prefix_nonbinary')

    def test_suffix(self) -> None:
        self.exec_test(['suffix'], persons, 'suffix')

    def test_suffix_female(self) -> None:
        self.exec_test(['suffix_female'], persons, 'suffix_female')

    def test_suffix_male(self) -> None:
        self.exec_test(['suffix_male'], persons, 'suffix_male')

    def test_suffix_nonbinary(self) -> None:
        self.exec_test(['suffix_nonbinary'], persons, 'suffix_nonbinary')

__all__ = []
