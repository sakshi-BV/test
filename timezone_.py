from datetime import datetime
import pytz
local = datetime.now()
print("Local:", local.strftime("%m/%d/%Y, %H:%M:%S"))


tz_us=pytz.timezone('Europe/London')
datetime_us= datetime.now(tz_us)
print("us:", datetime_us.strftime("%m/%d/%Y, %H:%M:%S"))

tz_ind=pytz.timezone('Asia/Kolkata')
datetime_ind= datetime.now(tz_ind)
print("us:", datetime_ind.strftime("%m/%d/%Y, %H:%M:%S"))
print("sakshi")