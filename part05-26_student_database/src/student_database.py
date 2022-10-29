# Write your solution here

def add_student(database : dict, student: str):
    database[student] = []


def print_student(database : dict, student: str):
    if student not in database:
        print(f"{student}: no such person in the database")
    elif database[student] == []:
        print(f"{student}:")
        print(" no completed courses")
    else:
        print(f"{student}:")
        grade = 0
        print(f" {len(database[student])} completed courses:")
        for course, score in database[student]:
            print(" ",course, score )
            grade += score   
        print(f" average grade {grade/len(database[student]):.1f}") 




def add_course(database : dict, student: str, course: tuple):
    if course[1] == 0:
        return

    for name, courses in database.items():
        if name == student:    
            for crse in courses:
                if crse[0] == course[0]:
                    if crse[1] >= course[1]:
                        return
                    if crse[1] < course[1]:
                        database[student].remove(crse)

    database[student].append(course)
   

def summary(database : dict):
    most_courses = [0, ""]    
    best_avg = [0, ""]

    for name, courses in database.items():
        total_courses = len(database[name])
        if total_courses >  most_courses[0]:
            most_courses[0],most_courses[1] = total_courses, name
        grades = 0
        for course in courses:
            grades += course[1]
        avg_grades = grades /  len(database[name])
        if avg_grades > best_avg[0]:
              best_avg[0],best_avg[1] = avg_grades, name

    print(f"students {len(database)}")
    print("most courses completed", most_courses[0], most_courses[1])
    print("best average grade", best_avg[0], best_avg[1])








# def main():
#     students = {}
#     add_student(students, "Peter")
#     add_student(students, "Eliza")
#     add_course(students, "Peter", ("Data Structures and Algorithms", 1))
#     add_course(students, "Peter", ("Introduction to Programming", 1))
#     add_course(students, "Peter", ("Advanced Course in Programming", 1))
#     add_course(students, "Eliza", ("Introduction to Programming", 5))
#     add_course(students, "Eliza", ("Introduction to Computer Science", 4))
#     summary(students)


# main()










