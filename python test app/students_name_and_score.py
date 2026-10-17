students = [
    ("Alice", 78),
    ("Bob", 45),
    ("Charlie", 90),
    ("Diana", 62),
    ("Kent", 30)
]
print("Student Names and Scores:")
for name, score in students:
    print(name, score)


print("\nStudents who scored 60 or above:")
for name, score in students:
    if score >= 60:
        print(name)

passed = 0
for name, score in students:
    if score >= 50:
        passed += 1
print("\nNumber of students who passed:", passed)
