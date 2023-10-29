from ._utils import unique


def file_extension(fake, category=None):
    """
    Generate a file extension under the specified `category`.

    Args:
        category: If category is None, a random category will be
            used. The list of valid categories include: 'audio',
            'image', 'office', 'text', and 'video'.
    """
    return fake.file_extension(category=category)

def unique_file_extension(fake, category=None):
    """
    Generate a unique file extension under the specified `category`.

    Args:
        category: If category is None, a random category will be
            used. The list of valid categories include: 'audio',
            'image', 'office', 'text', and 'video'.
    """
    return unique(fake, file_extension, category=category)

def file_name(fake, category=None, extension=None):
    """
    Generate a random file name with extension.

    If extension is None, a random extension will be created under
    the hood using file_extension() with the specified category.
    If a value for extension is provided, the value will be used
    instead, and category will be ignored.
    The actual name part itself is generated using word().
    """
    return fake.file_name(category=category, extension=extension)

def unique_file_name(fake, category=None, extension=None):
    """
    Generate a unique random file name with extension.

    If extension is None, a random extension will be created under
    the hood using file_extension() with the specified category.
    If a value for extension is provided, the value will be used
    instead, and category will be ignored.
    The actual name part itself is generated using word().
    """
    return unique(fake, file_name, category=category, extension=extension)

def mime_type(fake, category=None):
    """
    Generate a mime type under the specified category.

    If category is None, a random category will be used.
    The list of valid categories include 'application', 'audio',
    'image', 'message', 'model', 'multipart', 'text', and 'video'.
    """
    return fake.mime_type(category=category)

def unique_mime_type(fake, category=None):
    """
    Generate a unique mime type under the specified category.

    If category is None, a random category will be used.
    The list of valid categories include 'application', 'audio',
    'image', 'message', 'model', 'multipart', 'text', and 'video'.
    """
    return unique(fake, mime_type, category=category)
