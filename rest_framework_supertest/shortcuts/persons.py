from ._utils import unique


def first_name(fake: object) -> str:
    """Generate a first name."""
    return fake.first_name()

def unique_first_name(fake: object) -> str:
    """Generate a unique first name."""
    return unique(fake, first_name)

def first_name_female(fake: object) -> str:
    """Generate a first female name."""
    return fake.first_name_female()

def unique_first_name_female(fake: object) -> str:
    """Generate a unique female first name."""
    return unique(fake, first_name_female)

def first_name_male(fake: object) -> str:
    """Generate a first male name."""
    return fake.first_name_male()

def unique_first_name_male(fake: object) -> str:
    """Generate a unique male first name."""
    return unique(fake, first_name_male)

def first_name_nonbinary(fake: object) -> str:
    """Generate a non-binary first name."""
    return fake.first_name_nonbinary()

def unique_first_name_nonbinary(fake: object) -> str:
    """Generate a unique non-binary first name."""
    return unique(fake, first_name_nonbinary)

def language_name(fake: object) -> str:
    """Generate a random i18n language name (e.g. English)."""
    return fake.language_name()

def last_name(fake: object) -> str:
    """Generate a last name."""
    return fake.last_name()

def unique_last_name(fake: object) -> str:
    """Generate a unique last name."""
    return unique(fake, last_name)

def last_name_female(fake: object) -> str:
    """Generate a female last name."""
    return fake.last_name_female()

def unique_last_name_female(fake: object) -> str:
    """Generate a unique female last name."""
    return unique(fake, last_name_female)

def last_name_male(fake: object) -> str:
    """Generate a male last name."""
    return fake.last_name_male()

def unique_last_name_male(fake: object) -> str:
    """Generate a unique male last name."""
    return unique(fake, last_name_male)

def last_name_nonbinary(fake: object) -> str:
    """Generate a non-binary last name."""
    return fake.last_name_nonbinary()

def unique_last_name_nonbinary(fake: object) -> str:
    """Generate a unique non-binary last name."""
    return unique(fake, last_name_nonbinary)

def name(fake: object) -> str:
    """Generate a name."""
    return fake.name()

def unique_name(fake: object) -> str:
    """Generate a unique name."""
    return unique(fake, name)

def name_female(fake: object) -> str:
    """Generate a female name."""
    return fake.name_female()

def unique_name_female(fake: object) -> str:
    """Generate a unique female name."""
    return unique(fake, name_female)

def name_male(fake: object) -> str:
    """Generate a male name."""
    return fake.name_male()

def unique_name_male(fake: object) -> str:
    """Generate a unique male name."""
    return unique(fake, name_male)

def name_nonbinary(fake: object) -> str:
    """Generate a non-binary name."""
    return fake.name_nonbinary()

def unique_name_nonbinary(fake: object) -> str:
    """Generate a unique non-binary name."""
    return unique(fake, name_nonbinary)

def prefix(fake: object) -> str:
    """Generate a prefix."""
    return fake.prefix()

def prefix_female(fake: object) -> str:
    """Generate a female prefix."""
    return fake.prefix_female()

def prefix_male(fake: object) -> str:
    """Generate a male prefix."""
    return fake.prefix_male()

def prefix_nonbinary(fake: object) -> str:
    """Generate a non-binary prefix."""
    return fake.prefix_nonbinary()

def suffix(fake: object) -> str:
    """Generate a suffix."""
    return fake.suffix()

def suffix_female(fake: object) -> str:
    """Generate a female suffix."""
    return fake.suffix_female()

def suffix_male(fake: object) -> str:
    """Generate a male suffix."""
    return fake.suffix_male()

def suffix_nonbinary(fake: object) -> str:
    """Generate a non-binary suffix."""
    return fake.suffix_nonbinary()
