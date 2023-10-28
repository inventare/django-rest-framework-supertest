from django.test import TestCase
from rest_framework_supertest.shortcuts import isbn
from .base import FakerMockMixin

class ISBNShortcutsTests(FakerMockMixin, TestCase):
    def test_isbn10(self):
        separator = "@"
        self.exec_test(['isbn10'], isbn, 'isbn10', separator=separator)

    def test_unique_isbn10(self):
        separator = "@"
        self.exec_test(['unique', 'isbn10'], isbn, 'unique_isbn10', separator=separator)

    def test_isbn13(self):
        separator = "@"
        self.exec_test(['isbn13'], isbn, 'isbn13', separator=separator)

    def test_unique_isbn13(self):
        separator = "@"
        self.exec_test(['unique', 'isbn13'], isbn, 'unique_isbn13', separator=separator)
