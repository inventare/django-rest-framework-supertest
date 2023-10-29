from django.db import models


def setup_faker_fields(
    model_class: type[models.Model],
    **kwargs: dict,
) -> type[models.Model]:
    """
    Setup faker fields for an model class.

    Register `faker_fields` and `faker_args` inside the model to store the
    faker model constructor properties.
    """
    if not issubclass(model_class, models.Model):
        msg = "Wrapped class must subclass Model."
        raise TypeError(msg)

    if not hasattr(model_class, 'faker_fields'):
        model_class.faker_fields = {}
    if not hasattr(model_class, 'faker_args'):
        model_class.faker_args = {}

    keys = kwargs.keys()
    for field in keys:
        func = kwargs.get(field)
        args = {}
        try:
            _ = list(func)
        except TypeError:
            pass
        else:
            func, args = func

        model_class.faker_fields[field] = func
        model_class.faker_args[field] = args

    return model_class
