# ADR 0001: Faker Shortcuts

October 2023 . [Eduardo Oliveira](https://github.com/EduardoJM)

## Context

When we introduced the [faker](https://faker.readthedocs.io/) inside this project, we decided to use only one `faker.Faker` instance for all model generations. The reason for this is to grant the `faker.unique` generated values are really unique for various models context with the possibility to clear the [already seen values](https://faker.readthedocs.io/en/master/fakerclass.html#unique-values).

To use only one `faker.Fake` instance we decided to parse this as the **first argument** of the functions to generate field values. To made it more easy to write generator for model fields, we need to write shortcuts for the faker.

## Decision Drivers

- Easy to set the methods in the `@faker_fields` decorator.
- The shortcuts can receive arguments to configure the faker methods.
- Must include the most part of standard providers of the faker.

## Decision

We decided to write shortcuts (this name is an inspiration from the original `django.shortcuts` package) with the format bellow, with the optional named `**kwargs`:

```python
def country_code(fake, representation='alpha-2'):
    """Generate a country code"""
    return fake.country_code(representation=representation)
```
To use the shortcuts is very easy, using the `@faker_fields` decorator:

```python
from django.db import models
from rest_framework_supertest import shotcuts
from rest_framework_supertest.models.decorators import faker_fields

@faker_fields(
    title=shotcuts.name,
    mime=(shotcuts.mime_type, { 'category': 'audio' })
)
class Book(models.Model):
    title = models.CharField()
    mime = models.TextField()
```

## Related Issues

When this ADR was created, we have some related issues for this decision:

- [#21 [feature] create an shortcut module and define methods to basic faker methods](https://github.com/inventare/django-rest-framework-supertest/issues/21)
- [#45 [feature] add support for parsing arguments to fake function](https://github.com/inventare/django-rest-framework-supertest/issues/45)
- [#47 [documentation] explain better arguments of faker shotcuts](https://github.com/inventare/django-rest-framework-supertest/issues/47)
- [#62 [feature] create shotcuts for file generation faker with real support for directly set model files](https://github.com/inventare/django-rest-framework-supertest/issues/62)
- [#63 [feature] create json shotcuts](https://github.com/inventare/django-rest-framework-supertest/issues/63)
