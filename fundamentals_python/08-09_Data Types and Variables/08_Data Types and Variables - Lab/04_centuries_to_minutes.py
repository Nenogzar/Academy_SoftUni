years_per_century = 100
days_per_year = 365.2422
hours_per_day = 24
minutes_per_hour = 60

centuries = int(input())

years = centuries * years_per_century
days = int(years * days_per_year)
hours = days * hours_per_day
minutes = hours * minutes_per_hour

print(f"{centuries} centuries = {years} years = {days} days = {hours} hours = {minutes} minutes")
