from typing import Union
import datetime

# TODO: ListOfInt: TypeAlias = list[int]

DateTimeOptionalArg = Union[datetime.date, datetime.datetime, datetime.timedelta, str, int, None]
DateTimeArg = Union[datetime.date, datetime.datetime, datetime.timedelta, str, int]
