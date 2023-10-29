from ._utils import unique


def first_name(fake):
    """Generates a first name"""
    return fake.first_name()

def unique_first_name(fake):
    """Generates a unique first name"""
    return unique(fake, first_name)

def first_name_female(fake):
    """Generates a first female name"""
    return fake.first_name_female()

def unique_first_name_female(fake):
    """Generates a unique female first name"""
    return unique(fake, first_name_female)

def first_name_male(fake):
    """Generates a first male name"""
    return fake.first_name_male()

def unique_first_name_male(fake):
    """Generates a unique male first name"""
    return unique(fake, first_name_male)

def first_name_nonbinary(fake):
    """Generates a non-binary first name"""
    return fake.first_name_nonbinary()

def unique_first_name_nonbinary(fake):
    """Generates a unique non-binary first name"""
    return unique(fake, first_name_nonbinary)

def language_name(fake):
    """Generates a random i18n language name (e.g. English)."""
    return fake.language_name()

def last_name(fake):
    """Generates a last name"""
    return fake.last_name()

def unique_last_name(fake):
    """Generates a unique last name"""
    return unique(fake, last_name)

def last_name_female(fake):
    """Generates a female last name"""
    return fake.last_name_female()

def unique_last_name_female(fake):
    """Generates a unique female last name"""
    return unique(fake, last_name_female)

def last_name_male(fake):
    """Generates a male last name"""
    return fake.last_name_male()

def unique_last_name_male(fake):
    """Generates a unique male last name"""
    return unique(fake, last_name_male)

def last_name_nonbinary(fake):
    """Generates a non-binary last name"""
    return fake.last_name_nonbinary()

def unique_last_name_nonbinary(fake):
    """Generates a unique non-binary last name"""
    return unique(fake, last_name_nonbinary)

def name(fake):
    """Generates a name"""
    return fake.name()

def unique_name(fake):
    """Generates a unique name"""
    return unique(fake, name)

def name_female(fake):
    """Generates a female name"""
    return fake.name_female()

def unique_name_female(fake):
    """Generates a unique female name"""
    return unique(fake, name_female)

def name_male(fake):
    """Generates a male name"""
    return fake.name_male()

def unique_name_male(fake):
    """Generates a unique male name"""
    return unique(fake, name_male)

def name_nonbinary(fake):
    """Generates a non-binary name"""
    return fake.name_nonbinary()

def unique_name_nonbinary(fake):
    """Generates a unique non-binary name"""
    return unique(fake, name_nonbinary)

def prefix(fake):
    """Generates a prefix"""
    return fake.prefix()

def prefix_female(fake):
    """Generates a female prefix"""
    return fake.prefix_female()

def prefix_male(fake):
    """Generates a male prefix"""
    return fake.prefix_male()

def prefix_nonbinary(fake):
    """Generates a non-binary prefix"""
    return fake.prefix_nonbinary()

def suffix(fake):
    """Generates a suffix"""
    return fake.suffix()

def suffix_female(fake):
    """Generates a female suffix"""
    return fake.suffix_female()

def suffix_male(fake):
    """Generates a male suffix"""
    return fake.suffix_male()

def suffix_nonbinary(fake):
    """Generates a non-binary suffix"""
    return fake.suffix_nonbinary()
