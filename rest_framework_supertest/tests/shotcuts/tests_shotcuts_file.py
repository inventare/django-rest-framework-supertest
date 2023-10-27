from django.test import TestCase
from rest_framework_supertest.shotcuts import file
from .base import FakerMockMixin

class FileShotcuts(FakerMockMixin, TestCase):
    def test_file_extension(self):
        category = "image"
        self.exec_test(['file_extension'], file, 'file_extension', category=category)

    def test_unique_file_extension(self):
        category = "image"
        self.exec_test(['unique', 'file_extension'], file, 'unique_file_extension', category=category)

    def test_file_name(self):
        category = "image"
        extension = "jpg"
        self.exec_test(['file_name'], file, 'file_name', category=category, extension=extension)

    def test_unique_file_name(self):
        category = "image"
        extension = "jpg"
        self.exec_test(['unique', 'file_name'], file, 'unique_file_name', category=category, extension=extension)

    def test_mime_type(self):
        category = "image"
        self.exec_test(['mime_type'], file, 'mime_type', category=category)

    def test_unique_mime_type(self):
        category = "image"
        self.exec_test(['unique', 'mime_type'], file, 'unique_mime_type', category=category)
