from functools import wraps

is_logged_in = False


def login_required(func):
    def wrapper():
        if is_logged_in:
            func()
        else:
            print("Access is denied:")
            

    return wrapper

@login_required
def view_salary():
    print("Salary: Php100,000")

@login_required
def view_personal_details():
    print("Personal Details: Juan Delacruz")

@login_required
def download_report():
    print("Reports for: Juan Delacruz\n\n", "Salary is: Php 100,000\n\n")

print()
view_salary()
view_personal_details
download_report()
