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
        end_date = '+10y';
        self.exec_test(['date_between'], dates, 'date_between', start_date=start_date, end_date=end_date)

    def test_unique_date_between(self):
        start_date = '-10y'
        end_date = '+10y';
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
