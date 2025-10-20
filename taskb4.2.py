# Create the list of students
students = [
    {"name": "Ahmed", "grades": [85, 90, 78]},
    {"name": "Sara", "grades": [92, 88, 95]},
    {"name": "Mahmoud", "grades": [70, 75, 80]}
]

# Calculate and print average grades
print("\nStudent average grades:")
for student in students:
    avg = sum(student["grades"]) / len(student["grades"])
    print(f"{student['name']}: {avg:.2f}")