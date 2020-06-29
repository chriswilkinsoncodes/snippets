#!/usr/bin/env python3

import pytz

for time_zone_name in sorted(pytz.all_timezones_set):
    print(time_zone_name)