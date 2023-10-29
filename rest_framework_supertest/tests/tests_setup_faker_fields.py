from django.contrib.auth import get_user_model
from django.test import TestCase

from rest_framework_supertest.models import decorators, helpers

User = get_user_model()

class EmptyClass:
    pass

class SetupFakerFieldsTestCase(TestCase):
    def setUp(self):
        if hasattr(User, 'faker_fields'):
            del User.faker_fields
        if hasattr(User, 'faker_args'):
            del User.faker_args

    def test_call_setup_faker_fields_without_model(self):
        with self.assertRaises(ValueError):
            helpers.setup_faker_fields(EmptyClass)

    def test_call_setup_faker_without_fields(self):
        extension = helpers.setup_faker_fields(User)
        self.assertIsNotNone(extension)
        self.assertEqual(extension.faker_fields, {})
        self.assertEqual(extension.faker_args, {})
        self.assertEqual(extension.__name__, User.__name__)

    def test_call_setup_faker_with_one_field(self):
        fn = lambda faker: 'any-value-here'
        extension = helpers.setup_faker_fields(User, username=fn)
        self.assertIsNotNone(extension)
        self.assertEqual(extension.faker_fields, { 'username': fn })
        self.assertEqual(extension.faker_args, { 'username': {} })
        self.assertEqual(extension.__name__, User.__name__)

    def test_call_setup_faker_with_one_field_args(self):
        fn = lambda faker: 'any-value-here'
        extension = helpers.setup_faker_fields(User, username=(fn, { 'custom_arg': True }))
        self.assertIsNotNone(extension)
        self.assertEqual(extension.faker_fields, { 'username': fn })
        self.assertEqual(extension.faker_args, { 'username': { 'custom_arg': True } })
        self.assertEqual(extension.__name__, User.__name__)

    def test_call_setup_faker_with_multiple_fields(self):
        fn_username = lambda faker: 'any-value-here'
        fn_first_name = lambda faker: 'here'
        extension = helpers.setup_faker_fields(User, username=fn_username, first_name=fn_first_name)
        self.assertIsNotNone(extension)
        self.assertEqual(extension.faker_fields, { 'username': fn_username, 'first_name': fn_first_name })
        self.assertEqual(extension.faker_args, { 'username': {}, 'first_name': {} })
        self.assertEqual(extension.__name__, User.__name__)

    def test_call_setup_faker_with_multiple_fields_args(self):
        fn_username = lambda faker: 'any-value-here'
        fn_first_name = lambda faker: 'here'
        extension = helpers.setup_faker_fields(
            User,
            username=(fn_username, {'a': True}),
            first_name=(fn_first_name, {'b': 'any-value'}),
        )
        self.assertIsNotNone(extension)
        self.assertEqual(extension.faker_fields, { 'username': fn_username, 'first_name': fn_first_name })
        self.assertEqual(extension.faker_args, { 'username': { 'a': True }, 'first_name': { 'b': 'any-value' } })
        self.assertEqual(extension.__name__, User.__name__)

    def test_decorator_faker_fields_without_model(self):
        wrap = decorators.faker_fields()
        with self.assertRaises(ValueError):
            wrap(EmptyClass)

    def test_decorator_faker__fields_without_fields(self):
        wrap = decorators.faker_fields()
        wrap(User)

        self.assertEqual(User.faker_fields, {})
        self.assertEqual(User.faker_args, {})

    def test_decorator_faker__fields_with_one_field(self):
        fn = lambda faker: 'any-value-here'
        wrap = decorators.faker_fields(username=fn)
        wrap(User)

        self.assertEqual(User.faker_fields, { 'username': fn })
        self.assertEqual(User.faker_args, { 'username': {} })

    def test_decorator_faker__fields_with_one_field_args(self):
        fn = lambda faker: 'any-value-here'
        wrap = decorators.faker_fields(username=(fn, { 'a': False }))
        wrap(User)

        self.assertEqual(User.faker_fields, { 'username': fn })
        self.assertEqual(User.faker_args, { 'username': { 'a': False } })

    def test_decorator_faker__fields_with_multiple_fields(self):
        fn_username = lambda faker: 'any-value-here'
        fn_first_name = lambda faker: 'here'
        wrap = decorators.faker_fields(username=fn_username, first_name=fn_first_name)
        wrap(User)

        self.assertEqual(User.faker_fields, { 'username': fn_username, 'first_name': fn_first_name })
        self.assertEqual(User.faker_args, { 'username': {}, 'first_name': {} })

    def test_decorator_faker__fields_with_multiple_fields_args(self):
        fn_username = lambda faker: 'any-value-here'
        fn_first_name = lambda faker: 'here'
        wrap = decorators.faker_fields(username=(fn_username, { 'a': 'B' }), first_name=fn_first_name)
        wrap(User)

        self.assertEqual(User.faker_fields, { 'username': fn_username, 'first_name': fn_first_name })
        self.assertEqual(User.faker_args, { 'username': { 'a': 'B' }, 'first_name': {} })
