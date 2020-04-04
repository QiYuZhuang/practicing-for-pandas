import numpy as np
import pandas as pd

# question21: how to convert a series of data-strings to a time series?
ser = pd.Series(['01 Jan 2010', '02-02-2011', '20120303', '2013/04/04', '2014-05-05', '2015-06-06T12:20'])
print(ser)
# via pandas to_datetime
time_output = pd.to_datetime(ser)
print(time_output)
# via datautil
from dateutil.parser import parse

time_output = ser.map(lambda x: parse(x))
print(time_output)

# question22: how to get the day of month, week number, day of year and day of week from series of date strings?
ser = pd.Series(['01 Jan 2010', '02-02-2011', '20120303', '2013/04/04', '2014-05-05', '2015-06-06T12:20'])
day_list = pd.to_datetime(ser).dt.day.to_list()
day_of_year_list = pd.to_datetime(ser).dt.dayofyear.to_list()
week_list = pd.to_datetime(ser).dt.week.to_list()
year_list = pd.to_datetime(ser).dt.year.to_list()
weekday_list = pd.to_datetime(ser).dt.weekday_name.to_list()
print(day_list)  # day of week
print(day_of_year_list)
print(week_list)
print(year_list)
print(weekday_list)

# question23: how to convert year-month string to dates corresponding to the 4th day of the month?
ser = pd.Series(['Jan 2010', 'Feb 2011', 'Mar 2012'])
ser.map(lambda x: parse('04' + x))

# question24: how to filter words that contain at least 2 vowels from a series?
ser = pd.Series(['Apple', 'Orange', 'Plan', 'Python', 'School'])
vowels = list('aeiou')
list_output = []
for word in ser:
    count = 0
    for literal in list(word.lower()):
        if literal in vowels:
            count += 1
    if count > 2:
        list_output.append(word)

output = ser[ser.isin(list_output)]
print(output)

# how to filter valid emails from a series? (practicing for regex)
emails = pd.Series(['buying books at amazom.com', 'rameses@egypt.com', 'matt@t.co', 'narendra@modi.com'])
pattern = r'[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,4}'  # regex
import re
re_ = re.compile(pattern)
emails_output = emails[emails.str.contains(pat=re_, regex=True)]
print(emails_output)
# using mask
mask = emails.map(lambda x: bool(re.match(pattern, x)))
emails_output = emails[mask]
print(emails_output)
# via function findall
emails_output = emails.str.findall(pattern, flags=re.IGNORECASE)
print(emails_output)
