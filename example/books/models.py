from django.db import models
from rest_framework_supertest.models.decorators import faker_field
from rest_framework_supertest.models.base import FakerModelMixin


@faker_field('title', lambda fake : fake.name())
class Book(FakerModelMixin, models.Model):
    title = models.CharField(max_length=160)
