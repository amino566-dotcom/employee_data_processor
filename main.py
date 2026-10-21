from pathlib import Path
import csv

INPUT_FILE = Path("employees.csv")
OUTPUT_FILE = Path("processed_employees.csv")

sample_employees = [
    {"id": "1", "name": "Ali", "department": "IT", "salary": "5000"},
    {"id": "2", "name": "Sara", "department": "HR", "salary": "6000"},
    {"id": "3", "name": "Youssef", "department": "IT", "salary": "7000"},
    {"id": "4", "name": "Mariam", "department": "Sales", "salary": "4500"},
    {"id": "5", "name": "Amine", "department": "IT", "salary": "8000"},
    {"id": "6", "name": "Karim", "department": "HR", "salary": "invalid"},
    {"id": "7", "name": "Nadia", "department": "Sales", "salary": ""},
    {"id": "3", "name": "Youssef", "department": "IT", "salary": "7000"},
    {"id": "8", "name": "  Salma  ", "department": " it ", "salary": "6500"},
    {"id": "9", "name": "Omar", "department": "HR", "salary": "-500"}
]


def create_input_file():

    if INPUT_FILE.exists():
        return

    fieldnames = ["id", "name", "department", "salary"]

    with INPUT_FILE.open("w", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(sample_employees)


def load_data(file_path):
    employees = []

    with file_path.open("r", newline="", encoding="utf-8") as file:
        reader = csv.DictReader(file)

        for row in reader:
            employees.append(row)

    return employees


def clean_data(employees):

    for employee in employees:
        employee["id"] = employee["id"].strip()
        employee["name"] = employee["name"].strip()
        employee["department"] = (
            employee["department"].strip().upper()
        )

    return employees


def validate_salary(employees):
    valid_employees = []

    for employee in employees:
        salary_text = employee["salary"].strip()

        if not salary_text:
            continue

        try:
            salary = float(salary_text)
        except ValueError:
            continue

        if salary < 0:
            continue

        employee["salary"] = salary
        valid_employees.append(employee)

    return valid_employees


def remove_duplication(employees):
    seen_ids = set()
    unique_employees = []

    for employee in employees:
        employee_id = employee["id"]

        if employee_id in seen_ids:
            continue

        seen_ids.add(employee_id)
        unique_employees.append(employee)

    return unique_employees


def add_annual_salary(employees):
    for employee in employees:
        employee["annual_salary"] = employee["salary"] * 12

    return employees


def calculate_statistics(employees):
    if not employees:
        return {}, None

    department_totals = {}
    department_counts = {}

    highest_paid_employee = employees[0]

    for employee in employees:
        department = employee["department"]
        salary = employee["salary"]

        if department not in department_totals:
            department_totals[department] = 0
            department_counts[department] = 0

        department_totals[department] += salary
        department_counts[department] += 1

        if salary > highest_paid_employee["salary"]:
            highest_paid_employee = employee

    department_averages = {}

    for department in department_totals:
        average = (
            department_totals[department]
            / department_counts[department]
        )

        department_averages[department] = average

    return department_averages, highest_paid_employee


def save_data(employees, file_path):
    if not employees:
        print("No valid employee records to export.")
        return

    fieldnames = [
        "id",
        "name",
        "department",
        "salary",
        "annual_salary"
    ]

    with file_path.open("w", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)

        writer.writeheader()
        writer.writerows(employees)


def print_report(employees, department_averages, highest_paid_employee):

    print(f"Number of valid employees: {len(employees)}")

    print("\n--- Average Monthly Salary by Department ---")

    for department, average in department_averages.items():
        print(f"{department}: {average:.2f}")

    print("\n--- Highest-Paid Employee ---")

    if highest_paid_employee is not None:
        print(f"Name: {highest_paid_employee['name']}")
        print(f"Department: {highest_paid_employee['department']}")
        print(f"Monthly salary: {highest_paid_employee['salary']:.2f}")
        print(f"Annual salary: {highest_paid_employee['annual_salary']:.2f}")
    else:
        print("No valid employees found.")




def main():
    create_input_file()
    employees = load_data(INPUT_FILE)
    employees = clean_data(employees)
    employees = remove_duplication(employees)
    employees = validate_salary(employees)
    employees = add_annual_salary(employees)

    department_averages, highest_paid_employee = (
        calculate_statistics(employees)
    )

    save_data(employees, OUTPUT_FILE)

    print_report(
        employees,
        department_averages,
        highest_paid_employee
    )

    print(f"\ncleaned data saved to: {OUTPUT_FILE.resolve()}")


if __name__ == "__main__":
    main()

