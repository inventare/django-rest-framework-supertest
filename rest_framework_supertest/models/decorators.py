from typing import Callable

from django.db import models

from rest_framework_supertest.models.helpers import setup_faker_fields


def faker_fields(**kwargs: dict) -> Callable:
    """
    Setup faker fields for an model class.

    Register `faker_fields` and `faker_args` inside the model to store the
    faker model constructor properties.
    """
    def wrapper(model_class: type[models.Model]) -> type[models.Model]:
        return setup_faker_fields(model_class, **kwargs)

    return wrapper
