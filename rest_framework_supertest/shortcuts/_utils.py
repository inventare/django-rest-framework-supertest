from typing import Callable


def unique(fake: object, fn: Callable, **kwargs: dict) -> object:
    """Wrap the Faker.unique method inside the function."""
    return fn(fake.unique, **kwargs)
