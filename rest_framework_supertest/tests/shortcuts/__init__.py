from typing import Optional
from unittest.mock import MagicMock

from django.test import TestCase


class ShortcutTestCase(TestCase):
    """A TestCase to help testint faker shortcuts functions."""

    def get_faker_mock(
        self,
        paths: Optional[list[str]] = None,
    ) -> (MagicMock, MagicMock):
        """
        Create a mock for `faker.Faker()` instance.

        Create a mock, with determinated paths, for the `faker.Faker()` instance
        to run the shortcuts tests.

        Args:
            paths: the paths to create `unittest.mock.MagicMock` on the
              `faker.Faker` mock. e.g: using `['unique', 'method']` then
              the `faker.Faker` mock has the `fake.unique.method()` mocked.

        Returns:
            A tuple containing two mocks. The first is the `faker.Faker` mock
            and the second is the last mocked function of the path.
        """
        if not paths:
            paths = []
        fake = MagicMock()
        last = fake
        for path in paths:
            setattr(last, path, MagicMock())
            last = getattr(last, path)
        return fake, last

    def exec_test(
        self,
        paths: list[str],
        module: object,
        function_name: str,
        **kwargs: dict,
    ) -> None:
        """
        Execute a test for a shortcut.

        Create the `faker.Faker` mock, call the shortcut function
        and assert if the mocked function is called.

        Args:
            paths: the paths to be called on the faker. e.g: `['unique', 'name']`
              indicate that the `fake.unique.name()` should be called when call
              the shortcut.
            module: the module containing the shortcut functions.
            function_name: the shortcut to test function name.
            **kwargs: arguments to be parsed to the call of the shortcut function.
        """
        fake, mock = self.get_faker_mock(paths)

        fn = getattr(module, function_name)
        fn(fake, **kwargs)

        mock.assert_called_once_with(**kwargs)
