from django.db import models
from rest_framework_supertest.models.decorators import faker_field

@faker_field('title', lambda fake : fake.name())
class Book(models.Model):
    title = models.CharField(max_length=160)
