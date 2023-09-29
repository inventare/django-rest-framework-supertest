from django.test import TestCase
from django.contrib.auth import get_user_model
from rest_framework_supertest.models import helpers, decorators

User = get_user_model()

class EmptyClass:
    pass

class SetupFakerFieldsTestCase(TestCase):
    def setUp(self):
        if hasattr(User, 'faker_fields'):
            del User.faker_fields
    
    def test_call_setup_faker_fields_without_model(self):
        with self.assertRaises(ValueError):
            helpers.setup_faker_fields(EmptyClass)

    def test_call_setup_faker_without_fields(self):
        extension = helpers.setup_faker_fields(User)
        self.assertIsNotNone(extension)
        self.assertEqual(extension.faker_fields, {})
        self.assertEqual(extension.__name__, User.__name__)

    def test_call_setup_faker_with_one_field(self):
        fn = lambda faker: 'any-value-here'
        extension = helpers.setup_faker_fields(User, username=fn)
        self.assertIsNotNone(extension)
        self.assertEqual(extension.faker_fields, { 'username': fn })
        self.assertEqual(extension.__name__, User.__name__)

    def test_call_setup_faker_with_multiple_fields(self):
        fn_username = lambda faker: 'any-value-here'
        fn_first_name = lambda faker: 'here'
        extension = helpers.setup_faker_fields(User, username=fn_username, first_name=fn_first_name)
        self.assertIsNotNone(extension)
        self.assertEqual(extension.faker_fields, { 'username': fn_username, 'first_name': fn_first_name })
        self.assertEqual(extension.__name__, User.__name__)

    def test_decorator_faker_fields_without_model(self):
        wrap = decorators.faker_fields()
        with self.assertRaises(ValueError):
            wrap(EmptyClass)

    def test_decorator_faker__fields_without_fields(self):
        wrap = decorators.faker_fields()
        wrap(User)
        
        self.assertEqual(User.faker_fields, {})

    def test_decorator_faker__fields_with_one_field(self):
        fn = lambda faker: 'any-value-here'
        wrap = decorators.faker_fields(username=fn)
        wrap(User)
        
        self.assertEqual(User.faker_fields, { 'username': fn })

    def test_decorator_faker__fields_with_multiple_fields(self):
        fn_username = lambda faker: 'any-value-here'
        fn_first_name = lambda faker: 'here'
        wrap = decorators.faker_fields(username=fn_username, first_name=fn_first_name)
        wrap(User)
        
        self.assertEqual(User.faker_fields, { 'username': fn_username, 'first_name': fn_first_name })
