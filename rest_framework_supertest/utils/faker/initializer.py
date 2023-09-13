from faker import Faker
from django.conf import settings
from django.utils.module_loading import import_string
from rest_framework_supertest import settings as faker_settings

def initialize_faker():
    locale = getattr(settings, 'FAKER_LOCALE', faker_settings.FAKER_LOCALE)
    init_providers = getattr(settings, 'FAKER_ADD_PROVIDERS', faker_settings.FAKER_ADD_PROVIDERS)

    fake = Faker(locale)
    try:
        func = import_string(init_providers)
        func(fake)
    except ImportError:
        msg = "Could not import FAKER_ADD_PROVIDERS '%s'" % init_providers
        raise ImportError(msg)

    return fake

__all__ = ['initialize_faker']
