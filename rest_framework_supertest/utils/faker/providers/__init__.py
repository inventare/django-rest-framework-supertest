from .image import ImageProvider
from .image import ImageProvider

def add_providers(fake):
    fake.add_provider(ImageProvider)

__all__ = ['ImageProvider', 'add_providers']
