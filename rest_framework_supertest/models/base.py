from typing import Optional

from rest_framework_supertest.utils.faker import fake


def create_faker(model_class, data: Optional[dict] = None, save = True):
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
