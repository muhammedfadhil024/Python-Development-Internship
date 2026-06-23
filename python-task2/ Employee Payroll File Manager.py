import os

FILE = "employees.txt"


def add_employee(name, salary):
    with open(FILE, "a") as f:
        f.write(f"{name},{salary}\n")
    print(f"Saved: {name} - Rs.{salary}")


def show_employees():
    if not os.path.exists(FILE):
        print("No records yet.")
        return
    with open(FILE, "r") as f:
        lines = f.readlines()
    if not lines:
        print("No records yet.")
        return
    print("\n--- Employee Records ---")
    total = 0
    for line in lines:
        name, salary = line.strip().split(",")
        salary = int(salary)
        total += salary
        print(f"{name}: Rs.{salary}")
    print(f"Total Payroll: Rs.{total}")
    print(f"Average Salary: Rs.{total // len(lines)}")


def save_report():
    if not os.path.exists(FILE):
        print("No records to report.")
        return
    with open(FILE, "r") as f:
        lines = f.readlines()
    with open("report.txt", "w") as f:
        f.write("PAYROLL REPORT\n")
        f.write("=" * 25 + "\n")
        for line in lines:
            f.write(line)
    print("Report saved to report.txt")


while True:
    print("\n== Employee Payroll File Manager ==")
    print("1. Add employee")
    print("2. Show all employees")
    print("3. Save report to file")
    print("4. Quit")

    choice = input("Choose: ").strip()

    if choice == "1":
        name = input("Name: ").strip()
        salary = int(input("Salary: "))
        add_employee(name, salary)
    elif choice == "2":
        show_employees()
    elif choice == "3":
        save_report()
    elif choice == "4":
        print("Goodbye!")
        break
    else:
        print("Invalid choice.")