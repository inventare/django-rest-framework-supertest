from typing import Any
from unittest.mock import MagicMock

class FakerMockMixin:
    def get_faker_mock(self, paths=[]):
        fake = MagicMock()
        last = fake
        for path in paths:
            setattr(last, path, MagicMock())
            last = getattr(last, path)
        return fake, last
    
    def exec_test(self, paths: list[str], module: Any, function_name: str, **kwargs):
        fake, mock = self.get_faker_mock(paths)

        fn = getattr(module, function_name)
        fn(fake, **kwargs)

        mock.assert_called_once_with(**kwargs)
