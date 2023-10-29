import datetime
from typing import Union

# TODO: ListOfInt: TypeAlias = list[int]

DateTimeOptionalArg = Union[datetime.date, datetime.datetime, datetime.timedelta, str, int, None]
DateTimeArg = Union[datetime.date, datetime.datetime, datetime.timedelta, str, int]
