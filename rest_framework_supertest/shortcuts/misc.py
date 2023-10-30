from typing import Union
from uuid import UUID


def boolean(fake: object, chance_of_getting_true: int = 50) -> bool:
    """Generate a random boolean value based on chance_of_getting_true."""
    return fake.boolean(chance_of_getting_true=chance_of_getting_true)

def null_boolean(fake: object) -> Union[None, bool]:
    """Generate None, True, or False, each with equal probability."""
    return fake.null_boolean()

def password(
    fake: object,
    *,
    length: int = 10,
    special_chars: bool = True,
    digits: bool = True,
    upper_case: bool = True,
    lower_case: bool = True,
) -> str:
    """
    Generate a random password of the specified length.

    Args:
        fake: The `Faker` instance.
        length: The length of the password.
        special_chars: indicate if at least one special char is present
          on the password. Special characters are characters from !@#$%^&*()_+
        digits: indicate if at least one digit is present on the password.
          The digits are characters from 0123456789.
        upper_case: indicate if at least one upper case letter is present.
        lower_case: indicate if at least one lower case letter is present.
    """
    return fake.password(
        length=length,
        special_chars=special_chars,
        digits=digits,
        upper_case=upper_case,
        lower_case=lower_case,
    )

def uuid4(fake: object, cast_to: type = str) -> Union[str, UUID]:
    """
    Generate a random UUID4 object and cast it to another type.

    Args:
        fake: The `Faker` instance.
        cast_to: the type to cast the UUID to. By default, cast_to is set to str.
          May be called with cast_to=None to return a full-fledged UUID.
    """
    return fake.uuid4(cast_to=cast_to)
