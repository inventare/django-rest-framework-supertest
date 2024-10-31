from unittest.mock import MagicMock

from django.contrib.auth import get_user_model
from django.test import TestCase

from rest_framework_supertest.models import base, helpers

User = get_user_model()


def _username(_: object) -> str:
    return "any-value-here"


def _first_name(_: object) -> str:
    return "here"


class CreateFakerDataTestCase(TestCase):
    def setUp(self) -> None:
        if hasattr(User, "faker_fields"):
            del User.faker_fields
        if hasattr(User, "faker_args"):
            del User.faker_args

    def test_call_create_faker_data_without_fields(self) -> None:
        with self.assertRaises(AttributeError):
            base.create_faker_data(User)

    def test_call_create_faker_data_without_args(self) -> None:
        User.faker_fields = {}

        with self.assertRaises(AttributeError):
            base.create_faker_data(User)

    def test_call_create_faker_data(self) -> None:
        helpers.setup_faker_fields(
            User,
            username=_username,
            first_name=_first_name,
        )
        expected = {
            "username": _username(None),
            "first_name": _first_name(None),
        }
        data = base.create_faker_data(User)
        self.assertDictEqual(data, expected)

    def test_call_create_faker_data_with_one_field(self) -> None:
        helpers.setup_faker_fields(
            User,
            username=_username,
        )
        expected = {
            "username": _username(None),
        }
        data = base.create_faker_data(User)
        self.assertDictEqual(data, expected)

    def test_call_create_faker_data_with_override(self) -> None:
        helpers.setup_faker_fields(
            User,
            username=_username,
        )
        mail = "example@example.com.br"
        expected = {
            "username": _username(None),
            "email": mail,
        }
        data = base.create_faker_data(User, {"email": mail})
        self.assertDictEqual(data, expected)

    def test_call_create_faker_data_with_overrides_not_call_shortcut(self) -> None:
        username_shortcut = MagicMock()
        username_shortcut.return_value = "any"

        helpers.setup_faker_fields(
            User,
            username=(username_shortcut, {}),
        )
        mail = "example@example.com.br"
        username = "new-user-name"
        expected = {
            "username": username,
            "email": mail,
        }
        data = base.create_faker_data(User, {"email": mail, "username": username})
        self.assertDictEqual(data, expected)
        username_shortcut.assert_not_called()


__all__ = []
