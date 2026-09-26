# Student Result Management Program
# Asks for the names and marks of 5 students, works out each student's
# average, shows Pass/Fail, then shows the class average and the top student.

PASS_MARK = 50
NUMBER_OF_STUDENTS = 5
NUMBER_OF_SUBJECTS = 3

# Dictionary to store each student's name and their list of marks
students = {}

# Step 1: Get the names and marks from the user
for i in range(1, NUMBER_OF_STUDENTS + 1):
    print(f"\nStudent {i}")
    name = input("Enter student name: ")

    marks = []
    for j in range(1, NUMBER_OF_SUBJECTS + 1):
        mark = float(input(f"Enter mark for subject {j}: "))
        marks.append(mark)

    students[name] = marks

# Step 2: Calculate each student's average and show Pass/Fail
print("\n----- Student Results -----")

averages = {}
for name, marks in students.items():
    average = sum(marks) / len(marks)
    averages[name] = average

    if average >= PASS_MARK:
        result = "Passed"
    else:
        result = "Failed"

    print(f"{name}: Average = {average:.2f} -> {result}")

# Step 3: Calculate the class average
class_average = sum(averages.values()) / len(averages)
print(f"\nClass Average: {class_average:.2f}")

# Step 4: Find the student with the highest average mark
top_student = max(averages, key=averages.get)
print(f"Top Student: {top_student} with an average of {averages[top_student]:.2f}")
