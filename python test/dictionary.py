
students = {
    "nifla": 85,
    "juanaidha": 90,
    "kavya": 88,
    "Athira": 75
}

name = input("Enter student name: ")


if name in students:
    print("Marks:", students[name])
else:
    print("Student not found")