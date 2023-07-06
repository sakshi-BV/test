from datetime import datetime
import pytz
format = "%Y-%m-%d %H:%M:%S %Z%z"
original_tz = pytz.timezone('Asia/Kolkata')
converted_tz = pytz.timezone('US/Eastern')
datetime_object = datetime.now(original_tz)
print("Original Date & Time: in Asia/Kolkata ",datetime_object.strftime(format))

datetime_object = datetime.now(converted_tz )
print("Converted Date & Time: in US/Eastern TimeZone ",datetime_object.strftime(format))