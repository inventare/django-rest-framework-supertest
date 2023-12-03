from datetime import date, datetime, timedelta
from enum import Enum
from typing import Sequence, TypeVar, Union

DateParseType = Union[date, datetime, timedelta, str, int]

HueType = TypeVar("HueType", str, float, Sequence[int])

class CountryCodeType(Enum):
    """
    Indicate country code type.

    For example, United States has Alpha-2 country code as
    'US' and Alpha-3 as 'USA'.
    """

    ALPHA_2 = "alpha-2"
    ALPHA_3 = "alpha-3"
