from django.test import TestCase

from rest_framework_supertest.shortcuts import files

from .base import FakerMockMixin


class FilesShortcutsTests(FakerMockMixin, TestCase):
    def test_file_extension(self):
        category = "image"
        self.exec_test(['file_extension'], files, 'file_extension', category=category)

    def test_unique_file_extension(self):
        category = "image"
        self.exec_test(['unique', 'file_extension'], files, 'unique_file_extension', category=category)

    def test_file_name(self):
        category = "image"
        extension = "jpg"
        self.exec_test(['file_name'], files, 'file_name', category=category, extension=extension)

    def test_unique_file_name(self):
        category = "image"
        extension = "jpg"
        self.exec_test(['unique', 'file_name'], files, 'unique_file_name', category=category, extension=extension)

    def test_mime_type(self):
        category = "image"
        self.exec_test(['mime_type'], files, 'mime_type', category=category)

    def test_unique_mime_type(self):
        category = "image"
        self.exec_test(['unique', 'mime_type'], files, 'unique_mime_type', category=category)
