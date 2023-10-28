import datetime
from typing import Optional
from ._utils import unique
from .types import DateTimeOptionalArg, DateTimeArg

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
    datetime_start: DateTimeOptionalArg = None,
    datetime_end: DateTimeOptionalArg = None,
    tzinfo: Optional[datetime.tzinfo] = None
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
    datetime_start: DateTimeOptionalArg = None,
    datetime_end: DateTimeOptionalArg = None,
    tzinfo: Optional[datetime.tzinfo] = None
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

def date_time_this_century(
    fake,
    before_now: bool = True,
    after_now: bool = False,
    tzinfo: Optional[datetime.tzinfo] = None
) -> datetime.datetime:
    """
    Gets a datetime object for the current century.

    Args:
        - before_now: include days in current century before today
        - after_now: include days in current century after today
        - tzinfo: timezone, instance of datetime.tzinfo subclass
    
    Returns:
        A datetime
    """
    return fake.date_time_this_century(before_now=before_now, after_now=after_now, tzinfo=tzinfo)

def unique_date_time_this_century(
    fake,
    before_now: bool = True,
    after_now: bool = False,
    tzinfo: Optional[datetime.tzinfo] = None
) -> datetime.datetime:
    """
    Gets a unique datetime object for the current century.

    Args:
        - before_now: include days in current century before today
        - after_now: include days in current century after today
        - tzinfo: timezone, instance of datetime.tzinfo subclass
    
    Returns:
        A datetime
    """
    return unique(fake, date_time_this_century, before_now=before_now, after_now=after_now, tzinfo=tzinfo)

def date_time_this_decade(
    fake,
    before_now: bool = True,
    after_now: bool = False,
    tzinfo: Optional[datetime.tzinfo] = None
) -> datetime.datetime:
    """
    Gets a datetime object for the decade year.

    Args:
        - before_now: include days in current decade before today
        - after_now: include days in current decade after today
        - tzinfo: timezone, instance of datetime.tzinfo subclass

    Returns:
        A datetime
    """
    return fake.date_time_this_decade(before_now=before_now, after_now=after_now, tzinfo=tzinfo)

def unique_date_time_this_decade(
    fake,
    before_now: bool = True,
    after_now: bool = False,
    tzinfo: Optional[datetime.tzinfo] = None
) -> datetime.datetime:
    """
    Gets a unique datetime object for the decade year.

    Args:
        - before_now: include days in current decade before today
        - after_now: include days in current decade after today
        - tzinfo: timezone, instance of datetime.tzinfo subclass

    Returns:
        A datetime
    """
    return unique(fake, date_time_this_decade, before_now=before_now, after_now=after_now, tzinfo=tzinfo)

def date_time_this_month(
    fake,
    before_now: bool = True,
    after_now: bool = False,
    tzinfo: Optional[datetime.tzinfo] = None
) -> datetime.datetime:
    """
    Gets a datetime object for the current month.

    Args:
        - before_now: include days in current month before today
        - after_now: include days in current month after today
        - tzinfo: timezone, instance of datetime.tzinfo subclass

    Returns:
        A datetime
    """
    return fake.date_time_this_month(before_now=before_now, after_now=after_now, tzinfo=tzinfo)

def unique_date_time_this_month(
    fake,
    before_now: bool = True,
    after_now: bool = False,
    tzinfo: Optional[datetime.tzinfo] = None
) -> datetime.datetime:
    """
    Gets a datetime object for the current month.

    Args:
        - before_now: include days in current month before today
        - after_now: include days in current month after today
        - tzinfo: timezone, instance of datetime.tzinfo subclass

    Returns:
        A datetime
    """
    return unique(fake, date_time_this_month, before_now=before_now, after_now=after_now, tzinfo=tzinfo)

def date_time_this_year(
    fake,
    before_now: bool = True,
    after_now: bool = False,
    tzinfo: Optional[datetime.tzinfo] = None
) -> datetime.datetime:
    """
    Gets a datetime object for the current year.

    Args:
        - before_now: include days in current year before today
        - after_now: include days in current year after today
        - tzinfo: timezone, instance of datetime.tzinfo subclass

    Returns:
        A datetime
    """
    return fake.date_time_this_year(before_now=before_now, after_now=after_now, tzinfo=tzinfo)

def unique_date_time_this_year(
    fake,
    before_now: bool = True,
    after_now: bool = False,
    tzinfo: Optional[datetime.tzinfo] = None
) -> datetime.datetime:
    """
    Gets a datetime object for the current year.

    Args:
        - before_now: include days in current year before today
        - after_now: include days in current year after today
        - tzinfo: timezone, instance of datetime.tzinfo subclass

    Returns:
        A datetime
    """
    return unique(fake, date_time_this_year, before_now=before_now, after_now=after_now, tzinfo=tzinfo)

def day_of_month(fake):
    """
    Generate a day of month.
    """
    return fake.day_of_month()

def unique_day_of_month(fake):
    """
    Generate a day of month.
    """
    return unique(fake, day_of_month)

def day_of_week(fake):
    """
    Generate a day of week.
    """
    return fake.day_of_week()

def unique_day_of_week(fake):
    """
    Generate a day of week.
    """
    return unique(fake, day_of_week)

def future_date(fake, end_date: DateTimeArg = '+30d', tzinfo: Optional[datetime.tzinfo] = None) -> datetime.date:
    """
    Get a Date object based on a random date between 1 day from now
    and a given date. Accepts date strings that can be
    recognized by strtotime().

    Args:
        - end_date: Defaults to “+30d”
        - tzinfo: timezone, instance of datetime.tzinfo subclass

    Returns:
        A date
    """
    return fake.future_date(end_date=end_date, tzinfo=tzinfo)

def unique_future_date(fake, end_date: DateTimeArg = '+30d', tzinfo: Optional[datetime.tzinfo] = None) -> datetime.date:
    """
    Get a Date object based on a random date between 1 day from now
    and a given date. Accepts date strings that can be
    recognized by strtotime().

    Args:
        - end_date: Defaults to “+30d”
        - tzinfo: timezone, instance of datetime.tzinfo subclass

    Returns:
        A date
    """
    return unique(fake, future_date, end_date=end_date, tzinfo=tzinfo)

def future_datetime(fake, end_date: DateTimeArg = '+30d', tzinfo: Optional[datetime.tzinfo] = None) -> datetime.datetime:
    """
    Get a datetime object based on a random date between 1 second form now
    and a given date. Accepts date strings that can be recognized
    by strtotime().

    Args:
        - end_date: Defaults to “+30d”
        - tzinfo: timezone, instance of datetime.tzinfo subclass

    Returns:
        A datetime
    """
    return fake.future_datetime(end_date=end_date, tzinfo=tzinfo)

def unique_future_datetime(fake, end_date: DateTimeArg = '+30d', tzinfo: Optional[datetime.tzinfo] = None) -> datetime.datetime:
    """
    Get a datetime object based on a random date between 1 second form now
    and a given date. Accepts date strings that can be recognized
    by strtotime().

    Args:
        - end_date: Defaults to “+30d”
        - tzinfo: timezone, instance of datetime.tzinfo subclass

    Returns:
        A datetime
    """
    return unique(fake, future_datetime, end_date=end_date, tzinfo=tzinfo)

def iso8601(
    fake,
    tzinfo: Optional[datetime.tzinfo] = None,
    end_datetime: DateTimeOptionalArg = None,
    sep: str = 'T',
    timespec: str = 'auto'
) -> str:
    """
    Get a timestamp in ISO 8601 format (or one of its profiles).

    Args:
        - tzinfo: timezone, instance of datetime.tzinfo subclass
        - sep: separator between date and time, defaults to ‘T’
        - timespec: format specifier for the time part,
          defaults to ‘auto’ - see datetime.isoformat() documentation
    
    Returns:
        A string with date into ISO 8601 format.
    """
    return fake.iso8601(tzinfo=tzinfo, end_datetime=end_datetime, sep=sep, timespec=timespec)

def unique_iso8601(
    fake,
    tzinfo: Optional[datetime.tzinfo] = None,
    end_datetime: DateTimeOptionalArg = None,
    sep: str = 'T',
    timespec: str = 'auto'
) -> str:
    """
    Get a timestamp in ISO 8601 format (or one of its profiles).

    Args:
        - tzinfo: timezone, instance of datetime.tzinfo subclass
        - sep: separator between date and time, defaults to ‘T’
        - timespec: format specifier for the time part,
          defaults to ‘auto’ - see datetime.isoformat() documentation
    
    Returns:
        A string with date into ISO 8601 format.
    """
    return unique(fake, iso8601, tzinfo=tzinfo, end_datetime=end_datetime, sep=sep, timespec=timespec)

def month(fake):
    return fake.month()

def unique_month(fake):
    return unique(fake, month)

def month_name(fake):
    return fake.month_name()

def unique_month_name(fake):
    return unique(fake, month_name)

def past_date(fake, start_date: DateTimeArg = '-30d', tzinfo: Optional[datetime.tzinfo] = None) -> datetime.date:
    """
    Get a Date object based on a random date between a given
    date and 1 day ago. Accepts date strings that
    can be recognized by strtotime().

    Args:
        - start_date: Defaults to “-30d”
        - tzinfo: timezone, instance of datetime.tzinfo subclass
    """
    return fake.past_date(start_date=start_date, tzinfo=tzinfo)

def unique_past_date(fake, start_date: DateTimeArg = '-30d', tzinfo: Optional[datetime.tzinfo] = None) -> datetime.date:
    """
    Get a Date object based on a random date between a given
    date and 1 day ago. Accepts date strings that
    can be recognized by strtotime().

    Args:
        - start_date: Defaults to “-30d”
        - tzinfo: timezone, instance of datetime.tzinfo subclass
    """
    return unique(fake, past_date, start_date=start_date, tzinfo=tzinfo)

def past_datetime(fake, start_date: DateTimeArg = '-30d', tzinfo: Optional[datetime.tzinfo] = None) -> datetime.datetime:
    """
    Get a datetime object based on a random date between a given
    date and 1 second ago. Accepts date strings
    that can be recognized by strtotime().

    Args:
        - start_date: Defaults to “-30d”
        - tzinfo: timezone, instance of datetime.tzinfo subclass
    """
    return fake.past_datetime(start_date=start_date, tzinfo=tzinfo)

def unique_past_datetime(fake, start_date: DateTimeArg = '-30d', tzinfo: Optional[datetime.tzinfo] = None) -> datetime.datetime:
    """
    Get a datetime object based on a random date between a given
    date and 1 second ago. Accepts date strings
    that can be recognized by strtotime().

    Args:
        - start_date: Defaults to “-30d”
        - tzinfo: timezone, instance of datetime.tzinfo subclass
    """
    return unique(fake, past_datetime, start_date=start_date, tzinfo=tzinfo)

def time(fake, pattern: str = '%H:%M:%S', end_datetime: DateTimeOptionalArg = None) -> str:
    """Get a time string (24h format by default)"""
    return fake.time(pattern=pattern, end_datetime=end_datetime)

def unique_time(fake, pattern: str = '%H:%M:%S', end_datetime: DateTimeOptionalArg = None) -> str:
    """Get a time string (24h format by default)"""
    return unique(fake, time, pattern=pattern, end_datetime=end_datetime)

def time_object(fake, end_datetime: DateTimeOptionalArg = None) -> datetime.time:
    """Get a time object"""
    return fake.time_object(end_datetime=end_datetime)

def unique_time_object(fake, end_datetime: DateTimeOptionalArg = None) -> datetime.time:
    """Get a time object"""
    return unique(fake, time_object, end_datetime=end_datetime)

def timezone(fake) -> str:
    return fake.timezone()

def unique_timezone(fake) -> str:
    return unique(fake, timezone)

def year(fake) -> str:
    return fake.year()

def unique_year(fake) -> str:
    return unique(fake, year)
