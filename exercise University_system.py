class Department:
    def __init__(self, name, head):
        self.name = name
        self.head = head

    def show_department(self):
        print(f"Department Name: {self.name}")
        print(f"Department Head: {self.head}")


class University:
    def __init__(self, name, dept_name, dept_head):
        self.name = name
        # Composition: Instantiating Department inside University
        self.department = Department(dept_name, dept_head)

    def show_university(self):
        print(f"University Name: {self.name}")
        self.department.show_department()


# Usage
u1 = University("Yoobee College", "Software Engineering", "Dr. Smith")
u1.show_university()