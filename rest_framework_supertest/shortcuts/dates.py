import datetime
from typing import Optional

from ._utils import unique
from .typing import DateParseType


def am_pm(fake: object) -> str:
    """Generate a AM or PM string."""
    return fake.am_pm()

def century(fake: object) -> str:
    """Generate a century."""
    return fake.century()

def unique_century(fake: object) -> str:
    """Generate a unique century."""
    return unique(fake, century)

def date(
    fake: object,
    pattern: str = "%Y-%m-%d",
    end_datetime: Optional[DateParseType] = None,
) -> str:
    """
    Generate a date string between January 1, 1970 and now.

    Args:
        fake: The `Faker` instance.
        pattern: format of the date (year-month-day by default)
        end_datetime: if is set, this is the max date possible.
    """
    return fake.date(pattern=pattern, end_datetime=end_datetime)

def unique_date(
    fake: object,
    pattern: str = "%Y-%m-%d",
    end_datetime: Optional[DateParseType] = None,
) -> str:
    """
    Generate a unique date string between January 1, 1970 and now.

    Args:
        fake: The `Faker` instance.
        pattern: format of the date (year-month-day by default)
        end_datetime: if is set, this is the max date possible.
    """
    return unique(fake, date, pattern=pattern, end_datetime=end_datetime)

def date_between(
    fake: object,
    start_date: DateParseType = '-30y',
    end_date: DateParseType = 'today',
) -> datetime.date:
    """
    Generate a date object based on a random date between two given dates.

    Args:
        fake: The `Faker` instance.
        start_date: first date of the date range to generate. Accepts
          date strings that can be recognized by strtotime().
        end_date: last date of the date range to generate. Accepts
          date strings that can be recognized by strtotime().
    """
    return fake.date_between(start_date=start_date, end_date=end_date)

def unique_date_between(
    fake: object,
    start_date: DateParseType = '-30y',
    end_date: DateParseType = 'today',
) -> datetime.date:
    """
    Generate a unique date object based on a random date between two given dates.

    Args:
        fake: The `Faker` instance.
        start_date: first date of the date range to generate. Accepts
          date strings that can be recognized by strtotime().
        end_date: last date of the date range to generate. Accepts
          date strings that can be recognized by strtotime().
    """
    return unique(fake, date_between, start_date=start_date, end_date=end_date)

def date_between_dates(
    fake: object,
    date_start: Optional[DateParseType] = None,
    date_end: Optional[DateParseType] = None,
) -> datetime.date:
    """
    Generate a date between two dates.

    Args:
        fake: The `Faker` instance.
        date_start: first date of the date range to generate.
        date_end: second date of the date range to generate.
    """
    return fake.date_between_dates(date_start=date_start, date_end=date_end)

def unique_date_between_dates(
    fake: object,
    date_start: Optional[DateParseType] = None,
    date_end: Optional[DateParseType] = None,
) -> datetime.date:
    """
    Generate a unique date between two dates.

    Args:
        fake: The `Faker` instance.
        date_start: first date of the date range to generate.
        date_end: second date of the date range to generate.
    """
    return unique(fake, date_between_dates, date_start=date_start, date_end=date_end)

def date_object(
    fake: object,
    end_datetime: Optional[DateParseType] = None,
) -> datetime.date:
    """
    Generate a date object between January 1, 1970 and now.

    Args:
        fake: The `Faker` instance.
        end_datetime: if is set, this is the max date possible.
    """
    return fake.date_object(end_datetime=end_datetime)

def unique_date_object(
    fake: object,
    end_datetime: Optional[DateParseType] = None,
) -> datetime.date:
    """
    Generate a unique date object between January 1, 1970 and now.

    Args:
        fake: The `Faker` instance.
        end_datetime: if is set, this is the max date possible.
    """
    return unique(fake, date_object, end_datetime=end_datetime)

def date_of_birth(
    fake: object,
    tzinfo: Optional[datetime.tzinfo] = None,
    minimum_age: int = 0,
    maximum_age: int = 115,
) -> datetime.date:
    """
    Generate a random date of birth constrained by minimum_age and maximum_age.

    Args:
        fake: The `Faker` instance.
        tzinfo: timezone, instance of datetime.tzinfo subclass.
        minimum_age: the minimum age of the person with this birth date.
        maximum_age: the maximum age of the person with this birth date.
    """
    return fake.date_of_birth(
        tzinfo=tzinfo,
        minimum_age=minimum_age,
        maximum_age=maximum_age,
    )

def unique_date_of_birth(
    fake: object,
    tzinfo: Optional[datetime.tzinfo] = None,
    minimum_age: int = 0,
    maximum_age: int = 115,
) -> datetime.date:
    """
    Generate a unique date of birth constrained by minimum_age and maximum_age.

    Args:
        fake: The `Faker` instance.
        tzinfo: timezone, instance of datetime.tzinfo subclass.
        minimum_age: the minimum age of the person with this birth date.
        maximum_age: the maximum age of the person with this birth date.
    """
    return unique(
        fake,
        date_of_birth,
        tzinfo=tzinfo,
        minimum_age=minimum_age,
        maximum_age=maximum_age,
    )

def date_this_century(
    fake: object,
    *,
    before_today: bool = True,
    after_today: bool = False,
) -> datetime.date:
    """
    Generate a date in the current century.

    Args:
        fake: The `Faker` instance.
        before_today: include days in current century before today.
        after_today: include days in current century after today.
    """
    return fake.date_this_century(before_today=before_today, after_today=after_today)

def unique_date_this_century(
    fake: object,
    *,
    before_today: bool = True,
    after_today: bool = False,
) -> datetime.date:
    """
    Generate a unique date in the current century.

    Args:
        fake: The `Faker` instance.
        before_today: include days in current century before today.
        after_today: include days in current century after today.
    """
    return unique(
        fake,
        date_this_century,
        before_today=before_today,
        after_today=after_today,
    )

def date_this_decade(
    fake: object,
    *,
    before_today: bool = True,
    after_today: bool = False,
) -> datetime.date:
    """
    Generate a date in the current decade.

    Args:
        fake: The `Faker` instance.
        before_today: include days in current decade before today.
        after_today: include days in current decade after today.
    """
    return fake.date_this_decade(before_today=before_today, after_today=after_today)

def unique_date_this_decade(
    fake: object,
    *,
    before_today: bool = True,
    after_today: bool = False,
) -> datetime.date:
    """
    Generate a unique date in the current decade.

    Args:
        fake: The `Faker` instance.
        before_today: include days in current decade before today.
        after_today: include days in current decade after today.
    """
    return unique(
        fake,
        date_this_decade,
        before_today=before_today,
        after_today=after_today,
    )

def date_this_month(
    fake: object,
    *,
    before_today: bool = True,
    after_today: bool = False,
) -> datetime.date:
    """
    Generate a date in the current month.

    Args:
        fake: The `Faker` instance.
        before_today: include days in current month before today.
        after_today: include days in current month after today.
    """
    return fake.date_this_month(before_today=before_today, after_today=after_today)

def unique_date_this_month(
    fake: object,
    *,
    before_today: bool = True,
    after_today: bool = False,
) -> datetime.date:
    """
    Generate a unique date in the current month.

    Args:
        fake: The `Faker` instance.
        before_today: include days in current month before today.
        after_today: include days in current month after today.
    """
    return unique(
        fake,
        date_this_month,
        before_today=before_today,
        after_today=after_today,
    )

def date_this_year(
    fake: object,
    *,
    before_today: bool = True,
    after_today: bool = False,
) -> datetime.date:
    """
    Generate a unique date in the current year.

    Args:
        fake: The `Faker` instance.
        before_today: include days in current year before today.
        after_today: include days in current year after today.
    """
    return fake.date_this_year(before_today=before_today, after_today=after_today)

def unique_date_this_year(
    fake: object,
    *,
    before_today: bool = True,
    after_today: bool = False,
) -> datetime.date:
    """
    Generate a unique date in the current year.

    Args:
        fake: The `Faker` instance.
        before_today: include days in current year before today.
        after_today: include days in current year after today.
    """
    return unique(
        fake,
        date_this_year,
        before_today=before_today,
        after_today=after_today,
    )

def date_time(
    fake: object,
    tzinfo: Optional[datetime.tzinfo] = None,
    end_datetime: Optional[DateParseType] = None,
) -> datetime.datetime:
    """
    Generate a datetime object for a date between January 1, 1970 and now.

    Args:
        fake: The `Faker` instance.
        tzinfo: timezone, instance of datetime.tzinfo subclass.
        end_datetime: if is set, this is the max date possible.
    """
    return fake.date_time(tzinfo=tzinfo, end_datetime=end_datetime)

def unique_date_time(
    fake: object,
    tzinfo: Optional[datetime.tzinfo] = None,
    end_datetime: Optional[DateParseType] = None,
) -> datetime.datetime:
    """
    Generate a unique datetime object for a date between January 1, 1970 and now.

    Args:
        fake: The `Faker` instance.
        tzinfo: timezone, instance of datetime.tzinfo subclass.
        end_datetime: if is set, this is the max date possible.
    """
    return unique(fake, date_time, tzinfo=tzinfo, end_datetime=end_datetime)

def date_time_ad(
    fake: object,
    tzinfo: Optional[datetime.tzinfo] = None,
    end_datetime: Optional[DateParseType] = None,
    start_datetime: Optional[DateParseType] = None,
) -> datetime.datetime:
    """
    Generate a datetime object for a date between January 1, 001 and now.

    Args:
        fake: The `Faker` instance.
        tzinfo: timezone, instance of datetime.tzinfo subclass.
        start_datetime: the start of the possible date range.
        end_datetime: the end of the possible date range.
    """
    return fake.date_time_ad(
        tzinfo=tzinfo,
        end_datetime=end_datetime,
        start_datetime=start_datetime,
    )

def unique_date_time_ad(
    fake: object,
    tzinfo: Optional[datetime.tzinfo] = None,
    end_datetime: Optional[DateParseType] = None,
    start_datetime: Optional[DateParseType] = None,
) -> datetime.datetime:
    """
    Generate a unique datetime object for a date between January 1, 001 and now.

    Args:
        fake: The `Faker` instance.
        tzinfo: timezone, instance of datetime.tzinfo subclass.
        start_datetime: the start of the possible date range.
        end_datetime: the end of the possible date range.
    """
    return unique(
        fake,
        date_time_ad,
        tzinfo=tzinfo,
        end_datetime=end_datetime,
        start_datetime=start_datetime,
    )

def date_time_between(
    fake: object,
    start_date: DateParseType = '-30y',
    end_date: DateParseType = 'now',
    tzinfo: Optional[datetime.tzinfo] = None,
) -> datetime.datetime:
    """
    Generate a datetime object between two given dates.

    Accepts date strings that can be recognized by strtotime().

    Args:
        fake: The `Faker` instance.
        start_date: the start of the possible date range.
        end_date: the end of the possible date range.
        tzinfo: timezone, instance of datetime.tzinfo subclass.
    """
    return fake.date_time_between(
        start_date=start_date,
        end_date=end_date,
        tzinfo=tzinfo,
    )

def unique_date_time_between(
    fake: object,
    start_date: DateParseType = '-30y',
    end_date: DateParseType = 'now',
    tzinfo: Optional[datetime.tzinfo] = None,
) -> datetime.datetime:
    """
    Generate a unique datetime object between two given dates.

    Accepts date strings that can be recognized by strtotime().

    Args:
        fake: The `Faker` instance.
        start_date: the start of the possible date range.
        end_date: the end of the possible date range.
        tzinfo: timezone, instance of datetime.tzinfo subclass.
    """
    return unique(
        fake,
        date_time_between,
        start_date=start_date,
        end_date=end_date,
        tzinfo=tzinfo,
    )

def date_time_between_dates(
    fake: object,
    datetime_start: Optional[DateParseType] = None,
    datetime_end: Optional[DateParseType] = None,
    tzinfo: Optional[datetime.tzinfo] = None,
) -> datetime.datetime:
    """
    Generate a datetime between two dates.

    Accepts datetime objects.

    Args:
        fake: The `Faker` instance.
        datetime_start: the start of the possible datetime range.
        datetime_end: the end of the possible datetime range.
        tzinfo: timezone, instance of datetime.tzinfo subclass.
    """
    return fake.date_time_between_dates(
        datetime_start=datetime_start,
        datetime_end=datetime_end,
        tzinfo=tzinfo,
    )

def unique_date_time_between_dates(
    fake: object,
    datetime_start: Optional[DateParseType] = None,
    datetime_end: Optional[DateParseType] = None,
    tzinfo: Optional[datetime.tzinfo] = None,
) -> datetime.datetime:
    """
    Generate a unique datetime between two dates.

    Accepts datetime objects.

    Args:
        fake: The `Faker` instance.
        datetime_start: the start of the possible datetime range.
        datetime_end: the end of the possible datetime range.
        tzinfo: timezone, instance of datetime.tzinfo subclass.
    """
    return unique(
        fake,
        date_time_between_dates,
        datetime_start=datetime_start,
        datetime_end=datetime_end,
        tzinfo=tzinfo,
    )

def date_time_this_century(
    fake: object,
    *,
    before_now: bool = True,
    after_now: bool = False,
    tzinfo: Optional[datetime.tzinfo] = None,
) -> datetime.datetime:
    """
    Generate a datetime object for the current century.

    Args:
        fake: The `Faker` instance.
        before_now: include days in current century before today.
        after_now: include days in current century after today.
        tzinfo: timezone, instance of datetime.tzinfo subclass.
    """
    return fake.date_time_this_century(
        before_now=before_now,
        after_now=after_now,
        tzinfo=tzinfo,
    )

def unique_date_time_this_century(
    fake: object,
    *,
    before_now: bool = True,
    after_now: bool = False,
    tzinfo: Optional[datetime.tzinfo] = None,
) -> datetime.datetime:
    """
    Generate a unique datetime object for the current century.

    Args:
        fake: The `Faker` instance.
        before_now: include days in current century before today.
        after_now: include days in current century after today.
        tzinfo: timezone, instance of datetime.tzinfo subclass.
    """
    return unique(
        fake,
        date_time_this_century,
        before_now=before_now,
        after_now=after_now,
        tzinfo=tzinfo,
    )

def date_time_this_decade(
    fake: object,
    *,
    before_now: bool = True,
    after_now: bool = False,
    tzinfo: Optional[datetime.tzinfo] = None,
) -> datetime.datetime:
    """
    Generate a datetime object for the current decade.

    Args:
        fake: The `Faker` instance.
        before_now: include days in current decade before today.
        after_now: include days in current decade after today.
        tzinfo: timezone, instance of datetime.tzinfo subclass.
    """
    return fake.date_time_this_decade(
        before_now=before_now,
        after_now=after_now,
        tzinfo=tzinfo,
    )

def unique_date_time_this_decade(
    fake: object,
    *,
    before_now: bool = True,
    after_now: bool = False,
    tzinfo: Optional[datetime.tzinfo] = None,
) -> datetime.datetime:
    """
    Generate a unique datetime object for the current decade.

    Args:
        fake: The `Faker` instance.
        before_now: include days in current decade before today.
        after_now: include days in current decade after today.
        tzinfo: timezone, instance of datetime.tzinfo subclass.
    """
    return unique(
        fake,
        date_time_this_decade,
        before_now=before_now,
        after_now=after_now,
        tzinfo=tzinfo,
    )

def date_time_this_month(
    fake: object,
    *,
    before_now: bool = True,
    after_now: bool = False,
    tzinfo: Optional[datetime.tzinfo] = None,
) -> datetime.datetime:
    """
    Generate a datetime object for the current month.

    Args:
        fake: The `Faker` instance.
        before_now: include days in current month before today.
        after_now: include days in current month after today.
        tzinfo: timezone, instance of datetime.tzinfo subclass.
    """
    return fake.date_time_this_month(
        before_now=before_now,
        after_now=after_now,
        tzinfo=tzinfo,
    )

def unique_date_time_this_month(
    fake: object,
    *,
    before_now: bool = True,
    after_now: bool = False,
    tzinfo: Optional[datetime.tzinfo] = None,
) -> datetime.datetime:
    """
    Generate a unique datetime object for the current month.

    Args:
        fake: The `Faker` instance.
        before_now: include days in current month before today.
        after_now: include days in current month after today.
        tzinfo: timezone, instance of datetime.tzinfo subclass.
    """
    return unique(
        fake,
        date_time_this_month,
        before_now=before_now,
        after_now=after_now,
        tzinfo=tzinfo,
    )

def date_time_this_year(
    fake: object,
    *,
    before_now: bool = True,
    after_now: bool = False,
    tzinfo: Optional[datetime.tzinfo] = None,
) -> datetime.datetime:
    """
    Generate a datetime object for the current year.

    Args:
        fake: The `Faker` instance.
        before_now: include days in current year before today.
        after_now: include days in current year after today.
        tzinfo: timezone, instance of datetime.tzinfo subclass.
    """
    return fake.date_time_this_year(
        before_now=before_now,
        after_now=after_now,
        tzinfo=tzinfo,
    )

def unique_date_time_this_year(
    fake: object,
    *,
    before_now: bool = True,
    after_now: bool = False,
    tzinfo: Optional[datetime.tzinfo] = None,
) -> datetime.datetime:
    """
    Generate a unique datetime object for the current year.

    Args:
        fake: The `Faker` instance.
        before_now: include days in current year before today.
        after_now: include days in current year after today.
        tzinfo: timezone, instance of datetime.tzinfo subclass.
    """
    return unique(
        fake,
        date_time_this_year,
        before_now=before_now,
        after_now=after_now,
        tzinfo=tzinfo,
    )

def future_date(
    fake: object,
    end_date: DateParseType = '+30d',
    tzinfo: Optional[datetime.tzinfo] = None,
) -> datetime.date:
    """
    Generate a random date object between 1 day from now and a given date.

    Accepts date strings that can be recognized by strtotime().

    Args:
        fake: The `Faker` instance.
        end_date: The max future date.
        tzinfo: timezone, instance of datetime.tzinfo subclass.
    """
    return fake.future_date(end_date=end_date, tzinfo=tzinfo)

def unique_future_date(
    fake: object,
    end_date: DateParseType = '+30d',
    tzinfo: Optional[datetime.tzinfo] = None,
) -> datetime.date:
    """
    Generate a unique random date object between 1 day from now and a given date.

    Accepts date strings that can be recognized by strtotime().

    Args:
        fake: The `Faker` instance.
        end_date: The max future date.
        tzinfo: timezone, instance of datetime.tzinfo subclass.
    """
    return unique(fake, future_date, end_date=end_date, tzinfo=tzinfo)

def future_datetime(
    fake: object,
    end_date: DateParseType = '+30d',
    tzinfo: Optional[datetime.tzinfo] = None,
) -> datetime.datetime:
    """
    Generate a random datetime object between 1 second from now and a given date.

    Accepts date strings that can be recognized by strtotime().

    Args:
        fake: The `Faker` instance.
        end_date: The max future date.
        tzinfo: timezone, instance of datetime.tzinfo subclass.
    """
    return fake.future_datetime(end_date=end_date, tzinfo=tzinfo)

def unique_future_datetime(
    fake: object,
    end_date: DateParseType = '+30d',
    tzinfo: Optional[datetime.tzinfo] = None,
) -> datetime.datetime:
    """
    Generate a unique datetime object between 1 second from now and a given date.

    Accepts date strings that can be recognized by strtotime().

    Args:
        fake: The `Faker` instance.
        end_date: The max future date.
        tzinfo: timezone, instance of datetime.tzinfo subclass.
    """
    return unique(fake, future_datetime, end_date=end_date, tzinfo=tzinfo)

def iso8601(
    fake: object,
    tzinfo: Optional[datetime.tzinfo] = None,
    end_datetime: Optional[DateParseType] = None,
    sep: str = 'T',
    timespec: str = 'auto',
) -> str:
    """
    Generate a timestamp in ISO 8601 format (or one of its profiles).

    Args:
        fake: The `Faker` instance.
        end_datetime: The max future datetime.
        tzinfo: timezone, instance of datetime.tzinfo subclass.
        sep: separator between date and time, defaults to 'T'.
        timespec: format specifier for the time part,
          defaults to 'auto' - see datetime.isoformat() documentation.

    Returns:
        A string with date into ISO 8601 format.
    """
    return fake.iso8601(
        tzinfo=tzinfo,
        end_datetime=end_datetime,
        sep=sep,
        timespec=timespec,
    )

def unique_iso8601(
    fake: object,
    tzinfo: Optional[datetime.tzinfo] = None,
    end_datetime: Optional[DateParseType] = None,
    sep: str = 'T',
    timespec: str = 'auto',
) -> str:
    """
    Generate a unique timestamp in ISO 8601 format (or one of its profiles).

    Args:
        fake: The `Faker` instance.
        end_datetime: The max future datetime.
        tzinfo: timezone, instance of datetime.tzinfo subclass.
        sep: separator between date and time, defaults to 'T'.
        timespec: format specifier for the time part,
          defaults to 'auto' - see datetime.isoformat() documentation.

    Returns:
        A string with date into ISO 8601 format.
    """
    return unique(
        fake,
        iso8601,
        tzinfo=tzinfo,
        end_datetime=end_datetime,
        sep=sep,
        timespec=timespec,
    )

def past_date(
    fake: object,
    start_date: DateParseType = '-30d',
    tzinfo: Optional[datetime.tzinfo] = None,
) -> datetime.date:
    """
    Generate a random date between a given date and 1 day ago.

    Accepts date strings that can be recognized by strtotime().

    Args:
        fake: The `Faker` instance.
        start_date: The minimum old date.
        tzinfo: timezone, instance of datetime.tzinfo subclass.
    """
    return fake.past_date(start_date=start_date, tzinfo=tzinfo)

def unique_past_date(
    fake: object,
    start_date: DateParseType = '-30d',
    tzinfo: Optional[datetime.tzinfo] = None,
) -> datetime.date:
    """
    Generate a unique date between a given date and 1 day ago.

    Accepts date strings that can be recognized by strtotime().

    Args:
        fake: The `Faker` instance.
        start_date: The minimum old date.
        tzinfo: timezone, instance of datetime.tzinfo subclass.
    """
    return unique(fake, past_date, start_date=start_date, tzinfo=tzinfo)

def past_datetime(
    fake: object,
    start_date: DateParseType = '-30d',
    tzinfo: Optional[datetime.tzinfo] = None,
) -> datetime.datetime:
    """
    Generate a random datetime between a given date and 1 second ago.

    Accepts date strings that can be recognized by strtotime().

    Args:
        fake: The `Faker` instance.
        start_date: The minimum old date.
        tzinfo: timezone, instance of datetime.tzinfo subclass
    """
    return fake.past_datetime(start_date=start_date, tzinfo=tzinfo)

def unique_past_datetime(
    fake: object,
    start_date: DateParseType = '-30d',
    tzinfo: Optional[datetime.tzinfo] = None,
) -> datetime.datetime:
    """
    Generate a unique datetime between a given date and 1 second ago.

    Accepts date strings that can be recognized by strtotime().

    Args:
        fake: The `Faker` instance.
        start_date: The minimum old date.
        tzinfo: timezone, instance of datetime.tzinfo subclass
    """
    return unique(fake, past_datetime, start_date=start_date, tzinfo=tzinfo)

def time(
    fake: object,
    pattern: str = '%H:%M:%S',
    end_datetime: Optional[DateParseType] = None,
) -> str:
    """Generate a time string (24h format by default)."""
    return fake.time(pattern=pattern, end_datetime=end_datetime)

def unique_time(
    fake: object,
    pattern: str = '%H:%M:%S',
    end_datetime: Optional[DateParseType] = None,
) -> str:
    """Generate a time string (24h format by default)."""
    return unique(fake, time, pattern=pattern, end_datetime=end_datetime)

def time_object(
    fake: object,
    end_datetime: Optional[DateParseType] = None,
) -> datetime.time:
    """Generate a time object."""
    return fake.time_object(end_datetime=end_datetime)

def unique_time_object(
    fake: object,
    end_datetime: Optional[DateParseType] = None,
) -> datetime.time:
    """Generate a unique time object."""
    return unique(fake, time_object, end_datetime=end_datetime)

def day_of_month(fake: object) -> str:
    """Generate a day of month."""
    return fake.day_of_month()

def unique_day_of_month(fake: object) -> str:
    """Generate a unique day of month."""
    return unique(fake, day_of_month)

def day_of_week(fake: object) -> str:
    """Generate a day of week."""
    return fake.day_of_week()

def unique_day_of_week(fake: object) -> str:
    """Generate a unique day of week."""
    return unique(fake, day_of_week)

def timezone(fake: object) -> str:
    """Generate a timezone."""
    return fake.timezone()

def unique_timezone(fake: object) -> str:
    """Generate a unique timezone."""
    return unique(fake, timezone)

def month(fake: object) -> str:
    """Generate a month."""
    return fake.month()

def unique_month(fake: object) -> str:
    """Generate a unique month."""
    return unique(fake, month)

def month_name(fake: object) -> str:
    """Generate a month name."""
    return fake.month_name()

def unique_month_name(fake: object) -> str:
    """Generate a unique month name."""
    return unique(fake, month_name)

def year(fake: object) -> str:
    """Generate a year."""
    return fake.year()

def unique_year(fake: object) -> str:
    """Generate a unique year."""
    return unique(fake, year)
