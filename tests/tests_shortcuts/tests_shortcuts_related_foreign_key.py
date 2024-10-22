from django.test import TestCase
from rest_framework_supertest.shortcuts import foreign_key
from rest_framework_supertest.models.helpers import setup_faker_fields
from rest_framework_supertest.models.base import create_faker
from tests.models import RelatedParent, RelatedChild


class RelatedForeignShortcutsTests(TestCase):
    name = 'my name'

    def name_fn(self, faker):
        return self.name

    def setUp(self):
        if hasattr(RelatedParent, 'faker_fields'):
            del RelatedParent.faker_fields
        if hasattr(RelatedParent, 'faker_args'):
            del RelatedParent.faker_args
        if hasattr(RelatedChild, 'faker_fields'):
            del RelatedChild.faker_fields
        if hasattr(RelatedChild, 'faker_args'):
            del RelatedChild.faker_args
        
        setup_faker_fields(
            RelatedParent,
            name=self.name_fn,
        )
        setup_faker_fields(
            RelatedChild,
            parent=(foreign_key, { 'model_class': RelatedParent })
        )

    def test_foreign_key_creation(self):
        child = create_faker(RelatedChild)
        
        self.assertIsNotNone(child)
        self.assertIsNotNone(child.parent)
        self.assertEqual(RelatedChild.objects.count(), 1)
        self.assertEqual(RelatedParent.objects.count(), 1)
        self.assertEqual(RelatedParent.objects.first().name, self.name)

__all__ = []
