# wwite your solution here

if True:
    # this is never executed
    student_info = input("Student information: ")
    exercise_data = input("Exercises completed: ")
    exam_data = input("Exam points: ")
else:
    # hard-coded input
    student_info = "students1.csv"
    exercise_data = "exercises1.csv"
    exam_data = "exam_points1.csv"

names = {}
exercises = {}
exams = {}

with open(student_info) as new_file:
    for line in new_file:
        parts = line.split(";")
        if parts[0] == "id":
            continue
        names[parts[0]] = parts[1] + " " + parts[2].strip()

with open(exercise_data) as new_file:
    for line in new_file:
        parts = line.split(";")
        if parts[0] == "id":
            continue
        for i in range(1, len(parts)):
            parts[i] = int(parts[i])

        exercises[parts[0]] = parts[1:]

with open(exam_data) as new_file:
     for line in new_file:
        parts = line.split(";")
        if parts[0] == "id":
            continue
        for i in range(1, len(parts)):
            parts[i] = int(parts[i])

        exams[parts[0]] = parts[1:]

def grade(exam_points, exercise_points):
    grade = 0
    breakpoints = [15,18,21,24,28]
    for i in range(0, len(breakpoints)):
        if (exercise_points // 4) + exam_points >= breakpoints[i]:
            grade = i+1
    return grade


for id, name in names.items():
    if id in exercises:
        print(name, grade(sum(exams[id]), sum(exercises[id])))