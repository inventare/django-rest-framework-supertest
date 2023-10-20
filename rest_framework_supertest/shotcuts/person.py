from ._utils import unique

def name(fake):
    """Generates a name"""
    return fake.name

def unique_name(fake):
    """Generates a unique name"""
    return unique(fake, name)
