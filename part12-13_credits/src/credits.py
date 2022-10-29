from functools import reduce

class CourseAttempt:
    def __init__(self, course_name: str, grade: int, credits: int):
        self.course_name = course_name
        self.grade = grade
        self.credits = credits

    def __str__(self):
        return f"{self.course_name} ({self.credits} cr) grade {self.grade}"

# Write your solution
def credits_sum_helper(credit_sum, course):
        return credit_sum + course.credits

def grades_sum_helper(grades_sum, course):
        return grades_sum + course.grade

def sum_of_all_credits(courses: list):
    return reduce(credits_sum_helper, courses, 0)

def sum_of_passed_credits(courses: list):    
    return reduce(credits_sum_helper, filter(lambda x: x.grade >= 1, courses), 0)

def average(courses: list):
    passed_courses = list(filter(lambda x: x.grade >= 1, courses))
    return reduce(grades_sum_helper, passed_courses, 0) / len(passed_courses)
