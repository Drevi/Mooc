# Write your solution here
import csv
import datetime

def cheaters():
    students = {}
    cheaters = []
    time_limit = datetime.timedelta(hours = 3)
    with open("start_times.csv") as my_file:
        for line in csv.reader(my_file, delimiter=";"):
          students[line[0]] = {"start_time": datetime.datetime.strptime(line[1], "%H:%M"), "cheater" : False}

    with open("submissions.csv") as my_file:
        for line in csv.reader(my_file, delimiter=";"):
            if datetime.datetime.strptime(line[-1], "%H:%M") - students[line[0]]["start_time"] > time_limit:
                students[line[0]]["cheater"] = True

    for student, info in students.items():
        if info["cheater"]:
            cheaters.append(student)

    return cheaters