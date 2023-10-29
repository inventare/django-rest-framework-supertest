from django.test import TestCase

from rest_framework_supertest.shortcuts import dates

from .base import FakerMockMixin


class DatesShortcutsTests(FakerMockMixin, TestCase):
    def test_am_pm(self):
        self.exec_test(['am_pm'], dates, 'am_pm')

    def test_century(self):
        self.exec_test(['century'], dates, 'century')

    def test_unique_century(self):
        self.exec_test(['unique', 'century'], dates, 'unique_century')

    def test_date(self):
        pattern = "%d/%m/%Y"
        end_datetime = None
        self.exec_test(['date'], dates, 'date', pattern=pattern, end_datetime=end_datetime)

    def test_unique_date(self):
        pattern = "%d/%m/%Y"
        end_datetime = None
        self.exec_test(['unique', 'date'], dates, 'unique_date', pattern=pattern, end_datetime=end_datetime)

    def test_date_between(self):
        start_date = '-10y'
        end_date = '+10y'
        self.exec_test(['date_between'], dates, 'date_between', start_date=start_date, end_date=end_date)

    def test_unique_date_between(self):
        start_date = '-10y'
        end_date = '+10y'
        self.exec_test(['unique', 'date_between'], dates, 'unique_date_between', start_date=start_date, end_date=end_date)

    def test_date_between_dates(self):
        date_start = None
        date_end = None
        self.exec_test(['date_between_dates'], dates, 'date_between_dates', date_start=date_start, date_end=date_end)

    def test_unique_date_between_dates(self):
        date_start = None
        date_end = None
        self.exec_test(['unique', 'date_between_dates'], dates, 'unique_date_between_dates', date_start=date_start, date_end=date_end)

    def test_date_object(self):
        end_datetime = None
        self.exec_test(['date_object'], dates, 'date_object', end_datetime=end_datetime)

    def test_unique_date_object(self):
        end_datetime = None
        self.exec_test(['unique', 'date_object'], dates, 'unique_date_object', end_datetime=end_datetime)

    def test_date_of_birth(self):
        tzinfo = None
        minimum_age = 20
        maximum_age = 90
        self.exec_test(['date_of_birth'], dates, 'date_of_birth', tzinfo=tzinfo, minimum_age=minimum_age, maximum_age=maximum_age)

    def test_unique_date_of_birth(self):
        tzinfo = None
        minimum_age = 20
        maximum_age = 90
        self.exec_test(['unique', 'date_of_birth'], dates, 'unique_date_of_birth', tzinfo=tzinfo, minimum_age=minimum_age, maximum_age=maximum_age)

    def test_date_this_century(self):
        before_today = False
        after_today = True
        self.exec_test(['date_this_century'], dates, 'date_this_century', before_today=before_today, after_today=after_today)

    def test_unique_date_this_century(self):
        before_today = False
        after_today = True
        self.exec_test(['unique', 'date_this_century'], dates, 'unique_date_this_century', before_today=before_today, after_today=after_today)

    def test_date_this_decade(self):
        before_today = False
        after_today = True
        self.exec_test(['date_this_decade'], dates, 'date_this_decade', before_today=before_today, after_today=after_today)

    def test_unique_date_this_decade(self):
        before_today = False
        after_today = True
        self.exec_test(['unique', 'date_this_decade'], dates, 'unique_date_this_decade', before_today=before_today, after_today=after_today)

    def test_date_this_month(self):
        before_today = False
        after_today = True
        self.exec_test(['date_this_month'], dates, 'date_this_month', before_today=before_today, after_today=after_today)

    def test_unique_date_this_month(self):
        before_today = False
        after_today = True
        self.exec_test(['unique', 'date_this_month'], dates, 'unique_date_this_month', before_today=before_today, after_today=after_today)

    def test_date_this_year(self):
        before_today = False
        after_today = True
        self.exec_test(['date_this_year'], dates, 'date_this_year', before_today=before_today, after_today=after_today)

    def test_unique_date_this_year(self):
        before_today = False
        after_today = True
        self.exec_test(['unique', 'date_this_year'], dates, 'unique_date_this_year', before_today=before_today, after_today=after_today)

    def test_date_time(self):
        tzinfo = None
        end_datetime = None
        self.exec_test(['date_time'], dates, 'date_time', tzinfo=tzinfo, end_datetime=end_datetime)

    def test_unique_date_time(self):
        tzinfo = None
        end_datetime = None
        self.exec_test(['unique', 'date_time'], dates, 'unique_date_time', tzinfo=tzinfo, end_datetime=end_datetime)

    def test_date_time_ad(self):
        tzinfo = None
        end_datetime = None
        start_datetime = None
        self.exec_test(['date_time_ad'], dates, 'date_time_ad', tzinfo=tzinfo, end_datetime=end_datetime, start_datetime=start_datetime)

    def test_unique_date_time_ad(self):
        tzinfo = None
        end_datetime = None
        start_datetime = None
        self.exec_test(['unique', 'date_time_ad'], dates, 'unique_date_time_ad', tzinfo=tzinfo, end_datetime=end_datetime, start_datetime=start_datetime)

    def test_date_time_between(self):
        tzinfo = None
        start_date = '-30y'
        end_date = 'now'
        self.exec_test(['date_time_between'], dates, 'date_time_between', tzinfo=tzinfo, start_date=start_date, end_date=end_date)

    def test_unique_date_time_between(self):
        tzinfo = None
        start_date = '-30y'
        end_date = 'now'
        self.exec_test(['unique', 'date_time_between'], dates, 'unique_date_time_between', tzinfo=tzinfo, start_date=start_date, end_date=end_date)

    def test_date_time_between_dates(self):
        tzinfo = None
        datetime_start = None,
        datetime_end = None
        self.exec_test(['date_time_between_dates'], dates, 'date_time_between_dates', tzinfo=tzinfo, datetime_start=datetime_start, datetime_end=datetime_end)

    def test_unique_date_time_between_dates(self):
        tzinfo = None
        datetime_start = None,
        datetime_end = None
        self.exec_test(['unique', 'date_time_between_dates'], dates, 'unique_date_time_between_dates', tzinfo=tzinfo, datetime_start=datetime_start, datetime_end=datetime_end)

    def test_date_time_this_century(self):
        tzinfo = None
        before_now = False
        after_now = True
        self.exec_test(['date_time_this_century'], dates, 'date_time_this_century', tzinfo=tzinfo, before_now=before_now, after_now=after_now)

    def test_unique_date_time_this_century(self):
        tzinfo = None
        before_now = False
        after_now = True
        self.exec_test(['unique', 'date_time_this_century'], dates, 'unique_date_time_this_century', tzinfo=tzinfo, before_now=before_now, after_now=after_now)

    def test_date_time_this_decade(self):
        tzinfo = None
        before_now = False
        after_now = True
        self.exec_test(['date_time_this_decade'], dates, 'date_time_this_decade', tzinfo=tzinfo, before_now=before_now, after_now=after_now)

    def test_unique_date_time_this_decade(self):
        tzinfo = None
        before_now = False
        after_now = True
        self.exec_test(['unique', 'date_time_this_decade'], dates, 'unique_date_time_this_decade', tzinfo=tzinfo, before_now=before_now, after_now=after_now)

    def test_date_time_this_month(self):
        tzinfo = None
        before_now = False
        after_now = True
        self.exec_test(['date_time_this_month'], dates, 'date_time_this_month', tzinfo=tzinfo, before_now=before_now, after_now=after_now)

    def test_unique_date_time_this_month(self):
        tzinfo = None
        before_now = False
        after_now = True
        self.exec_test(['unique', 'date_time_this_month'], dates, 'unique_date_time_this_month', tzinfo=tzinfo, before_now=before_now, after_now=after_now)

    def test_date_time_this_year(self):
        tzinfo = None
        before_now = False
        after_now = True
        self.exec_test(['date_time_this_year'], dates, 'date_time_this_year', tzinfo=tzinfo, before_now=before_now, after_now=after_now)

    def test_unique_date_time_this_year(self):
        tzinfo = None
        before_now = False
        after_now = True
        self.exec_test(['unique', 'date_time_this_year'], dates, 'unique_date_time_this_year', tzinfo=tzinfo, before_now=before_now, after_now=after_now)

    def test_day_of_month(self):
        self.exec_test(['day_of_month'], dates, 'day_of_month')

    def test_unique_day_of_month(self):
        self.exec_test(['unique', 'day_of_month'], dates, 'unique_day_of_month')

    def test_day_of_week(self):
        self.exec_test(['day_of_week'], dates, 'day_of_week')

    def test_unique_day_of_week(self):
        self.exec_test(['unique', 'day_of_week'], dates, 'unique_day_of_week')

    def test_future_date(self):
        end_date = '+20d'
        tzinfo = None
        self.exec_test(['future_date'], dates, 'future_date', end_date=end_date, tzinfo=tzinfo)

    def test_unique_future_date(self):
        end_date = '+20d'
        tzinfo = None
        self.exec_test(['unique', 'future_date'], dates, 'unique_future_date', end_date=end_date, tzinfo=tzinfo)

    def test_future_datetime(self):
        end_date = '+20d'
        tzinfo = None
        self.exec_test(['future_datetime'], dates, 'future_datetime', end_date=end_date, tzinfo=tzinfo)

    def test_unique_future_datetime(self):
        end_date = '+20d'
        tzinfo = None
        self.exec_test(['unique', 'future_datetime'], dates, 'unique_future_datetime', end_date=end_date, tzinfo=tzinfo)

    def test_iso8601(self):
        tzinfo = None
        end_datetime = '+20y'
        sep = '@'
        timespec = 'auto'
        self.exec_test(['iso8601'], dates, 'iso8601', end_datetime=end_datetime, tzinfo=tzinfo, sep=sep, timespec=timespec)

    def test_unique_iso8601(self):
        tzinfo = None
        end_datetime = '+20y'
        sep = '@'
        timespec = 'auto'
        self.exec_test(['unique', 'iso8601'], dates, 'unique_iso8601', end_datetime=end_datetime, tzinfo=tzinfo, sep=sep, timespec=timespec)

    def test_month(self):
        self.exec_test(['month'], dates, 'month')

    def test_unique_month(self):
        self.exec_test(['unique', 'month'], dates, 'unique_month')

    def test_month_name(self):
        self.exec_test(['month_name'], dates, 'month_name')

    def test_unique_month_name(self):
        self.exec_test(['unique', 'month_name'], dates, 'unique_month_name')

    def test_past_date(self):
        start_date = '-20d'
        tzinfo = None
        self.exec_test(['past_date'], dates, 'past_date', start_date=start_date, tzinfo=tzinfo)

    def test_unique_past_date(self):
        start_date = '-20d'
        tzinfo = None
        self.exec_test(['unique', 'past_date'], dates, 'unique_past_date', start_date=start_date, tzinfo=tzinfo)

    def test_past_datetime(self):
        start_date = '-20d'
        tzinfo = None
        self.exec_test(['past_datetime'], dates, 'past_datetime', start_date=start_date, tzinfo=tzinfo)

    def test_unique_past_datetime(self):
        start_date = '-20d'
        tzinfo = None
        self.exec_test(['unique', 'past_datetime'], dates, 'unique_past_datetime', start_date=start_date, tzinfo=tzinfo)

    def test_time(self):
        pattern = '%H:%M:%S'
        end_datetime = '20d'
        self.exec_test(['time'], dates, 'time', pattern=pattern, end_datetime=end_datetime)

    def test_unique_time(self):
        pattern = '%H:%M:%S'
        end_datetime = '20d'
        self.exec_test(['unique', 'time'], dates, 'unique_time', pattern=pattern, end_datetime=end_datetime)

    def test_time_object(self):
        end_datetime = '20d'
        self.exec_test(['time_object'], dates, 'time_object', end_datetime=end_datetime)

    def test_unique_time_object(self):
        end_datetime = '20d'
        self.exec_test(['unique', 'time_object'], dates, 'unique_time_object', end_datetime=end_datetime)

    def test_timezone(self):
        self.exec_test(['timezone'], dates, 'timezone')

    def test_unique_timezone(self):
        self.exec_test(['unique', 'timezone'], dates, 'unique_timezone')

    def test_year(self):
        self.exec_test(['year'], dates, 'year')

    def test_unique_year(self):
        self.exec_test(['unique', 'year'], dates, 'unique_year')
