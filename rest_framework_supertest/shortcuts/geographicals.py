import decimal
from typing import Optional, Union

from ._utils import unique


def coordinate(
    fake: object,
    center: Optional[float] = None,
    radius: Union[float, int] = 0.001,
) -> decimal.Decimal:
    """
    Generate a corrdinate.

    Args:
        fake: The `Faker` instance.
        center: define a center of coordinate. If the center=None, then
          an random coordinate is generated.
        radius: if the center is not None, this is used to radius to
          define an random coordinate between center - radius and
          center + radius.
    """
    return fake.coordinate(center=center, radius=radius)

def unique_coordinate(
    fake: object,
    center: Optional[float] = None,
    radius: Union[float, int] = 0.001,
) -> decimal.Decimal:
    """
    Generate a unique corrdinate.

    Args:
        fake: The `Faker` instance.
        center: define a center of coordinate. If the center=None, then
          an random coordinate is generated.
        radius: if the center is not None, this is used to radius to
          define an random coordinate between center - radius and
          center + radius.
    """
    return unique(fake, coordinate, center=center, radius=radius)

def latitude(fake: object) -> decimal.Decimal:
    """Generate a latitude."""
    return fake.latitude()

def unique_latitude(fake: object) -> decimal.Decimal:
    """Generate a unique latitude."""
    return unique(fake, latitude)

def longitude(fake: object) -> decimal.Decimal:
    """Generate a longitude."""
    return fake.longitude()

def unique_longitude(fake: object) -> decimal.Decimal:
    """Generate a unique longitude."""
    return unique(fake, longitude)
