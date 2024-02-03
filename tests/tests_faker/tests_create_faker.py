from django.contrib.auth import get_user_model
from django.test import TestCase

from rest_framework_supertest.models import base, helpers

User = get_user_model()

def _username(_: object) -> str:
    return "any-value-here"

def _first_name(_: object) -> str:
    return "here"

class CreateFakerTestCase(TestCase):
    def setUp(self) -> None:
        if hasattr(User, 'faker_fields'):
            del User.faker_fields
        if hasattr(User, 'faker_args'):
            del User.faker_args

    def test_call_create_faker_without_fields(self) -> None:
        with self.assertRaises(AttributeError):
            base.create_faker(User)

    def test_call_create_faker_without_args(self) -> None:
        User.faker_fields = {}

        with self.assertRaises(AttributeError):
            base.create_faker(User)

    def test_call_create_faker(self) -> None:
        username = _username(None)
        first_name = _first_name(None)
        helpers.setup_faker_fields(
            User,
            username=_username,
            first_name=_first_name,
        )
        user = base.create_faker(User)
        self.assertEqual(user.username, username)
        self.assertEqual(user.first_name, first_name)
        self.assertIsNotNone(user.pk)
        self.assertEqual(user.email, '')

    def test_call_create_faker_data_with_one_field(self) -> None:
        username = _username(None)
        helpers.setup_faker_fields(
            User,
            username=_username,
        )
        user = base.create_faker(User)
        self.assertEqual(user.username, username)
        self.assertEqual(user.first_name, '')
        self.assertIsNotNone(user.pk)
        self.assertEqual(user.email, '')

    def test_call_create_faker_data_with_override(self) -> None:
        username = _username(None)
        first_name = _first_name(None)
        email = 'example@example.com.br'
        helpers.setup_faker_fields(
            User,
            username=_username,
            first_name=_first_name,
        )
        user = base.create_faker(User, {'email': email})
        self.assertEqual(user.username, username)
        self.assertEqual(user.first_name, first_name)
        self.assertIsNotNone(user.pk)
        self.assertEqual(user.email, email)

    def test_call_create_faker_data_without_save(self) -> None:
        username = _username(None)
        first_name = _first_name(None)
        email = 'example@example.com.br'
        helpers.setup_faker_fields(
            User,
            username=_username,
            first_name=_first_name,
        )
        user = base.create_faker(User, {'email': email}, save=False)
        self.assertEqual(user.username, username)
        self.assertEqual(user.first_name, first_name)
        self.assertIsNone(user.pk)
        self.assertEqual(user.email, email)

__all__ = []
