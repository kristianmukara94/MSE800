# College Enrollment System - OOP implementation of the W5-A1 activity diagram
# and class diagram (Student, Course, Teacher).

# Represents a single subject that belongs to a course
class Subject:
    def __init__(self, subject_id, subject_name):
        self.subject_id = subject_id
        self.subject_name = subject_name


# Student class - matches the Student box in the class diagram
class Student:
    def __init__(self, student_id, student_name, student_email):
        self.student_id = student_id
        self.student_name = student_name
        self.student_email = student_email
        self.enrolled_courses = []
        self.subjects = []
        self.grades = {}

# Show the available courses so the student can choose one to enroll in
    def view_courses_and_add_subjects(self, course_list):
        print("\n=== Available Courses ===")
        for course in course_list:
            status = "OPEN" if course.check_enrolled_course_capacity() else "FULL"
            print(f"{course.course_id} - {course.course_name} "
                  f"({len(course.enrolled_students)}/{course.capacity}) [{status}]")
        return course_list

# Add the chosen course to enroll, checking the course capacity first
    def select_course_to_enroll(self, course_id, course_list):
        for course in course_list:
            if course.course_id == course_id:
                if course in self.enrolled_courses:
                    print("You are already enrolled in this course.")
                    return
                if course.check_enrolled_course_capacity():
                    course.enrolled_students.append(self)
                    self.enrolled_courses.append(course)
                    self.add_subjects(course.subjects)
                    print(f"Enrollment complete for {course.course_name}.")
                else:
                    course.display_error()
                return
        print("Course ID not found.")

# Add the subjects that come with an enrolled course to the student's record
    def add_subjects(self, subjects_to_add):
        for subject in subjects_to_add:
            if subject not in self.subjects:
                self.subjects.append(subject)

# Show every course and subject the student is currently enrolled in
    def view_enrollment_confirmation(self):
        print(f"\n=== Enrolled Subjects for {self.student_name} ===")
        if not self.enrolled_courses:
            print("No courses enrolled yet.")
            return
        for course in self.enrolled_courses:
            grade = self.grades.get(course.course_name, "Not graded yet")
            subject_names = ", ".join(s.subject_name for s in course.subjects) or "None"
            print(f"{course.course_name} | Subjects: {subject_names} | Grade: {grade}")


# Course class - matches the Course box in the class diagram
class Course:
    def __init__(self, course_id, course_name, capacity, member_name=""):
        self.course_id = course_id
        self.course_name = course_name
        self.capacity = capacity
        self.enrolled_students = []
        self.subjects = []
        self.member_name = member_name

# Return True if there is still room to enroll another student
    def check_enrolled_course_capacity(self):
        return len(self.enrolled_students) < self.capacity

# Return the list of students currently enrolled in this course
    def display_enrolled_students(self):
        return self.enrolled_students

# Display the enrollment error when a course is full
    def display_error(self):
        print(f"Error: {self.course_name} is at full capacity. No available subject.")


# Teacher class - matches the Teacher box in the class diagram
class Teacher:
    def __init__(self, teacher_id, teacher_name, teacher_dept):
        self.teacher_id = teacher_id
        self.teacher_name = teacher_name
        self.teacher_dept = teacher_dept
        self.assigned_courses = []

# Check whether the given course still has capacity for enrollment
    def check_enrolled_capacity(self, course):
        return course.check_enrolled_course_capacity()

# Show the course details, its subjects, and the enrolled students
    def view_courses_details_and_subjects(self, course):
        print(f"\n=== {course.course_name} ({course.course_id}) ===")
        subject_names = ", ".join(s.subject_name for s in course.subjects) or "None"
        print(f"Subjects: {subject_names}")
        students = course.display_enrolled_students()
        if not students:
            print("No students enrolled yet.")
            return
        for student in students:
            print(f"{student.student_id} - {student.student_name}")

# Add or update the grade for a specific student in a specific course
    def add_grades_to_the_specific_student(self, student, course, grade):
        if student not in course.enrolled_students:
            print("This student is not enrolled in that course.")
            return
        student.grades[course.course_name] = grade
        print(f"Grade '{grade}' saved for {student.student_name} in {course.course_name}.")


# Set up a few courses, subjects and a teacher so the demo has data to use
def seed_data():
    math101 = Course("C101", "Math 101", capacity=2, member_name="Algebra Stream")
    math101.subjects = [Subject("S1", "Algebra"), Subject("S2", "Statistics")]

    cs101 = Course("C102", "Intro to Programming", capacity=2, member_name="Software Stream")
    cs101.subjects = [Subject("S3", "Python Basics")]

    teacher = Teacher("T01", "Dr. Smith", "Computer Science")
    teacher.assigned_courses = [math101, cs101]

    return [math101, cs101], teacher


# Create a Student or Teacher account and store the login credentials
def create_account(students, teachers, accounts):
    print("\n=== Create Account ===")
    role = input("Register as (Student/Teacher): ").strip().lower()

    if role == "student":
        student_id = input("Enter Student ID: ").strip()
        student_name = input("Enter Full Name: ").strip()
        student_email = input("Enter Email: ").strip()
        password = input("Create a Password: ").strip()

        students[student_id] = Student(student_id, student_name, student_email)
        accounts[student_id] = {"password": password, "role": "student"}
        print(f"Student account created for {student_name}.")
        return "student", student_id

    elif role == "teacher":
        teacher_id = input("Enter Teacher ID: ").strip()
        teacher_name = input("Enter Full Name: ").strip()
        teacher_dept = input("Enter Department: ").strip()
        password = input("Create a Password: ").strip()

        teachers[teacher_id] = Teacher(teacher_id, teacher_name, teacher_dept)
        accounts[teacher_id] = {"password": password, "role": "teacher"}
        print(f"Teacher account created for {teacher_name}.")
        return "teacher", teacher_id

    else:
        print("Invalid role. Please choose Student or Teacher.")
        return None, None


# Log in with an existing account and return its role and ID
def login(accounts):
    print("\n=== Login ===")
    user_id = input("Enter your ID: ").strip()
    password = input("Enter your Password: ").strip()

    account = accounts.get(user_id)
    if account and account["password"] == password:
        print(f"Login successful. Welcome back, {user_id}!")
        return account["role"], user_id

    print("Invalid ID or password.")
    return None, None


# Run the Student workflow: view courses, enroll, view enrollment confirmation
def student_workflow(student, courses):
    while True:
        print(f"\n=== Student Menu ({student.student_name}) ===")
        print("1. View Available Courses")
        print("2. Add Course to Enroll")
        print("3. View Enrolled Subjects")
        print("4. Logout")
        choice = input("Choose an option: ").strip()

        if choice == "1":
            student.view_courses_and_add_subjects(courses)
        elif choice == "2":
            course_id = input("Enter the Course ID to enroll: ").strip()
            student.select_course_to_enroll(course_id, courses)
        elif choice == "3":
            student.view_enrollment_confirmation()
        elif choice == "4":
            print("Logging out...")
            break
        else:
            print("Invalid option, please try again.")


# Run the Teacher workflow: view assigned course, view students, add/update grades
def teacher_workflow(teacher):
    while True:
        print(f"\n=== Teacher Menu ({teacher.teacher_name}) ===")
        print("1. View Assigned Course")
        print("2. Select Course and View Students")
        print("3. Add/Update Grades")
        print("4. Logout")
        choice = input("Choose an option: ").strip()

        if choice == "1":
            for course in teacher.assigned_courses:
                print(f"{course.course_id} - {course.course_name}")
        elif choice == "2":
            course_id = input("Enter the Course ID to select: ").strip()
            course = next((c for c in teacher.assigned_courses if c.course_id == course_id), None)
            if course:
                teacher.view_courses_details_and_subjects(course)
            else:
                print("Course not found among your assigned courses.")
        elif choice == "3":
            course_id = input("Enter the Course ID: ").strip()
            course = next((c for c in teacher.assigned_courses if c.course_id == course_id), None)
            if not course:
                print("Course not found among your assigned courses.")
                continue
            student_id = input("Enter the Student ID: ").strip()
            student = next((s for s in course.enrolled_students if s.student_id == student_id), None)
            if not student:
                print("Student not found in that course.")
                continue
            grade = input("Enter the Grade: ").strip()
            teacher.add_grades_to_the_specific_student(student, course, grade)
            print("Changes saved.")
        elif choice == "4":
            print("Logging out...")
            break
        else:
            print("Invalid option, please try again.")


# Main driver: follows START -> Create Account -> Student/Teacher -> Login ->
# role workflow -> LOGOUT -> END from the activity diagram
def main():
    courses, seed_teacher = seed_data()
    students = {}
    teachers = {seed_teacher.teacher_id: seed_teacher}
    accounts = {seed_teacher.teacher_id: {"password": "teach123", "role": "teacher"}}

    print("=== START ===")
    print(f"(Demo teacher account -> ID: {seed_teacher.teacher_id}, Password: teach123)")

    while True:
        create_account(students, teachers, accounts)

        role, user_id = login(accounts)
        if role == "student":
            student_workflow(students[user_id], courses)
        elif role == "teacher":
            teacher_workflow(teachers[user_id])

        again = input("\nRun another session? (y/n): ").strip().lower()
        if again != "y":
            break

    print("=== END ===")


if __name__ == "__main__":
    main()
