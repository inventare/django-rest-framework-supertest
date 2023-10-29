from rest_framework_supertest.models.helpers import setup_faker_fields


def faker_fields(**kwargs: dict):
    def wrapper(model_class):
        return setup_faker_fields(model_class, **kwargs)

    return wrapper
