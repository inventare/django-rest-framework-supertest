from typing import Union
import datetime

DateTimeOptionalArg = Union[datetime.date, datetime.datetime, datetime.timedelta, str, int, None]
DateTimeArg = Union[datetime.date, datetime.datetime, datetime.timedelta, str, int]
