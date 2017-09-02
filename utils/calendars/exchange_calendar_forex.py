#
# Copyright 2016 Quantopian, Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from datetime import time
from pandas.tseries.holiday import (
    Holiday,
    DateOffset,
    MO,
    weekend_to_monday,
    GoodFriday,
    EasterMonday,
)
from pytz import timezone

from .trading_calendar import (
    TradingCalendar,
    MONDAY,
    TUESDAY,
    HolidayCalendar)

# New Year's Day
LSENewYearsDay = Holiday(
    "New Year's Day",
    month=1,
    day=1,
    observance=weekend_to_monday,
)

class ForexCalendar(TradingCalendar):
    """
    Exchange calendar for the Forex

    Open Time: 0:00 AM, GMT
    Close Time: 23:59 PM, GMT    
    """

    @property
    def name(self):
        return "Forex"

    @property
    def tz(self):
        return timezone('UTC')

    @property
    def open_time(self):
        return time(0, 0)

    @property
    def close_time(self):
        return time(23, 59)

    @property
    def regular_holidays(self):
        return HolidayCalendar([])
