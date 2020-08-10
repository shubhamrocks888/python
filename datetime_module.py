##          Python datetime module with examples

1.                            '''Date class'''

When an object of this class is instantiated, it represents a date in the format YYYY-MM-DD.
Constructor of this class needs three mandatory arguments year, month and date.

Constructor syntax: class datetime.date(year, month, day)
'''RETURN TYPE'''       <class 'datetime.date'>


Note –  If the argument is not an integer it will raise a TypeError and if it is outside the
        range a ValueError will be raised.

# Python program to demonstrate date class
from datetime import date

d = date(1992,8,15)
print (d)           #Output:1992-8-15
print (d.year)      #Output:1992
print (d.month)     #Output:8
print (d.day)       #Output:15
print (d.date)
#Output:
##AttributeError: 'datetime.date' object has no attribute 'date'

print (type(d))     #Output: <class 'datetime.date'>
print (type(d.year))#Output: <class 'int'>


  
2.                            '''Current date'''

To return the current local date today() function of date class is used.
today() function comes with several attributes (year, month and day).
These can be printed individually.

from datetime import date
today = date.today()
print (today)           #Output:2020-08-10
print (today.year)      #Output:2020
print (today.month)     #Output:8
print (today.day)       #Output:10


3.                            '''Time class'''

Time object represents local time, independent of any day.

Constructor Syntax: class datetime.time(hour=0, minute=0, second=0, microsecond=0, tzinfo=None, *, fold=0)

All the arguments are optional. tzinfo can be None otherwise all the attributes must be integer in the following range –
0 <= hour < 24
0 <= minute < 60
0 <= second < 60
0 <= microsecond < 1000000
fold in [0, 1]

from datetime import time
t = time(7,34,44)
print (t)               #Output:7:34:44
print (t.hour)          #Output:7
print (t.minute)        #Output:34
print (t.second)        #Output:44

print (time(hour=10))   #Output:10:00:00
print (time(minute=25)) #Output:00:25:00

print (type(t))         #Output: <class 'datetime.time'>
print (type(t.hour))    #Output: <class 'int'>



4.                            '''Datetime class'''

Information on both date and time is contained in this class. Like a date object,
datetime assumes the current Gregorian calendar extended in both directions;
like a time object, datetime assumes there are exactly 3600*24 seconds in every day.


Constructor Syntax: class datetime.datetime(year, month, day, hour=0, minute=0, second=0, microsecond=0, tzinfo=None, *, fold=0)
# tzinfo FOR TIMEZONE
The year, month and day arguments are mandatory. tzinfo can be None, rest all the attributes must be an integer.

from datetime import datetime
dt = datetime(1990,11,22,13,45,49)

print (dt)               #Output: 1990-11-22 13:45:49
print (dt.year)          #Output: 1990
print (dt.month)         #Output: 11
print (dt.day)           #Output: 22
print (dt.hour)          #Output: 13
print (dt.minute)        #Output: 45
print (dt.second)        #Output: 49


'''timestamp() function return the time expressed as the number of seconds that have passed since January 1, 1970.
That zero moment is known as the epoch.
Example #1: Use Timestamp. timestamp() function to return the number of seconds that has passed since the zero
moment for the given Timestamp object.'''

print(dt.timestamp())   #Output: 659261749.0

##NOTE: 1. only datetime object has attribute timestamp
        2. date has no attribute timestamp
        3. time has no attribute timestamp


print (type(dt))            #Output: <class 'datetime.datetime'>
print (type(dt.year))       #Output: <class 'int'>
print (type(dt.hour))       #Output: <class 'int'>



5.                               '''Current date and time'''

You can print the current date and time using the now() function. now() function returns the current local date and time.

from datetime import datetime

today = datetime.now()
print (today)                   #Output: 2020-08-10 10:21:15.773300
print (today.year,today.day)    #Output: 2020 10

print (datetime.now().date())   #Output: 2020-08-10
print (datetime.now().time())   #Output: 15:36:00.102964

6.                                '''Timedelta class'''

Python timedelta() function is present under datetime library which is generally used for calculating differences in dates
and also can be used for date manipulations in Python. It is one of the easiest ways to perform date manipulations.

Constructor syntax: class datetime.timedelta(days=0, seconds=0, microseconds=0, milliseconds=0, minutes=0, hours=0, weeks=0)

Returns : Date

# Timedelta function demonstration   
from datetime import datetime,date,timedelta

d           = date.today()
future_date = d + timedelta(days=2)
past_date   = d - timedelta(days=2)

print (d)            #Output: 2020-08-10
print (future_date)  #Output: 2020-08-12
print (past_date)    #Output: 2020-08-08

d = datetime.now()
future_date = d + timedelta(days=365)
past_date   = d - timedelta(days=365)

print (d)           #Output: 2020-08-10 15:41:42.621804
print (future_date) #Output: 2021-08-10 15:41:42.621804
print (past_date)   #Output: 2019-08-11 15:41:42.621804

x = timedelta(days=2)
print (x)            #Output: 2 days, 0:00:00         
print (type(x))      #Output: <class 'datetime.timedelta'>

'''time delta does not work with time'''
t = time(7,45,23)
print (t+timedelta(hours=2))
#Output:
TypeError: unsupported operand type(s) for +: 'datetime.time' and 'datetime.timedelta'


7.                              '''pytz module'''   #For TimeZone

from datetime import datetime
import pytz

dt_today = datetime.datetime.today()   #datetime without timezone
dt_now = datetime.datetime.now()       #datetime with timezone(rightnow it is empty)
dt_utcnow = datetime.datetime.utcnow() #datetime with timezone(rightnow it is empty)

dt_tz     = datetime(1990,5,20,9,35,54,tzinfo=pytz.UTC)
dt_now    = datetime.now(tz=pytz.UTC)
dt_utcnow = datetime.utcnow().replace(tzinfo=pytz.UTC)

print (dt_tz)                          #1990-05-20 09:35:54+00:00
print (dt_now)                         #2020-08-10 10:41:35.609597+00:00
print (dt_utcnow)                      #2020-08-10 10:44:44.337134+00:00

for tz in pytz.all_timezones:
    print (tz,end=" ")

#Output:
Africa/Abidjan  Africa/Accra  Africa/Addis_Ababa -----------------------Zulu

##datetime with timezone
print (datetime.now(tz=pytz.timezone('Asia/Calcutta')))  #2020-08-10 16:20:39.987205+05:30










