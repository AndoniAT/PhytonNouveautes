from datetime import datetime, timezone
from zoneinfo import ZoneInfo

# 1) DateTime

print(datetime.now(tz=timezone.utc))

# Setting datatime in parameters
print(datetime(2020, 9, 8, 15, 4, 15, 361413, tzinfo=timezone.utc))

# zoneinfo allow you to get into the database IANA (Internet Assignet Numbers Authority) datetime
# They update their database many times par year
print(ZoneInfo("America/Vancouver"))
print(ZoneInfo(key='America/Vancouver'))


