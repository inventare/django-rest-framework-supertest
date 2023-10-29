from ._utils import unique


def coordinate(fake, center=None, radius=0.001):
    """
    Generate a coordinate with a optionally center
    and pick a point within radius.
    """
    return fake.coordinate(center=center, radius=radius)

def unique_coordinate(fake, center=None, radius=0.001):
    """
    Generate a unique coordinate with a optionally center
    and pick a point within radius.
    """
    return unique(fake, coordinate, center=center, radius=radius)

def latitude(fake):
    """Generate a latitude."""
    return fake.latitude()

def unique_latitude(fake):
    """Generate a unique latitude."""
    return unique(fake, latitude)

def longitude(fake):
    """Generate a longitude."""
    return fake.longitude()

def unique_longitude(fake):
    """Generate a unique longitude."""
    return unique(fake, longitude)
