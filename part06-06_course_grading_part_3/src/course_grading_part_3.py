# tee ratkaisu tänne

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

print(f"{'name':30}{'exec_nbr':10}{'exec_pts.':10}{'exm_pts.':10}{'tot_pts.':10}{'grade':10}")
for id, name in names.items():
    if id in exercises:
        print(f"{name:30}{sum(exercises[id]):<10}{sum(exercises[id])//4:<10}{sum(exams[id]):<10}{sum(exams[id])+(sum(exercises[id])//4):<10}{grade(sum(exams[id]), sum(exercises[id])):<10}")