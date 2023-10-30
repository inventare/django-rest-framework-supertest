from ._utils import unique


def emoji(fake: object) -> str:
    """Generate a emoji."""
    return fake.emoji()

def unique_emoji(fake: object) -> str:
    """Generate a unique emoji."""
    return unique(fake, emoji)
