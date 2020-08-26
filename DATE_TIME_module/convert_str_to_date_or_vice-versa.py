##          Python | Convert string to DateTime and vice-versa

1.                  '''strptime() function'''
strptime() is available in datetime and time modules and is used for Date-Time Conversion.
This function changes the given string of datetime into the desired format.

Syntax: datetime.strptime(date_string,format)

##Examples:
##
##Input : Dec 4 2018 10:07AM 
##Output : 2018-12-04 10:07:00
##
##Input : Jun 12 2013 5:30PM 
##Output : 2013-06-12 17:30:00


from datetime import datetime

dt = 'Dec 4 2018 10:07AM'
formatt = '%b %d %Y %H:%M%p'
new_dt = datetime.strptime(dt,formatt)
print (new_dt,type(new_dt))

##2018-12-04 10:07:00 <class 'datetime.datetime'>



from datetime import datetime

dt_str = '2020-02-11 23:48:54.358220+05:30'

new_dt = datetime.strptime(dt_str,'%Y-%m-%d %H:%M:%S.%f%z')
print (new_dt,type(new_dt))

##2020-02-11 23:48:54.358220+05:30 <class 'datetime.datetime'>


2.                  '''strftime() function'''
Python strftime() function is present in datetime and time modules to create a string
representation based on the specified format string.

Syntax: datetime_object.strftime(format_str)

from datetime import datetime

dt = datetime.now()
formatt = '%b %d %Y %H:%M%p'
new_dt = dt.strftime(formatt)
print (new_dt,type(new_dt))

#Aug 10 2020 17:10PM <class 'str'>



                                '''A reference of all the legal format codes:'''

Directive	                Description	                        Example	

%a	            Weekday, short version	                        Wed	
%A	            Weekday, full version	                        Wednesday	
%w	            Weekday as a number 0-6,0 is Sunday	                3	
%d	            Day of month 01-31	                                31	
%b	            Month name, short version	                        Dec	
%B	            Month name, full version	                        December	
%m	            Month as a number 01-12	                        12	
%y	            Year, short version, without century                18
%Y	            Year, full version	                                2018	
%H	            Hour 00-23	                                        17	
%I	            Hour 00-12	                                        05	
%p	            AM/PM	                                        PM	
%M	            Minute 00-59	                                41	
%S	            Second 00-59	                                08	
%f	            Microsecond 000000-999999	                        548513	
%z	            UTC offset	                                        +0100	
%Z	            Timezone	                                        CST	
%j	            Day number of year 001-366	                        365	
%U	            Week number of year,                                52
                    Sunday as the first day of week,
                    00-53
%W	            Week number of year,                                52
                    Monday as the first day of week,
                    00-53		
%c	            Local version of date and time	                Mon Dec 31 17:41:00 2018	
%x	            Local version of date	                        12/31/18
%X	            Local version of time	                        17:41:00	
%%	            A % character	                                %
%X	            Local version of time	                        17:41:00	
%%	            A % character	                                %
%Y	            Year, full version	                                2018






