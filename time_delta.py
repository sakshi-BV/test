from datetime import timedelta , time
print(dir(timedelta))
a=timedelta(hours=10 ,minutes=20)
b=timedelta(hours=10 ,minutes=20)
c = timedelta.__add__(a,b)
print(c)
print(c.total_seconds())