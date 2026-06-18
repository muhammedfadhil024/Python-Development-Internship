# 1. Simple Data Structure
employees = [
    {"name": "Rahul", "department": "IT", "salary": 45000},
    {"name": "Vikram", "department": "IT", "salary": 52000},
    {"name": "Anjali", "department": "HR", "salary": 38000},
    {"name": "Ramya", "department": "Finance", "salary": 43000},
    {"name": "Nani", "department": "Sales", "salary": 40000},
    {"name": "Amaya", "department": "Finance", "salary": 43000}
]

# 2. Logic to display all employees
print("**EMPLOYEE SALARY REGISTRY**")
for e in employees:
    print(f"Name: {e['name']} | Dept: {e['department']} | Salary: {e['salary']}")

# 3. Logic to calculate financial analytics
total_employees = len(employees)
total_payout = sum(e['salary'] for e in employees)
avg_salary = total_payout / total_employees
highest_earner = max(employees, key=lambda e: e['salary'])
lowest_earner = min(employees, key=lambda e: e['salary'])

print("\n**FINANCIAL SUMMARY**")
print(f"Total Staff Count: {total_employees}")
print(f"Total Monthly Payout: ₹{total_payout}")
print(f"Average Staff Salary: ₹{avg_salary:.2f}")

# 4.Find maximum and minimum earners using a key lambda function
print(f"Highest Salary: {highest_earner['name']}-₹{highest_earner['salary']}")
print(f"Lowest Salary: {lowest_earner['name']}-₹{lowest_earner['salary']}")

# 5. Simple filtering logic (Find HR Department payroll)
print("\n**DEPARTMENT FILTER (HR)**")
for e in employees:
    if e['department'] == "HR":
        print(f" {e['name']} - {e['salary']}")