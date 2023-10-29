from ._utils import unique


def isbn10(fake: object, separator: str = "-") -> str:
    """Generate a ISBN10."""
    return fake.isbn10(separator=separator)

def unique_isbn10(fake: object, separator: str = '') -> str:
    """Generate a unique ISBN10."""
    return unique(fake, isbn10, separator=separator)

def isbn13(fake: object, separator: str = "-") -> str:
    """Generate a ISBN13."""
    return fake.isbn13(separator=separator)

def unique_isbn13(fake: object, separator: str = '') -> str:
    """Generate a unique ISBN13."""
    return unique(fake, isbn13, separator=separator)
