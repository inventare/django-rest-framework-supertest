import io
import uuid
from typing import Optional

from django.core.files import File


def image(
    fake: object,
    width: int = 256,
    height: int = 256,
    image_format: str = 'png',
    file_name: Optional[str] = None,
) -> File:
    """
    Generate a image to store it to django file field.

    Args:
        fake: The `Faker` instance.
        width: The image width.
        height: The image height.
        image_format: The image_format to store. See Pillow image file formats.
        file_name: The file name to store into `django.core.files.File` instance.
    """
    data = fake.image(size=(width, height), image_format=image_format)
    buffer = io.BytesIO(data)

    if not file_name:
        name = str(uuid.uuid4())
        file_name = f"{name}.{image_format}"

    return File(buffer, file_name)
