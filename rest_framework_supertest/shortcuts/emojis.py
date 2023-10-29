from ._utils import unique


def emoji(fake):
    """Generates a emoji"""
    return fake.emoji()

def unique_emoji(fake):
    """Generates a unique emoji"""
    return unique(fake, emoji)
