"""
Whereas most countries use a 24-hour clock, the United States tends to use a 12-hour clock.
Accordingly, instead of “09:00 to 17:00”, many Americans would say they work “9:00 AM to 5:00 PM” (or “9 AM to 5 PM”),
wherein “AM” is an abbreviation for “ante meridiem” and “PM” is an abbreviation for “post meridiem”, wherein “meridiem” means midday (i.e., noon).

Conversion Table
In a file called working.py,
implement a function called convert that expects a str in any of the 12-hour formats below and returns the corresponding str in 24-hour format
(i.e., 9:00 to 17:00). Expect that AM and PM will be capitalized (with no periods therein) and that there will be a space before each.
Assume that these times are representative of actual times, not necessarily 9:00 AM and 5:00 PM specifically.

9:00 AM to 5:00 PM
9 AM to 5 PM
9:00 AM to 5 PM
9 AM to 5:00 PM
Raise a ValueError instead if the input to convert is not in either of those formats or if either time is invalid (e.g., 12:60 AM, 13:00 PM, etc.).
But do not assume that someone's hours will start ante meridiem and end post meridiem;
someone might work late and even long hours (e.g., 5:00 PM to 9:00 AM).

Structure working.py as follows, wherein you're welcome to modify main and/or implement other functions as you see fit,
but you may not import any other libraries. You're welcome, but not required, to use re and/or sys.

import re
import sys


def main():
    print(convert(input("Hours: ")))


def convert(s):
    ...


...


if __name__ == "__main__":
    main()
Either before or after you implement convert in working.py, additionally implement, in a file called test_working.py,
three or more functions that collectively test your implementation of convert thoroughly,
each of whose names should begin with test_ so that you can execute your tests with:

pytest test_working.py
"""
import re

def main():
    print(convert(input("Hours: ")))

def convert(s):
    new_start = ""
    new_stop = ""
    try:
        start, stop = isValid(s)
    except ValueError:
        raise ValueError
    if place_holder := re.search(r"(\d+)(\:\d\d)? ([AP]M)", start):
        time_0 = int(place_holder.group(1))
        if time_0 == 12:
            time_0 = 0
        if place_holder.group(3) == 'PM':
            time_0 += 12
        if place_holder.group(2) != None:
            new_start += f"{time_0:02}{place_holder.group(2)}"
        else:
            new_start += f"{time_0:02}:00"
    if place_holder := re.search(r"(\d+)(\:\d\d)? ([AP]M)", stop):
        time_0 = int(place_holder.group(1))
        if time_0 == 12:
            time_0 = 0
        if place_holder.group(3) == 'PM':
            time_0 += 12
        if place_holder.group(2) != None:
            new_stop += f"{time_0:02}{place_holder.group(2)}"
        else:
            new_stop += f"{time_0:02}:00"
    return str(f"{new_start} to {new_stop}")

def isValid(s):
    if time := re.search(r"^((\d+)(?:\:(\d+))? [AP]M) to ((\d+)(?:\:(\d+))? [AP]M)$", s):
        pass
    else:
        raise ValueError
    if int(time.group(2)) > 12 or int(time.group(2)) < 1:
        raise ValueError
    if int(time.group(5)) > 12 or int(time.group(5)) < 1:
        raise ValueError
    if time.group(3):
        if int(time.group(3)) > 59 or int(time.group(3)) < 0:
            raise ValueError
    if time.group(6):
        if int(time.group(6)) > 59 or int(time.group(6)) < 0:
            raise ValueError
    return time.group(1), time.group(4)

if __name__ == "__main__":
    main()