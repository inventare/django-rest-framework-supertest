from ._utils import unique
from .typing import CountryCodeType


def address(fake: object) -> str:
    """Generate a address."""
    return fake.address()

def unique_address(fake: object) -> str:
    """Generate a unique address."""
    return unique(fake, address)

def building_number(fake: object) -> str:
    """Generate a building number."""
    return fake.building_number()

def unique_building_number(fake: object) -> str:
    """Generate a unique building number."""
    return unique(fake, building_number)

def city(fake: object) -> str:
    """Generate a city name."""
    return fake.city()

def unique_city(fake: object) -> str:
    """Generate a unique city name."""
    return unique(fake, city)

def city_suffix(fake: object) -> str:
    """Generate a city suffix."""
    return fake.city_suffix()

def country(fake: object) -> str:
    """Generate a country name."""
    return fake.country()

def unique_country(fake: object) -> str:
    """Generate a unique country name."""
    return unique(fake, country)

def country_code(
    fake: object,
    representation: CountryCodeType = CountryCodeType.ALPHA_2,
) -> str:
    """
    Generate a country code.

    Args:
        fake: The `Faker` instance.
        representation: "alpha-2" or "alpha-3". For example, United States has Alpha-2
          country code as 'US' and Alpha-3 as 'USA'.
    """
    return fake.country_code(representation=representation)

def unique_country_code(
    fake: object,
    representation: CountryCodeType = CountryCodeType.ALPHA_2,
) -> str:
    """
    Generate a unique country code.

    Args:
        fake: The `Faker` instance.
        representation: "alpha-2" or "alpha-3". For example, United States has Alpha-2
          country code as 'US' and Alpha-3 as 'USA'.
    """
    return unique(fake, country_code, representation=representation)

def current_country(fake: object) -> str:
    """Generate a current country name."""
    return fake.current_country()

def current_country_code(fake: object) -> str:
    """Generate a current country code."""
    return fake.current_country_code()

def postcode(fake: object) -> str:
    """Generate a postal code."""
    return fake.postcode()

def unique_postcode(fake: object) -> str:
    """Generate a unique postal code."""
    return unique(fake, postcode)

def street_address(fake: object) -> str:
    """Generate a street address."""
    return fake.street_address()

def unique_street_address(fake: object) -> str:
    """Generate a unique street address."""
    return unique(fake, street_address)

def street_name(fake: object) -> str:
    """Generate a street name."""
    return fake.street_name()

def unique_street_name(fake: object) -> str:
    """Generate a unique street name."""
    return unique(fake, street_name)

def street_suffix(fake: object) -> str:
    """Generate a street suffix."""
    return fake.street_suffix()
