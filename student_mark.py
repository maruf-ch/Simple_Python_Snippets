from tabulate import tabulate

class Student:
    def __init__(self, name="unknown", roll=0, department="science", mark=0):
        self.name = name
        self.roll = roll
        self.department = department
        self.mark = mark

# Create student objects
print("\n Students mark table of Forhadabad High Schoool \n")
students = [
    Student("Maruf", 43, "arts", 80),
    Student("Istiaq", 44, "arts", 82),
    Student("Nahin", 45, "arts", 85),
    Student("Fahim", 46, "arts", 78),
    Student("Anabil", 47, "arts", 90),
    Student(),
    Student(),
    Student("Jaber", 48, "arts", 90)
]

# Prepare data for the table
table_data = []
for student in students:
    table_data.append([
        student.name.title(),
        student.roll,
        student.department.title(),
        student.mark
    ])

# Print table
print(tabulate(table_data, headers=["Name", "Roll", "Department", "Mark"], tablefmt="grid"))
