from io import BytesIO
from uuid import uuid4

from django.core.files.base import ContentFile
from faker.providers import BaseProvider
from PIL import Image


class ImageProvider(BaseProvider):
    def image(self, width = 50, height = 50, color=(200, 0, 0), format='png', name=None):
        image_file = BytesIO()
        image = Image.new("RGBA", size=(width, height), color=color)
        image.save(image_file, format)
        image_file.seek(0)

        if not name:
            name = "%s.%s" % (str(uuid4()), format)

        return ContentFile(image_file.read(), name)

def add_providers(fake):
    fake.add_provider(ImageProvider)

__all__ = ['ImageProvider', 'add_providers']
