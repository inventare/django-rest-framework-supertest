from typing import Callable, Type

from django.db import models

from rest_framework_supertest.models.helpers import setup_faker_fields


def faker_fields(**kwargs: dict) -> Callable:
    """
    Setups faker fields for a model class.

    Register `faker_fields` and `faker_args` inside the model to store the
    faker model constructor properties.
    """
    def wrapper(model_class: Type[models.Model]) -> Type[models.Model]:
        return setup_faker_fields(model_class, **kwargs)

    return wrapper
