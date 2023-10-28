from typing import Union, Optional
import datetime

DateTimeArg = Union[datetime.date, datetime.datetime, datetime.timedelta, str, int, None]
TimezoneArg = Optional[datetime.tzinfo]
