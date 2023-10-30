from io import BytesIO
from typing import Optional
from uuid import uuid4

from django.core.files.base import ContentFile
from faker.providers import BaseProvider
from PIL import Image


class ImageProvider(BaseProvider):
    """Provider to create django ContentFile with images."""

    def image(
        self,
        width: int = 50,
        height: int = 50,
        color: (int, int, int) = (200, 0, 0),
        image_format: str = 'png',
        name: Optional[str] = None,
    ) -> ContentFile:
        """
        Create an image with one color.

        Args:
            width: the width of the image.
            height: the height of the image.
            color: the image color.
            image_format: the format to save the image.
            name: the file name to save. If is not set, a uuid4() with the
              image_format is used to save.
        """
        image_file = BytesIO()
        image = Image.new("RGBA", size=(width, height), color=color)
        image.save(image_file, image_format)
        image_file.seek(0)

        if not name:
            name = f"{uuid4()!s}.{image_format}"

        return ContentFile(image_file.read(), name)

def add_providers(fake: object) -> None:
    """Add providers to the fake instance."""
    fake.add_provider(ImageProvider)

__all__ = ['ImageProvider', 'add_providers']
