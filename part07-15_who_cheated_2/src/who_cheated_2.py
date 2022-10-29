# Write your solution here
import csv
import datetime

def final_points():
    students = {}    
    time_limit = datetime.timedelta(hours = 3)
    with open("start_times.csv") as my_file:
        for line in csv.reader(my_file, delimiter=";"):
          students[line[0]] = {"start_time": datetime.datetime.strptime(line[1], "%H:%M"), "tasks" : {}}

    with open("submissions.csv") as my_file:
        for line in csv.reader(my_file, delimiter=";"):
            if datetime.datetime.strptime(line[-1], "%H:%M") - students[line[0]]["start_time"] < time_limit:
                if line[1] not in students[line[0]]["tasks"]:
                    students[line[0]]["tasks"][line[1]] = line[2]
                elif students[line[0]]["tasks"][line[1]] < line[2]:    
                    students[line[0]]["tasks"][line[1]] = line[2]

    total_points = {}
    for student, data in students.items():
        total_points[student] = 0
        for task, points in data["tasks"].items():
            total_points[student] += int(points)

    return total_points