from ._utils import unique


def country_calling_code(fake: object) -> str:
    """Generate a country calling code."""
    return fake.country_calling_code()

def unique_country_calling_code(fake: object) -> str:
    """Generate a unique country calling code."""
    return unique(fake, country_calling_code)

def phone_number(fake: object) -> str:
    """Generate a phone number."""
    return fake.phone_number()

def unique_phone_number(fake: object) -> str:
    """Generate a unique phone number."""
    return unique(fake, phone_number)
