from typing import Optional

from ._utils import unique


def cryptocurrency_code(fake: object) -> str:
    """Generate a cryptocurrency code."""
    return fake.cryptocurrency_code()

def unique_cryptocurrency_code(fake: object) -> str:
    """Generate a unique cryptocurrency code."""
    return unique(fake, cryptocurrency_code)

def cryptocurrency_name(fake: object) -> str:
    """Generate a cryptocurrency name."""
    return fake.cryptocurrency_name()

def unique_cryptocurrency_name(fake: object) -> str:
    """Generate a unique cryptocurrency name."""
    return unique(fake, cryptocurrency_name)

def currency_code(fake: object) -> str:
    """Generate a currency code."""
    return fake.currency_code()

def unique_currency_code(fake: object) -> str:
    """Generate a unique currency code."""
    return unique(fake, currency_code)

def currency_name(fake: object) -> str:
    """Generate a currency name."""
    return fake.currency_name()

def unique_currency_name(fake: object) -> str:
    """Generate a unique currency name."""
    return unique(fake, currency_name)

def currency_symbol(fake: object, code: Optional[str] = None) -> str:
    """Generate a currency symbol."""
    return fake.currency_symbol(code=code)

def unique_currency_symbol(fake: object, code: Optional[str] = None) -> str:
    """Generate a unique currency symbol."""
    return unique(fake, currency_symbol, code=code)
