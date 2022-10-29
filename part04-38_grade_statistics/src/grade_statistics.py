# Write your solution here

def points_input():
    points = input("Exam points and exercises completed:").split()
    for i in range(0, len(points)):
        points[i] = int(points[i])  
    
    return points


def grading(points: list):
    grades = [0, 0]
    grades[0] = points[0] + (points[1] // 10)
    grade_limits = [0, 15, 18, 21, 24, 28]
    for i in range(5,-1,-1):
        if grades[0] >= grade_limits[i]:
            grades[1] = i
            break    
    if points[0] < 10:
        grades[1] = 0  
    
    return(grades)


def statistics(points_average, pass_percentage, grade_distribution: list):
    print("Statistics:")
    print(f"Points average: {points_average:.1f}")
    print(f"Pass percentage: {pass_percentage:.1f}")
    print("Grade distribution:")
    for i in range(5, -1, -1):
        stars = "*" * grade_distribution[i]
        print(f"  {i}: {stars}")    


def main():
    avg_points = 0
    pass_percent = 0
    grade_dist = [0] * 6

    while True:
        points = points_input()
        if points == []:
            break
        graded_points = grading(points)
        grade_dist[graded_points[1]] += 1
        avg_points += graded_points[0]
        if graded_points[1] > 0:
            pass_percent += 1

    avg_points /= sum(grade_dist)
    pass_percent = (pass_percent / sum(grade_dist)) * 100

    statistics(avg_points, pass_percent, grade_dist)

main()