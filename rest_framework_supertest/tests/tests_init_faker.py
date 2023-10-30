from unittest.mock import MagicMock, patch

from django.test import TestCase
from django.test.utils import override_settings


def add_providers(_: object) -> None:
    pass

class InitFakerTestCase(TestCase):
    @override_settings(FAKER_LOCALE='en_US')
    @patch('rest_framework_supertest.utils.faker.initializer.Faker')
    def test_setup_locale_from_settings(self, mock: MagicMock) -> None:
        from rest_framework_supertest.utils.faker.initializer import initialize_faker
        fake = initialize_faker()
        mock.assert_called_once_with('en_US')
        self.assertIsNotNone(fake)

    @override_settings(FAKER_ADD_PROVIDERS='rest_framework_supertest.tests.tests_init_faker.add_providers')
    @patch('rest_framework_supertest.tests.tests_init_faker.add_providers')
    def test_setup_init_providers_from_settings(self, mock: MagicMock) -> None:
        from rest_framework_supertest.utils.faker.initializer import initialize_faker
        fake = initialize_faker()
        mock.assert_called_once()
        self.assertIsNotNone(fake)

    @override_settings(FAKER_ADD_PROVIDERS='rest_framework_supertest.tests.tests_init_faker.fake')
    def test_setup_init_providers_with_invalid_func(self) -> None:
        from rest_framework_supertest.utils.faker.initializer import initialize_faker
        with self.assertRaises(ImportError):
            initialize_faker()

__all__ = []
