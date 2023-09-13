def faker_fields(**kwargs: dict):
    from django.db import models

    def wrapper(model_class): 
        if not issubclass(model_class, models.Model):
            raise ValueError("Wrapped class must subclass Model.")
        
        if not hasattr(model_class, 'faker_fields'):
            model_class.faker_fields = {}
        
        keys = kwargs.keys()
        for field in keys:
            func = kwargs.get(field)
            model_class.faker_fields[field] = func

        return model_class

    return wrapper

def faker_field_image(field: str):
    from django.db import models

    def wrapper(model_class): 
        if not issubclass(model_class, models.Model):
            raise ValueError("Wrapped class must subclass Model.")
        
        raise NotImplementedError("Implements here!")
        
        return model_class
    
    return wrapper
    
__all__ = ['faker_field', 'faker_field_image']
