# Write your solution here
import datetime

file = input("Filename: ")
date = datetime.datetime.strptime(input("Starting date: "), "%d.%m.%Y")
days = int(input("How many days: "))
screen_time = {}
total_minutes = 0 

print("Please type in screen time in minutes on each day (TV computer mobile):")

for i in range(0, days):
    current_date = date + datetime.timedelta(days = i)
    scr_time = input(f"Screen time {current_date.strftime('%d.%m.%Y')}: ").split(' ')    
    screen_time[current_date] = [int(x) for x in scr_time]
    total_minutes += sum(screen_time[current_date])

with open(file, 'w') as f:
    current_date = date + datetime.timedelta(days = days-1)
    f.write(f"Time period: {date.strftime('%d.%m.%Y')}-{current_date.strftime('%d.%m.%Y')}\n")
    f.write(f"Total minutes: {total_minutes}\n")
    f.write(f"Average minutes: {total_minutes/days}\n")
    for i in range(0, days):
        current_date = date + datetime.timedelta(days = i)
        f.write(f"{current_date.strftime('%d.%m.%Y')}: {screen_time[current_date][0]}/{screen_time[current_date][1]}/{screen_time[current_date][2]}\n")
        
print(f"Data stored in file {file}")        





