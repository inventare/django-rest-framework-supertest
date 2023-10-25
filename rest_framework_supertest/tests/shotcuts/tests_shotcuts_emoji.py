from django.test import TestCase
from rest_framework_supertest.shotcuts import emojis
from .base import FakerMockMixin

class EmojiShotcuts(FakerMockMixin, TestCase):
    def test_emoji(self):
        self.exec_test(['emoji'], emojis, 'emoji')

    def test_unique_emoji(self):
        self.exec_test(['unique', 'emoji'], emojis, 'unique_emoji')
