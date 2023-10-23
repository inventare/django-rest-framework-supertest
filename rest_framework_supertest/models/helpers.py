from django.db import models

def setup_faker_fields(model_class, **kwargs: dict):
    if not issubclass(model_class, models.Model):
        raise ValueError("Wrapped class must subclass Model.")
    
    if not hasattr(model_class, 'faker_fields'):
        model_class.faker_fields = {}
    if not hasattr(model_class, 'faker_args'):
        model_class.faker_args = {}

    keys = kwargs.keys()
    for field in keys:
        func = kwargs.get(field)
        args = {}
        try:
            _ = [el for el in func]
        except TypeError:
            pass
        else:
            func, args = func
        
        model_class.faker_fields[field] = func
        model_class.faker_args[field] = args

    return model_class
