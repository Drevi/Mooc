# tee ratkaisusi tänne

class Course:
    def __init__(self, name: str, grade: int, credits: int):
        self._name = name
        self._grade = grade
        self._credits = credits
    
    def grade(self):
        return self._grade
    
    def change_grade(self, grade: int):
        if grade > self._grade:
            self._grade = grade        
    
    def name(self):
        return self._name

    def credits(self):
        return self._credits

    
class CourseRecords:
    def __init__(self):
        self._courses = {}

    def add_course(self, name: str, grade: int, credits: int):
        if name not in self._courses:
            self._courses[name] = Course(name, grade, credits)
        else:
            self._courses[name].change_grade(grade)

    def search_course(self, name):
        if name not in self._courses:
            return None
        return self._courses[name]

    def all_courses(self):
        return self._courses     


class CourseApp:
    def __init__(self):
        self._records = CourseRecords()

    def help(self):
        print("1 add course")
        print("2 get course data")
        print("3 statistics")
        print("0 exit")

    def add_course(self):
        name = input("course: ")
        grade = int(input("grade: "))
        credits = int(input("credits: "))
        self._records.add_course(name, grade, credits)

    def get_data(self):
        name = input("course: ")
        course = self._records.search_course(name)
        if  course == None:
            print("no entry for this course")
        else: 
            print(f"{course.name()} ({course.credits()} cr) grade {course.grade()}")

    def statistics(self):
        courses = self._records.all_courses()
        credits = 0
        grades = 0
        distribution = [0,0,0,0,0,0]

        for course in courses.values():
            credits += course.credits()
            grades += course.grade()
            distribution[course.grade()] += 1

        print(f"{len(courses)} completed courses, a total of {credits} credits")
        print(f"mean {grades / len(courses):.1f}")
        print("grade distribution")
        for i in range(5, 0, -1):
            print(f"{i}: {'x' * distribution[i]}")


    def execute(self):
        self.help()
        while True:
            command = input("command: ")
            if command == "0":
                break
            elif command == "1":                
                self.add_course()
            elif command == "2":
                self.get_data()
            elif command == "3":
                self.statistics()
            else:
                self.help()
        

application = CourseApp()
application.execute()