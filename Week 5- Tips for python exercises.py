# Quick practice set of list/dict comprehension exercises

# 1. extract information with age greater than 25 from the following list of dictionaries
data = [{"name": "Alice", "age": 28}, {"name": "Bob", "age": 24}, {"name": "Charlie", "age": 30}]
over_25 = [person for person in data if person["age"] > 25]
print("2. Age greater than 25:", over_25)

# 2. use list comprehension to flatten the matrix
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flattened = [num for row in matrix for num in row]
print("1. Flattened matrix:", flattened)

# 3. use enumerate() for looping to add 5 extra point to each grade in the list, the 5th one add 10
grades = [88, 92, 78, 65, 50, 94]
updated_grades = [g + 10 if i == 4 else g + 5 for i, g in enumerate(grades)]
print("3. Updated grades:", updated_grades)

# 4. filter out elements depend on their index: 
#    use list comprehension and enumerate() to get elements with even index 
data2 = [100, 200, 300, 400, 500]
even_index_elements = [value for i, value in enumerate(data2) if i % 2 == 0]
print("4. Elements at even index:", even_index_elements)

# 5. create a dictionary from lists using zip()
keys = ['name', 'age', 'grade']
values = ['Alice', 25, 'A']
person_dict = dict(zip(keys, values))
print("5. Dictionary from zip():", person_dict)

# 6. sort the dictionary based on the ages using lambda
students = [
    {'name': "John", 'grade': "A", 'age': 20},
    {'name': "Jane", 'grade': "B", 'age': 21},
    {'name': "Joss", 'grade': "A+", 'age': 19},
    {'name': "Jack", 'grade': "A-", 'age': 16},
    {'name': "Dave", 'grade': "C", 'age': 25},
]
sorted_students = sorted(students, key=lambda student: student['age'])
print("6. Students sorted by age:", sorted_students)

# 7. Sort by age, then by salary if ages are the same
     # use lambda
employees = [
    {'name': 'Alice', 'age': 30, 'salary': 80000},
    {'name': 'Bob', 'age': 25, 'salary': 50000},
    {'name': 'Charlie', 'age': 35, 'salary': 120000},
]
sorted_employees = sorted(employees, key=lambda emp: (emp['age'], emp['salary']))
print("7. Employees sorted by age then salary:", sorted_employees)
