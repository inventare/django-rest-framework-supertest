from ._utils import unique

def address(fake):
    """Generate a address."""
    return fake.address()

def unique_address(fake):
    """Generate a unique address."""
    return unique(fake, address)

def building_number(fake):
    """Generate a building number."""
    return fake.building_number()

def unique_building_number(fake):
    """Generate a unique building number."""
    return unique(fake, building_number)

def city(fake):
    """Generate a city name."""
    return fake.city()

def unique_city(fake):
    """Generate a unique city name."""
    return unique(fake, city)

def city_suffix(fake):
    """Generate a city suffix."""
    return fake.city_suffix()

def country(fake):
    """Generate a country name."""
    return fake.country()

def unique_country(fake):
    """Generate a unique country name."""
    return unique(fake, country)

def country_code(fake, representation='alpha-2'):
    """Generate a country code"""
    return fake.country_code(representation=representation)

def unique_country_code(fake, representation='alpha-2'):
    """Generate a unique country code"""
    return unique(fake, country_code, representation=representation)

def current_country(fake):
    """Generate a current country name."""
    return fake.current_country()

def current_country_code(fake):
    """Generate a current country code."""
    return fake.current_country_code()

def postcode(fake):
    """Generate a postal code"""
    return fake.postcode()

def unique_postcode(fake):
    """Generate a unique postal code"""
    return unique(fake, postcode)

def street_address(fake):
    """Generate a street address"""
    return fake.street_address()

def unique_street_address(fake):
    """Generate a unique street address"""
    return unique(fake, street_address)

def street_name(fake):
    """Generate a street name"""
    return fake.street_name()

def unique_street_name(fake):
    """Generate a unique street name"""
    return unique(fake, street_name)

def street_suffix(fake):
    """Generate a street suffix"""
    return fake.street_suffix()
