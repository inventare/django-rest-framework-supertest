from ._utils import unique


def license_plate(fake: object) -> str:
    """Generate a license plate."""
    return fake.license_plate()

def unique_license_plate(fake: object) -> str:
    """Generate a unique license plate."""
    return unique(fake, license_plate)

def vin(fake: object) -> str:
    """Generate a vin number."""
    return fake.vin()

def unique_vin(fake: object) -> str:
    """Generate a unique vin number."""
    return unique(fake, vin)
