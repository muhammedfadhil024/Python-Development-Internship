# Employee Salary Tracker

A simple Python script that stores employee records in memory and prints a salary register, a financial summary, and a department-wise filter.

## Overview

The script works with a hardcoded list of employee dictionaries (name, department, salary) and performs four tasks:

1. Prints a full register of all employees.
2. Calculates and prints financial analytics — total staff count, total monthly payout, and average salary.
3. Finds and prints the highest and lowest paid employees.
4. Filters and prints all employees belonging to the HR department.

## Requirements

- Python 3.x
- No external libraries — uses only built-in functions (`sum`, `max`, `min`, `len`)

## Usage

Run the script from the command line:

```bash
python "Employee Salary Tracker.py"
```

## Data Structure

Each employee is represented as a dictionary with three fields:

```python
{"name": "Rahul", "department": "IT", "salary": 45000}
```

The `employees` list currently holds 6 sample records across the IT, HR, Finance, and Sales departments.

## Sample Output

**EMPLOYEE SALARY REGISTRY**
Name: Rahul | Dept: IT | Salary: 45000
Name: Vikram | Dept: IT | Salary: 52000
Name: Anjali | Dept: HR | Salary: 38000
Name: Ramya | Dept: Finance | Salary: 43000
Name: Nani | Dept: Sales | Salary: 40000
Name: Amaya | Dept: Finance | Salary: 43000

**FINANCIAL SUMMARY**
Total Staff Count: 6
Total Monthly Payout: ₹261000
Average Staff Salary: ₹43500.00
Highest Salary: Vikram-₹52000
Lowest Salary: Anjali-₹38000

**DEPARTMENT FILTER (HR)**
| Anjali - 38000
```

## Code Structure

| Section | Purpose |
|---|---|
| Data Structure | Defines the `employees` list of dictionaries |
| Display Logic | Loops through and prints every employee record |
| Financial Analytics | Computes total count, total payout, and average salary |
| Max/Min Earners | Uses `max()`/`min()` with a `key=lambda` to find highest and lowest paid employees |
| Department Filter | Loops through employees and prints only those in a given department (HR) |

## Known Issues

- **Hardcoded data**: employee records and the department filter ("HR") are fixed in the code. For real use, consider loading data from a CSV/database and accepting the department as a function argument or user input.

## Possible Extensions

- Turn the filter into a reusable function: `filter_by_department(employees, dept)`.
- Add sorting (e.g., by salary, descending).
- Export the register/summary to a CSV or JSON file.
- Add input validation if data comes from an external source.