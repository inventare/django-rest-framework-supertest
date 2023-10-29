from typing import Optional

from django.db import models

from rest_framework_supertest.utils.faker import fake


def create_faker(
    model_class: type[models.Model],
    data: Optional[dict] = None,
    *,
    save: bool = True,
) -> models.Model:
    """
    Create a model from faker data arguments.

    Uses the `faker_fields` and `faker_args` of the model class to
    create an faker model.

    Args:
        model_class: The class of the model to create faker model.
        data: Additional data to override the default data setuped
          from faker. This is used to customize fields to some
          specific test cases.
        save: If true, the method uses the `model_class.objects.create()` to
          create and save the item at database. Otherwise, the method uses the
          model_class initializer to only create and not save the item.

    Returns:
        A instance of the `model_class`.
    """
    faker_fields = model_class.faker_fields
    faker_args = model_class.faker_args
    fields = faker_fields.keys()
    create_dict = {}
    for field in fields:
        args = faker_args.get(field) or {}
        create_dict[field] = faker_fields[field](fake, **args)

    if not data:
        data = {}

    create_dict = {
        **create_dict,
        **data,
    }

    if save:
        return model_class.objects.create(**create_dict)
    return model_class(**create_dict)
