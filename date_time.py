from datetime import datetime,time,date

now= datetime.now()
print(now)
current_date = date.today()
print(current_date)


print(dir(datetime))
#date class object
day= date.today()
print("year is", day.year)
print("month is", day.month)
print("day is ", day.day)

#time class object
time_= input("h:m:s")
a= datetime.strptime(time_,'%H:%M:%S')
print("hour", a.hour)
print("minute", a.minute)
print("second", a.second)

#strptime
cov= "20 december,2023"
a= datetime.strptime(cov, "%d %B,%Y")
print(a)
