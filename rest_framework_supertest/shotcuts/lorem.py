from ._utils import unique

def word(fake):
    """Generates a word"""
    return fake.word()

def unique_word(fake):
    """Generates a unique word"""
    return unique(fake, word)
