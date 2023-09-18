from django.db import models

def setup_faker_fields(model_class, **kwargs: dict):
    if not issubclass(model_class, models.Model):
        raise ValueError("Wrapped class must subclass Model.")
    
    if not hasattr(model_class, 'faker_fields'):
        model_class.faker_fields = {}

    keys = kwargs.keys()
    for field in keys:
        func = kwargs.get(field)
        model_class.faker_fields[field] = func

    return model_class
