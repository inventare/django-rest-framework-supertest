from rest_framework_supertest.shortcuts import emojis

from . import ShortcutTestCase


class EmojisShortcutsTests(ShortcutTestCase):
    def test_emoji(self) -> None:
        self.exec_test(['emoji'], emojis, 'emoji')

    def test_unique_emoji(self) -> None:
        self.exec_test(['unique', 'emoji'], emojis, 'unique_emoji')

__all__ = []
