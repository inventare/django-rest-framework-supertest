import io
import uuid
from typing import Optional

from django.core.files import File

from ._utils import unique


def file_extension(fake: object, category: Optional[str] = None) -> str:
    """
    Generate a file extension under the specified `category`.

    Args:
        fake: The `Faker` instance.
        category: If category is None, a random category will be
          used. The list of valid categories include: 'audio',
          'image', 'office', 'text', and 'video'.
    """
    return fake.file_extension(category=category)

def unique_file_extension(fake: object, category: Optional[str] = None) -> str:
    """
    Generate a unique file extension under the specified `category`.

    Args:
        fake: The `Faker` instance.
        category: If category is None, a random category will be
          used. The list of valid categories include: 'audio',
          'image', 'office', 'text', and 'video'.
    """
    return unique(fake, file_extension, category=category)

def file_name(
    fake: object,
    category: Optional[str] = None,
    extension: Optional[str] = None,
) -> str:
    """
    Generate a random file name with extension.

    Args:
        fake: The `Faker` instance.
        category: If category is None, a random category will be
          used. The list of valid categories include: 'audio',
          'image', 'office', 'text', and 'video'.
        extension: If extension is None, a random extension will be
          created under the hood using file_extension() with the
          specified category. If a value for extension is provided,
          the value will be used instead, and category will be ignored.
    """
    return fake.file_name(category=category, extension=extension)

def unique_file_name(
    fake: object,
    category: Optional[str] = None,
    extension: Optional[str] = None,
) -> str:
    """
    Generate a unique random file name with extension.

    Args:
        fake: The `Faker` instance.
        category: If category is None, a random category will be
          used. The list of valid categories include: 'audio',
          'image', 'office', 'text', and 'video'.
        extension: If extension is None, a random extension will be
          created under the hood using file_extension() with the
          specified category. If a value for extension is provided,
          the value will be used instead, and category will be ignored.
    """
    return unique(fake, file_name, category=category, extension=extension)

def mime_type(fake: object, category: Optional[str] = None) -> str:
    """
    Generate a mime type under the specified category.

    Args:
        fake: The `Faker` instance.
        category: If category is None, a random category will be
          used. The list of valid categories include: 'audio',
          'image', 'office', 'text', and 'video'.
    """
    return fake.mime_type(category=category)

def unique_mime_type(fake: object, category: Optional[str] = None) -> str:
    """
    Generate a unique mime type under the specified category.

    Args:
        fake: The `Faker` instance.
        category: If category is None, a random category will be
          used. The list of valid categories include: 'audio',
          'image', 'office', 'text', and 'video'.
    """
    return unique(fake, mime_type, category=category)

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

PDF_WIDTH = 2480
PDF_HEIGHT = 3508

def pdf(fake: object, file_name: Optional[str] = None) -> File:
    """
    Generate a pdf file to store it to django file field.

    Args:
        fake: The `Faker` instance.
        file_name: The file name to store into `django.core.files.File` instance.
    """
    data = fake.image(size=(PDF_WIDTH, PDF_HEIGHT), image_format='pdf')
    buffer = io.BytesIO(data)

    if not file_name:
        name = str(uuid.uuid4())
        file_name = f"{name}.pdf"

    return File(buffer, file_name)

def zip_file(
    fake: object,
    file_name: Optional[str] = None,
    uncompressed_size: int = 65536,
    num_files: int = 1,
    min_file_size: int = 4096,
    compression: Optional[str] = None,
) -> File:
    """
    Generate a zip file to store it to django file field.

    Args:
        fake: The `Faker` instance.
        file_name: The file name to store into `django.core.files.File` instance.
        uncompressed_size: The total size of files before compression, default: 16KiB.
        num_files: the number of files archived in resulting zip file, default: 1.
        min_file_size: the minimum size of each file before compression, default: 4KiB.
        compression: No compression is used by default, but setting compression to one
          of the values listed below will use the corresponding compression type:
            - `bzip2` or `bz2` for BZIP2
            - `lzma` or `xz` for LZMA
            - `defalte`, `gzip` or `gz` for GZIP.
    """
    data = fake.zip(
        uncompressed_size=uncompressed_size,
        num_files=num_files,
        min_file_size=min_file_size,
        compression=compression,
    )
    buffer = io.BytesIO(data)

    if not file_name:
        name = str(uuid.uuid4())
        file_name = f"{name}.zip"

    return File(buffer, file_name)
