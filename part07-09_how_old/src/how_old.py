# Write your solution here
from datetime import datetime, timedelta

dob_day = int(input("Day: "))
dob_month = int(input("Month: "))
dob_year = int(input("Year: "))

dob = datetime(dob_year, dob_month, dob_day)
age_at_milenium = datetime(1999, 12, 31) - dob

if age_at_milenium.days < 0:
    print("You weren't born yet on the eve of the new millennium.")
else:
    print(f"You were {age_at_milenium.days} days old on the eve of the new millennium.")