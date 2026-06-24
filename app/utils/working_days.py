import holidays
import datetime as dt
from datetime import datetime

## CONST
COUNTRY_HOLIDAYS = holidays.country_holidays('BE')
DAYS_OFF = {5, 6}

"""
    Compute and return the number of working days between {start_date} (include) and {end_date} (include).
"""
def compute_working_days(start_date: datetime, end_date: datetime):
    working_days = 0
    current_date = start_date


    while current_date <= end_date:
        if current_date.weekday() not in DAYS_OFF and current_date not in COUNTRY_HOLIDAYS:
            working_days += 1

        current_date += dt.timedelta(days=1)

    return working_days