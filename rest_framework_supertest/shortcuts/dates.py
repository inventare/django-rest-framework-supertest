import datetime
from ._utils import unique
from ._types import DateTimeArg, TimezoneArg

def am_pm(fake):
    """Generate a AM or PM string."""
    return fake.am_pm()

def century(fake):
    """Generate a century"""
    return fake.century()

def unique_century(fake):
    """Generate a unique century"""
    return unique(fake, century)

def date(fake, pattern="%Y-%m-%d", end_datetime=None):
    """
    Get a date string between January 1, 1970 and now.
    
    Args:
        pattern: Format of the date (year-month-day by default)

    Returns:
        A date
    """
    return fake.date(pattern=pattern, end_datetime=end_datetime)

def unique_date(fake, pattern="%Y-%m-%d", end_datetime=None):
    """
    Get a unique date string between January 1, 1970 and now.
    
    Args:
        - pattern: Format of the date (year-month-day by default)

    Returns:
        A date
    """
    return unique(fake, date, pattern=pattern, end_datetime=end_datetime)

def date_between(fake, start_date='-30y', end_date='today'):
    """
    Get a Date object based on a random date between two given dates.
    Accepts date strings that can be recognized by strtotime().

    Args:
        - start_date: Defaults to 30 years ago
        - end_date: Defaults to “today".

    Returns:
        A date
    """
    return fake.date_between(start_date=start_date, end_date=end_date)

def unique_date_between(fake, start_date='-30y', end_date='today'):
    """
    Get a unique Date object based on a random date between two given dates.
    Accepts date strings that can be recognized by strtotime().

    Args:
        - start_date: Defaults to 30 years ago
        - end_date: Defaults to “today".

    Returns:
        A date
    """
    return unique(fake, date_between, start_date=start_date, end_date=end_date)

def date_between_dates(fake, date_start=None, date_end=None):
    """
    Takes two Date objects and returns a random date between the two given dates.
    Accepts Date or datetime objects

    Args:
        - date_start: Date
        - date_end: Date

    Returns:
        A date
    """
    return fake.date_between_dates(date_start=date_start, date_end=date_end)

def unique_date_between_dates(fake, date_start=None, date_end=None):
    """
    Takes two Date objects and returns a unique random date between the two given dates.
    Accepts Date or datetime objects

    Args:
        - date_start: Date
        - date_end: Date

    Returns:
        A date
    """
    return unique(fake, date_between_dates, date_start=date_start, date_end=date_end)

def date_object(fake, end_datetime = None):
    """Get a date object between January 1, 1970 and now"""
    return fake.date_object(end_datetime=end_datetime)

def unique_date_object(fake, end_datetime = None):
    """Get a unique date object between January 1, 1970 and now"""
    return unique(fake, date_object, end_datetime=end_datetime)

def date_of_birth(fake, tzinfo=None, minimum_age=0, maximum_age=115):
    """
    Generate a random date of birth represented as a Date object, constrained
    by optional miminimum_age and maximum_age parameters.

    Args:
        - tzinfo: Defaults to None
        - minimum_age: Defaults to 0
        - maximum_age: Defaults to 115

    Returns:
        A date
    """
    return fake.date_of_birth(tzinfo=tzinfo, minimum_age=minimum_age, maximum_age=maximum_age)

def unique_date_of_birth(fake, tzinfo=None, minimum_age=0, maximum_age=115):
    """
    Generate a unique random date of birth represented as a Date object, constrained
    by optional miminimum_age and maximum_age parameters.

    Args:
        - tzinfo: Defaults to None
        - minimum_age: Defaults to 0
        - maximum_age: Defaults to 115

    Returns:
        A date
    """
    return unique(fake, date_of_birth, tzinfo=tzinfo, minimum_age=minimum_age, maximum_age=maximum_age)

def date_this_century(fake, before_today=True, after_today=False):
    """
    Gets a Date object for the current century.

    Args:
        - before_today: include days in current century before today
        - after_today: include days in current century after today

    Returns:
        A date
    """
    return fake.date_this_century(before_today=before_today, after_today=after_today)

def unique_date_this_century(fake, before_today=True, after_today=False):
    """
    Gets a unique Date object for the current century.

    Args:
        - before_today: include days in current century before today
        - after_today: include days in current century after today

    Returns:
        A date
    """
    return unique(fake, date_this_century, before_today=before_today, after_today=after_today)

def date_this_decade(fake, before_today=True, after_today=False):
    """
    Gets a Date object for the decade year.

    Args:
        - before_today: include days in current decade before today
        - after_today: include days in current decade after today
    
    Returns:
        A date
    """
    return fake.date_this_decade(before_today=before_today, after_today=after_today)

def unique_date_this_decade(fake, before_today=True, after_today=False):
    """
    Gets a unique Date object for the decade year.

    Args:
        - before_today: include days in current decade before today
        - after_today: include days in current decade after today
    
    Returns:
        A date
    """
    return unique(fake, date_this_decade, before_today=before_today, after_today=after_today)

def date_this_month(fake, before_today=True, after_today=False):
    """
    Gets a Date object for the current month.

    Args:
        - before_today: include days in current month before today
        - after_today: include days in current month after today
    
    Returns:
        A date
    """
    return fake.date_this_month(before_today=before_today, after_today=after_today)

def unique_date_this_month(fake, before_today=True, after_today=False):
    """
    Gets a Date object for the current month.

    Args:
        - before_today: include days in current month before today
        - after_today: include days in current month after today
    
    Returns:
        A date
    """
    return unique(fake, date_this_month, before_today=before_today, after_today=after_today)

def date_this_year(fake, before_today=True, after_today=False):
    """
    Gets a Date object for the current year.

    Args:
        - before_today: include days in current year before today
        - after_today: include days in current year after today
    
    Returns:
        A date
    """
    return fake.date_this_year(before_today=before_today, after_today=after_today)

def unique_date_this_year(fake, before_today=True, after_today=False):
    """
    Gets a Date object for the current year.

    Args:
        - before_today: include days in current year before today
        - after_today: include days in current year after today
    
    Returns:
        A date
    """
    return unique(fake, date_this_year, before_today=before_today, after_today=after_today)

def date_time(fake, tzinfo=None, end_datetime=None):
    """
    Get a datetime object for a date between January 1, 1970 and now

    Args:
        - tzinfo: timezone, instance of datetime.tzinfo subclass

    Returns:
        A datetime
    """
    return fake.date_time(tzinfo=tzinfo, end_datetime=end_datetime)

def unique_date_time(fake, tzinfo=None, end_datetime=None):
    """
    Get a datetime object for a date between January 1, 1970 and now

    Args:
        - tzinfo: timezone, instance of datetime.tzinfo subclass

    Returns:
        A datetime
    """
    return unique(fake, date_time, tzinfo=tzinfo, end_datetime=end_datetime)

def date_time_ad(fake, tzinfo=None, end_datetime=None, start_datetime=None):
    """
    Get a datetime object for a date between January 1, 001 and now

    Args:
        - tzinfo: timezone, instance of datetime.tzinfo subclass

    Returns:
        A datetime
    """
    return fake.date_time_ad(tzinfo=tzinfo, end_datetime=end_datetime, start_datetime=start_datetime)

def unique_date_time_ad(fake, tzinfo=None, end_datetime=None, start_datetime=None):
    """
    Get a datetime object for a date between January 1, 001 and now

    Args:
        - tzinfo: timezone, instance of datetime.tzinfo subclass

    Returns:
        A datetime
    """
    return unique(fake, date_time_ad, tzinfo=tzinfo, end_datetime=end_datetime, start_datetime=start_datetime)

def date_time_between(fake, start_date='-30y', end_date='now', tzinfo=None):
    """
    Get a datetime object based on a random date between two
    given dates. Accepts date strings that can be recognized by strtotime().

    Args:
        - start_date: Defaults to 30 years ago
        - end_date: Defaults to “now”
        - tzinfo: timezone, instance of datetime.tzinfo subclass

    Returns:
        A datetime
    """
    return fake.date_time_between(start_date=start_date, end_date=end_date, tzinfo=tzinfo)

def unique_date_time_between(fake, start_date='-30y', end_date='now', tzinfo=None):
    """
    Get a unique datetime object based on a random date between two
    given dates. Accepts date strings that can be recognized by strtotime().

    Args:
        - start_date: Defaults to 30 years ago
        - end_date: Defaults to “now”
        - tzinfo: timezone, instance of datetime.tzinfo subclass

    Returns:
        A datetime
    """
    return unique(fake, date_time_between, start_date=start_date, end_date=end_date, tzinfo=tzinfo)

def date_time_between_dates(
    fake,
    datetime_start: DateTimeArg = None,
    datetime_end: DateTimeArg = None,
    tzinfo: TimezoneArg = None
) -> datetime.datetime:
    """
    Takes two datetime objects and returns a random datetime
    between the two given datetimes. Accepts datetime objects.

    Args:
        - datetime_start: datetime
        - datetime_end: datetime
        - tzinfo: timezone, instance of datetime.tzinfo subclass
    
    Returns:
        A datetime
    """
    return fake.date_time_between_dates(
        datetime_start=datetime_start,
        datetime_end=datetime_end,
        tzinfo=tzinfo
    )

def unique_date_time_between_dates(
    fake,
    datetime_start: DateTimeArg = None,
    datetime_end: DateTimeArg = None,
    tzinfo: TimezoneArg = None
) -> datetime.datetime:
    """
    Takes two datetime objects and returns a unique random datetime
    between the two given datetimes. Accepts datetime objects.

    Args:
        - datetime_start: datetime
        - datetime_end: datetime
        - tzinfo: timezone, instance of datetime.tzinfo subclass
    
    Returns:
        A datetime
    """
    return unique(
        fake,
        date_time_between_dates,
        datetime_start=datetime_start,
        datetime_end=datetime_end,
        tzinfo=tzinfo
    )
