"""
The year attribute of a date or datetime object simply returns the year of that
date.

The isocalendar() returns a named tuple object with three components: year,
week and weekday.

The ISO calendar is a widely used variant of the Gregorian calendar.

The ISO year consists of 52 or 53 full weeks, and where a week starts on a
Monday and ends on a Sunday. The first week of an ISO year is the first
(Gregorian) calendar week of a year containing a Thursday. This is called week
number 1, and the ISO year of that Thursday is the same as its Gregorian year.

For example, 2004 begins on a Thursday, so the first week of ISO year 2004
begins on Monday, 29 Dec 2003 and ends on Sunday, 4 Jan 2004:
"""

from datetime import date

today = date.today()

today_year = today.year
iso_year = today.isocalendar()[0]