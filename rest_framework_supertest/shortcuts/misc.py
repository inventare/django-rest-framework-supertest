

def boolean(fake, chance_of_getting_true=50):
    """Generate a random boolean value based on chance_of_getting_true"""
    return fake.boolean(chance_of_getting_true=chance_of_getting_true)

def null_boolean(fake):
    """Generate None, True, or False, each with equal probability."""
    return fake.null_boolean()

def password(fake, length=10, special_chars=True, digits=True, upper_case=True, lower_case=True):
    """
    Generate a random password of the specified length.

    The arguments special_chars, digits, upper_case, and lower_case
    control what category of characters will appear in the generated
    password. If set to True (default), at least one character
    from the corresponding category is guaranteed to appear.
    Special characters are characters from !@#$%^&*()_+,
    digits are characters from 0123456789, and uppercase and lowercase
    characters are characters from the ASCII set of letters.
    """
    return fake.password(length=length, special_chars=special_chars, digits=digits, upper_case=upper_case, lower_case=lower_case)

def uuid4(fake, cast_to=str):
    """
    Generate a random UUID4 object and cast it to another
    type if specified using a callable cast_to.

    By default, cast_to is set to str. May be called
    with cast_to=None to return a full-fledged UUID.
    """
    return fake.uuid4(cast_to=cast_to)
