
# Define a class to store personal information of students
class Personal_Info:
    def __init__(self):
        self.name = ""
        self.age = 0
        self.address = ""
        self.student_id = ""

# Method to get input from the user for each student's information
    def get_input(self, student_number):
        print(f"\n=== Enter information for Student {student_number} ===")
        self.name = input("\nEnter your name: ")
        self.age = int(input("Enter your age: "))
        self.address = input("Enter your address: ")
        self.student_id = input("Enter your student ID: ")

# Main program to collect and display student information
total_students = int(input("How many students information do you want to enter? "))
students_list = []

# Loop to collect information for each student and store it in a list
for i in range(1, total_students + 1):
    student = Personal_Info() 
    student.get_input(i)
    students_list.append(student)

# Sort the list of students by age and display their information
    students_list.sort(key=lambda x: x.age)

# Display the sorted student information

    print("\n" + "=" * 50 )
    print(f"\n===  Student Information: {len(students_list)} ===")
    print("=" * 50)

    for x in students_list:
        print(f"Age: {x.age} | Full Name: {x.name} | Address: {x.address} | Student ID: {x.student_id}")