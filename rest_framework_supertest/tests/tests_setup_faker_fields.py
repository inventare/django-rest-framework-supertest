from django.contrib.auth import get_user_model
from django.test import TestCase

from rest_framework_supertest.models import decorators, helpers

User = get_user_model()

class EmptyClass:
    pass

def _username(_: object) -> str:
    return "any-value-here"

def _first_name(_: object) -> str:
    return "here"

class SetupFakerFieldsTestCase(TestCase):
    def setUp(self) -> None:
        if hasattr(User, 'faker_fields'):
            del User.faker_fields
        if hasattr(User, 'faker_args'):
            del User.faker_args

    def test_call_setup_faker_fields_without_model(self) -> None:
        with self.assertRaises(ValueError):
            helpers.setup_faker_fields(EmptyClass)

    def test_call_setup_faker_without_fields(self) -> None:
        extension = helpers.setup_faker_fields(User)
        self.assertIsNotNone(extension)
        self.assertEqual(extension.faker_fields, {})
        self.assertEqual(extension.faker_args, {})
        self.assertEqual(extension.__name__, User.__name__)

    def test_call_setup_faker_with_one_field(self) -> None:
        extension = helpers.setup_faker_fields(User, username=_username)
        self.assertIsNotNone(extension)
        self.assertEqual(extension.faker_fields, {'username': _username})
        self.assertEqual(extension.faker_args, {'username': {}})
        self.assertEqual(extension.__name__, User.__name__)

    def test_call_setup_faker_with_one_field_args(self) -> None:
        extension = helpers.setup_faker_fields(
            User,
            username=(_username, {'custom_arg': True}),
        )
        self.assertIsNotNone(extension)
        self.assertEqual(extension.faker_fields, {'username': _username})
        self.assertEqual(extension.faker_args, {'username': {'custom_arg': True}})
        self.assertEqual(extension.__name__, User.__name__)

    def test_call_setup_faker_with_multiple_fields(self) -> None:
        extension = helpers.setup_faker_fields(
            User,
            username=_username,
            first_name=_first_name,
        )
        self.assertIsNotNone(extension)
        self.assertEqual(
            extension.faker_fields,
            {'username': _username, 'first_name': _first_name},
        )
        self.assertEqual(extension.faker_args, { 'username': {}, 'first_name': {}})
        self.assertEqual(extension.__name__, User.__name__)

    def test_call_setup_faker_with_multiple_fields_args(self) -> None:
        extension = helpers.setup_faker_fields(
            User,
            username=(_username, {'a': True}),
            first_name=(_first_name, {'b': 'any-value'}),
        )
        self.assertIsNotNone(extension)
        self.assertEqual(
            extension.faker_fields,
            {'username': _username, 'first_name': _first_name},
        )
        self.assertEqual(
            extension.faker_args,
            {'username': {'a': True}, 'first_name': {'b': 'any-value'}},
        )
        self.assertEqual(extension.__name__, User.__name__)

    def test_decorator_faker_fields_without_model(self) -> None:
        wrap = decorators.faker_fields()
        with self.assertRaises(ValueError):
            wrap(EmptyClass)

    def test_decorator_faker__fields_without_fields(self) -> None:
        wrap = decorators.faker_fields()
        wrap(User)

        self.assertEqual(User.faker_fields, {})
        self.assertEqual(User.faker_args, {})

    def test_decorator_faker__fields_with_one_field(self) -> None:
        wrap = decorators.faker_fields(username=_username)
        wrap(User)

        self.assertEqual(User.faker_fields, {'username': _username})
        self.assertEqual(User.faker_args, {'username': {}})

    def test_decorator_faker__fields_with_one_field_args(self) -> None:
        wrap = decorators.faker_fields(username=(_username, {'a': False}))
        wrap(User)

        self.assertEqual(User.faker_fields, {'username': _username})
        self.assertEqual(User.faker_args, {'username': {'a': False}})

    def test_decorator_faker__fields_with_multiple_fields(self) -> None:
        wrap = decorators.faker_fields(username=_username, first_name=_first_name)
        wrap(User)

        self.assertEqual(
            User.faker_fields,
            {'username': _username, 'first_name': _first_name},
        )
        self.assertEqual(User.faker_args, {'username': {}, 'first_name': {}})

    def test_decorator_faker__fields_with_multiple_fields_args(self) -> None:
        wrap = decorators.faker_fields(
            username=(_username, {'a': 'B'}),
            first_name=_first_name,
        )
        wrap(User)

        self.assertEqual(
            User.faker_fields,
            {'username': _username, 'first_name': _first_name},
        )
        self.assertEqual(User.faker_args, {'username': {'a': 'B'}, 'first_name': {}})

__all__ = []
