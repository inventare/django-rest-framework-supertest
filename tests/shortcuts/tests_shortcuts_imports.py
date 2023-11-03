from types import FunctionType, ModuleType
from typing import List

from django.test import TestCase

from rest_framework_supertest import shortcuts


class ShortcutsImportTests(TestCase):
    def _get_modules(self) -> List[str]:
        items = dir(shortcuts)
        modules = []
        for item in items:
            if item.startswith(("__", "_")):
                continue
            item_prop = getattr(shortcuts, item)
            if not isinstance(item_prop, ModuleType):
                continue
            modules = [*modules, item]
        return modules


    def setUp(self) -> None:
        self.modules = self._get_modules()

    def test_reimports(self) -> None:
        items = dir(shortcuts)
        for item in items:
            if item in self.modules:
                continue
            item_prop = getattr(shortcuts, item)
            if not isinstance(item_prop, FunctionType):
                continue
            module_name = item_prop.__module__
            self.assertTrue(module_name.startswith('rest_framework_supertest.shortcuts.'))
            module_name = module_name.replace('rest_framework_supertest.shortcuts.', '')
            self.assertTrue(module_name in self.modules)


__all__ = []
