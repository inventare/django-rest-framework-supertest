from django.db import models
from rest_framework_supertest.models.decorators import faker_fields
from .faker import BookFaker

@faker_fields(**BookFaker)
class Book(models.Model):
    title = models.CharField(max_length=160)
    description = models.TextField()
