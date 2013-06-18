import nose
from datetime import datetime, time
from nose.tools import *
import human_dates

#beginning_of tests
def test_beginning_of_year():
    date = datetime.strptime('Jun 13 2005  1:33PM', '%b %d %Y %I:%M%p')
    expected = datetime.strptime('Jan 1 2005  12:00AM', '%b %d %Y %I:%M%p')
    result = human_dates.beginning_of_year(date)
    eq_(expected, result)

def test_beginning_of_month():
    date = datetime.strptime('Jun 13 2005  1:33PM', '%b %d %Y %I:%M%p')
    expected = datetime.strptime('Jun 1 2005  12:00AM', '%b %d %Y %I:%M%p')
    result = human_dates.beginning_of_month(date)
    eq_(expected, result)

def test_beginning_of_day():
    date = datetime.strptime('Jun 1 2005  1:33PM', '%b %d %Y %I:%M%p')
    expected = datetime.strptime('Jun 1 2005  12:00AM', '%b %d %Y %I:%M%p')
    result = human_dates.beginning_of_day(date)
    eq_(expected, result)

def test_beginning_of_hour():
    date = datetime.strptime('Jun 1 2005  1:33PM', '%b %d %Y %I:%M%p')
    expected = datetime.strptime('Jun 1 2005  1:00PM', '%b %d %Y %I:%M%p')
    result = human_dates.beginning_of_hour(date)
    eq_(expected, result)

def test_beginning_of_minute():
    date = datetime.strptime('Jun 1 2005  1:33.123456PM', '%b %d %Y %I:%M.%f%p')
    expected = datetime.strptime('Jun 1 2005  1:33PM', '%b %d %Y %I:%M%p')
    result = human_dates.beginning_of_minute(date)
    eq_(expected, result)

#end_of tests
def test_end_of_year():
    date = datetime.strptime('Jun 13 2005  1:33PM', '%b %d %Y %I:%M%p')
    expected = datetime.strptime('Dec 31 2005  23:59:59.999999', '%b %d %Y %H:%M:%S.%f')
    result = human_dates.end_of_year(date)
    eq_(expected, result)

def test_end_of_month():
    date = datetime.strptime('Feb 13 2005  1:33PM', '%b %d %Y %I:%M%p')
    expected = datetime.strptime('Feb 28 2005  23:59:59.999999', '%b %d %Y %H:%M:%S.%f')
    result = human_dates.end_of_month(date)
    eq_(expected, result)

def test_end_of_month_leapyear():
    date = datetime.strptime('Feb 13 2008  1:33PM', '%b %d %Y %I:%M%p')
    expected = datetime.strptime('Feb 29 2008  23:59:59.999999', '%b %d %Y %H:%M:%S.%f')
    result = human_dates.end_of_month(date)
    eq_(expected, result)

def test_end_of_day():
    date = datetime.strptime('Jun 1 2005  1:33PM', '%b %d %Y %I:%M%p')
    expected = datetime.strptime('Jun 1 2005  23:59:59.999999', '%b %d %Y %H:%M:%S.%f')
    result = human_dates.end_of_day(date)
    eq_(expected, result)

def test_end_of_hour():
    date = datetime.strptime('Jun 1 2005  1:33PM', '%b %d %Y %I:%M%p')
    expected = datetime.strptime('Jun 1 2005  13:59:59.999999', '%b %d %Y %H:%M:%S.%f')
    result = human_dates.end_of_hour(date)
    eq_(expected, result)

def test_end_of_minute():
    date = datetime.strptime('Jun 1 2005  1:33.123456PM', '%b %d %Y %I:%M.%f%p')
    expected = datetime.strptime('Jun 1 2005  13:33:59.999999', '%b %d %Y %H:%M:%S.%f')
    result = human_dates.end_of_minute(date)
    eq_(expected, result)



if __name__ == "__main__":
    nose.run()