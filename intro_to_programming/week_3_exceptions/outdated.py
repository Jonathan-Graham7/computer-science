"""
In the United States, dates are typically formatted in month-day-year order (MM/DD/YYYY),
otherwise known as middle-endian order, which is arguably bad design.
Dates in that format can't be easily sorted because the date's year comes last instead of first.
Try sorting, for instance, 2/2/1800, 3/3/1900, and 1/1/2000 chronologically in any program (e.g., a spreadsheet).
Dates in that format are also ambiguous. Harvard was founded on September 8, 1636, but 9/8/1636 could also be interpreted as August 9, 1636!

Fortunately, computers tend to use ISO 8601, an international standard that prescribes that dates should be formatted in year-month-day
(YYYY-MM-DD) order, no matter the country, formatting years with four digits, months with two digits,
and days with two digits, “padding” each with leading zeroes as needed.

In a file called outdated.py, implement a program that prompts the user for a date, anno Domini, in month-day-year order,
formatted like 9/8/1636 or September 8, 1636, wherein the month in the latter might be any of the values in the list below:

[
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]
Then output that same date in YYYY-MM-DD format. If the user's input is not a valid date in either format, prompt the user again.
Assume that every month has no more than 31 days; no need to validate whether a month has 28, 29, 30, or 31 days.
"""
def main():
    date_given = formatDate()
    interpretDate(date_given)
    return

def formatDate():
    while True:
        date = input("Date: ")
        if "/" in date:
            date = date.split("/")
            if slashDateVerify(date):
                return date
            continue
        elif "," in date:
            date = date.split(" ")
            date[1] = date[1].removesuffix(",")
            if commaDateVerify(date):
                return date
            continue
        else:
            continue

def slashDateVerify(date):
    try:
        date[0] = int(date[0])
        date[1] = int(date[1])
        date[2] = int(date[2])
    except ValueError:
        return False
    else:
        if date[0] > 12 or date[1] > 30:
            return False
    return True

def commaDateVerify(date):
    try:
        date[1] = int(date[1])
        date[2] = int(date[2])
    except ValueError:
        return False
    else:
        if date[1] > 30:
            return False
    return True

def interpretDate(date):
    try:
        int(date[0])
    except ValueError:
        months = [
            "January",
            "February",
            "March",
            "April",
            "May",
            "June",
            "July",
            "August",
            "September",
            "October",
            "November",
            "December"
        ]
        month_num = 1
        for month in months:
            if date[0] == month:
                month_num += months.index(month)
        print(f"{date[2]}-{month_num:02}-{date[1]:02}")
    else:
        print(f"{date[2]}-{date[0]:02}-{date[1]:02}")

main()