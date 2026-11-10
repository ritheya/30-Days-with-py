# Get the current day, month, year, hour, minute and timestamp from datetime module
from datetime import datetime
now=datetime.now()
print(now)
day=now.day
month=now.month
year=now.year
hour=now.hour
minute=now.minute
timestamp=now.timestamp()
print(day,month,year,hour,minute)
print('Tiestamp:',timestamp)
print(f'{day}/{month}/{year},{hour}:{minute}')
# Format the current date using this format: "%m/%d/%Y, %H:%M:%S")
time_strftime=now.strftime('%d/%m/%Y,%H:%M:%S')
print(time_strftime)
# Today is 5 December, 2019. Change this time string to time.
time_strptime='5 December,2019'
print(type(time_strptime))
time=datetime.strptime(time_strptime,'%d %B,%Y')
print(time)
print(type(time))
# Calculate the time difference between now and new year.
now_year=datetime.now()
new_year=datetime(now.year + 1,1,1)
diff=new_year-now_year
print(diff)
# Calculate the time difference between 1 January 1970 and now.
from datetime import date
now_date=date.today()
then=date(1970,1,1)
diffe=now_date-then
print(diffe)
# Think, what can you use the datetime module for? Examples:
 # Time series analysis
 # To get a timestamp of any activities in an application
 # Adding posts on a blog