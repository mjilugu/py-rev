#!/usr/local/bin/python3

print('Welcome to the GPA calculator')
print('Please enter all your letter grades, one per line.')
print('Enter a blank line to designate the end.')

# map from letter grade to point value
def compute_gpa(grades, points = {
                        'A+': 4.0, 'A': 4.0, 'A-':3.67, 'B+':3.33, 'B': 3.0, 'B-': 2.67,
                        'C+': 2.33, 'C': 2.0, 'C': 1.67, 'D+': 1.33, 'D': 1.0, 'F': 0.0
                    }):
    num_courses = 0
    total_points = 0
    for g in grades:
        if g in points:
            num_courses += 1
            total_points += points[g]
        elif g not in points:
            print(f"Unknown grade {g} being ignored")
    if num_courses > 0:
        return total_points / num_courses

# MAIN

grades = []
done = False
while not done:
    grade = input()
    if grade == '':
        done = True

    else:
        grades.append(grade)

if len(grades) > 0:
    print(f"Your GPA is {compute_gpa(grades)}")
