# employee_data_processor
A Python project that reads employee records from a CSV file, cleans and validates the data, removes duplicate records, calculates salary statistics, and exports the processed data to a new CSV file.

This project demonstrates fundamental data processing and ETL (Extract, Transform, Load) concepts using Python's built-in libraries.

Features
CSV Data Extraction: Read employee records using csv.DictReader.

Data Cleaning: Remove unnecessary whitespace from employee names and standardize department names.

Data Validation: Reject records with missing, invalid, or negative salaries.

Duplicate Removal: Use a Python set to identify and remove duplicate employee IDs.

Salary Calculation: Calculate annual salaries from monthly salaries.

Data Analysis: Calculate the average monthly salary for each department.

Highest-Paid Employee: Identify the employee with the highest monthly salary.

CSV Export: Save the cleaned and processed records to a new CSV file.

Summary Report: Display the number of valid employees, departmental salary averages, and highest-paid employee.

Python 3
    csv : reading and writing file
    pathlib : managing file's path



No external Python packages are required.
