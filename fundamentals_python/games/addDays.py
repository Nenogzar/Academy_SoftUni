import datetime


def isLeapYear(year):
    return (year % 4 == 0) and (year % 100 != 0 or year % 400 == 0)

monthDays = {
    1: 31, 2: 28, 3: 31, 4: 30, 5: 31, 6: 30, 7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31,
}
def daysInMonth(year, month):
    if month == 2 and isLeapYear(year):
        return 29
    return monthDays[month]

def addDays(year:int, month:int, day:int, nDays:int) -> tuple[int, int, int]:
    outpYear, outpMonth, outpDay = year, month, day

    # First, increment full years
    if nDays >= 365:
        years = nDays // 365
        outpYear += years
        nDays -= years * 365

    # Second, increment months
    while nDays > 0:
        monthDays = daysInMonth(outpYear, outpMonth)
        # nDays beyond this month
        if nDays >= monthDays:
            nDays -= monthDays
            outpMonth += 1
        # output date in the next month
        elif nDays + outpDay > monthDays:
            s = nDays + outpDay
            s -= monthDays
            outpDay = s
            nDays = 0
            outpMonth += 1
        else:
            outpDay += nDays
            nDays = 0
        # in the next month
        if outpMonth > 12: # next year
            outpMonth = 1
            outpYear += 1
        if outpDay == 0:
            outpDay = 1
    return outpYear, outpMonth, outpDay


for nDays in range(0, 365*3):
    computed = addDays(1970, 1, 1, nDays)
    computed_dt = datetime.date(computed[0], computed[1], computed[2])
    expected = datetime.date(1970, 1, 1) + datetime.timedelta(days=nDays)
    if computed_dt != expected:
        print(nDays, 'disagree', computed_dt, expected)