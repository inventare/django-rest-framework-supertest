def faker_field(field: str, func):
    from django.db.models import Model

    def wrapper(model_class): 
        if not isinstance(model_class, Model):
            raise ValueError("Wrapped class must subclass Model.")
        
        if not hasattr(model_class, 'faker'):
            model_class.faker_fields = {}
        
        model_class.faker_fields[field] = func

        return model_class

    return wrapper

__all__ = ['faker_field']
