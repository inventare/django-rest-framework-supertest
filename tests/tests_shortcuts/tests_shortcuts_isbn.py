from rest_framework_supertest.shortcuts import isbn

from . import ShortcutTestCase


class ISBNShortcutsTests(ShortcutTestCase):
    def test_isbn10(self) -> None:
        separator = "@"
        self.exec_test(['isbn10'], isbn, 'isbn10', separator=separator)

    def test_unique_isbn10(self) -> None:
        separator = "@"
        self.exec_test(['unique', 'isbn10'], isbn, 'unique_isbn10', separator=separator)

    def test_isbn13(self) -> None:
        separator = "@"
        self.exec_test(['isbn13'], isbn, 'isbn13', separator=separator)

    def test_unique_isbn13(self) -> None:
        separator = "@"
        self.exec_test(['unique', 'isbn13'], isbn, 'unique_isbn13', separator=separator)

__all__ = []
