from typing import Type, Optional
from django.db import models

def foreign_key(
    fake: object,
    model_class: Type[models.Model],
    custom_data: Optional[dict] = None,
):
    """Generate a foreign key entity."""
    from rest_framework_supertest.models.base import create_faker
    return create_faker(model_class, custom_data)
