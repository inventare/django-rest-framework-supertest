import importlib
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

    def _get_functions(self) -> List[str]:
        items = dir(shortcuts)
        functions = []
        for item in items:
            if item.startswith(("__", "_")):
                continue
            item_prop = getattr(shortcuts, item)
            if not isinstance(item_prop, FunctionType):
                continue
            functions = [*functions, item]
        return functions

    def setUp(self) -> None:
        self.modules = self._get_modules()
        self.functions = self._get_functions()

    def test_reimports(self) -> None:
        """Grant if all exported from shortcuts is intern of it's modules."""
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
            self.assertIn(module_name, self.modules)

    def test_reexport(self) -> None:
        """Grant if all exported from intern modules is exported from __init__."""
        items = self.modules
        for item in items:
            module_name = f"rest_framework_supertest.shortcuts.{item}"
            module = importlib.import_module(module_name)
            subitems = dir(module)

            for sub in subitems:
                if sub.startswith(("__", "_")):
                    continue
                if sub == 'unique':
                    continue
                sub_prop = getattr(module, sub)
                if not isinstance(sub_prop, FunctionType):
                    continue
                self.assertIn(sub, self.functions)

__all__ = []
