def unique(fake, fn, **kwargs):
    """Helper to wrap Faker.unique method inside the function."""
    return fn(fake.unique, **kwargs)
