# Write your solution here
import urllib.request
import json
from math import floor

def retrieve_all():
    request = urllib.request.urlopen("https://studies.cs.helsinki.fi/stats-mock/api/courses")
    course_dl = json.loads(request.read())
    courses = []    
    for course in course_dl:
        if course["enabled"]:
            courses.append((course["fullName"],course["name"],course["year"], sum(course["exercises"])))

    return courses        


def retrieve_course(course_name: str):    
    request = urllib.request.urlopen(f"https://studies.cs.helsinki.fi/stats-mock/api/courses/{course_name}/stats")
    course_dl = json.loads(request.read())
    course = {"weeks": len(course_dl), "students": 0, "hours": 0, "hours_average": 0, "exercises": 0, "exercises_average":0}

    for no, week in course_dl.items():
        if week["students"] > course["students"]:
            course["students"] = week["students"]
        course["hours"] += week["hour_total"]
        course["exercises"] += week["exercise_total"]
    course["hours_average"] = floor(course["hours"] / course["students"])
    course["exercises_average"] = floor(course["exercises"] / course["students"])

    return course













