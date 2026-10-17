employees = [
    ("John", "IT", 50000),
    ("Jane", "HR", 45000),
    ("Mike", "IT", 60000),
    ("Sara", "Finance", 70000)
]

for name, department, salary in employees:
    print("Name:", name)
    print("Department:", department)
    print("Salary:", salary)
    print()

it_employees = []
for name, department, salary in employees:
    if department == "IT":
       it_employees.append((name, department, salary))

print("Employees in the IT department:")
for name, department, salary in it_employees:
    print(name, department, salary)

print("\nIT employees earning more than 55,000:")
for name, department, salary in it_employees:
    if salary > 55000:
        print(name)
