from typing import Optional

from ._utils import unique
from .typing import HueType


def color(
    fake: object,
    hue: Optional[HueType] = None,
    luminosity: Optional[str] = None,
    color_format: str = "hex",
) -> str:
    """
    Generate a color in a human-friendly way.

    Under the hood, this method first creates a color
    represented in the HSV color model and then converts
    it to the desired color_format.

    Args:
        fake: The `Faker` instance.
        hue: controls the H value according to the following rules:
          - If the value is a number from 0 to 360, it will serve
            as the H value of the generated color.
          - If the value is a tuple/list of 2 numbers from 0 to 360,
            the color's H value will be randomly selected from that range.
          - If the value is a valid string, the color's H value will
            be randomly selected from the H range corresponding to the
            supplied string. Valid values are 'monochrome', 'red',
            'orange', 'yellow', 'green', 'blue', 'purple', and 'pink'.
        luminosity: influences both S and V values and is
          partially affected by hue as well. The finer details of this
          relationship are somewhat involved, so please refer to the
          source code instead if you wish to dig deeper. To keep the
          interface simple, this argument either can be omitted or can
          accept the following string values:'bright', 'dark', 'light', or 'random'.
        color_format: controls in which color model the color is
          represented. Valid values are 'hsv', 'hsl', 'rgb', or 'hex' (default).
    """
    return fake.color(hue=hue, luminosity=luminosity, color_format=color_format)

def unique_color(
    fake: object,
    hue: Optional[HueType] = None,
    luminosity: Optional[str] = None,
    color_format: str = "hex",
) -> str:
    """
    Generate a unique color in a human-friendly way.

    Under the hood, this method first creates a color
    represented in the HSV color model and then converts
    it to the desired color_format.

    Args:
        fake: The `Faker` instance.
        hue: controls the H value according to the following rules:
          - If the value is a number from 0 to 360, it will serve
            as the H value of the generated color.
          - If the value is a tuple/list of 2 numbers from 0 to 360,
            the color's H value will be randomly selected from that range.
          - If the value is a valid string, the color's H value will
            be randomly selected from the H range corresponding to the
            supplied string. Valid values are 'monochrome', 'red',
            'orange', 'yellow', 'green', 'blue', 'purple', and 'pink'.
        luminosity: influences both S and V values and is
          partially affected by hue as well. The finer details of this
          relationship are somewhat involved, so please refer to the
          source code instead if you wish to dig deeper. To keep the
          interface simple, this argument either can be omitted or can
          accept the following string values:'bright', 'dark', 'light', or 'random'.
        color_format: controls in which color model the color is
          represented. Valid values are 'hsv', 'hsl', 'rgb', or 'hex' (default).
    """
    return unique(
        fake,
        color,
        hue=hue,
        luminosity=luminosity,
        color_format=color_format,
    )

def color_name(fake: object) -> str:
    """Generate a color name."""
    return fake.color_name()

def unique_color_name(fake: object) -> str:
    """Generate a unique color name."""
    return unique(fake, color_name)

def hex_color(fake: object) -> str:
    """Generate a color formatted as a hex triplet."""
    return fake.hex_color()

def unique_hex_color(fake: object) -> str:
    """Generate a unique color formatted as a hex triplet."""
    return unique(fake, hex_color)

def rgb_color(fake: object) -> str:
    """Generate a color formatted as a comma-separated RGB value."""
    return fake.rgb_color()

def unique_rgb_color(fake: object) -> str:
    """Generate a unique color formatted as a comma-separated RGB value."""
    return unique(fake, rgb_color)

def rgb_css_color(fake: object) -> str:
    """Generate a color formatted as a CSS rgb() function."""
    return fake.rgb_css_color()

def unique_rgb_css_color(fake: object) -> str:
    """Generate a unique color formatted as a CSS rgb() function."""
    return unique(fake, rgb_css_color)

def safe_color_name(fake: object) -> str:
    """Generate a web-safe color name."""
    return fake.safe_color_name()

def unique_safe_color_name(fake: object) -> str:
    """Generate a unique web-safe color name."""
    return unique(fake, safe_color_name)

def safe_hex_color(fake: object) -> str:
    """Generate a web-safe color formatted as a hex triplet."""
    return fake.safe_hex_color()

def unique_safe_hex_color(fake: object) -> str:
    """Generate a web-safe color formatted as a hex triplet."""
    return unique(fake, safe_hex_color)
