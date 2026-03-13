import os
import csv

filename = os.path.join(os.path.dirname(__file__), "Employee_data.csv")
salaries = []

if os.path.exists(filename):
    with open(filename, newline='', encoding='utf-8') as csvfile:
        reader = csv.reader(csvfile)
        try:
            headers = next(reader)  # Skip the header row
        except StopIteration:
            print("CSV file is empty.")
            headers = []

        if headers:
            try:
                salary_index = headers.index("Annual_Salary")
            except ValueError:
                print("Header 'Annual_Salary' not found in CSV headers:", headers)
                salary_index = None

            print(headers)
            for row in reader:
                print(row)
                if salary_index is not None and len(row) > salary_index:
                    try:
                        salaries.append(float(row[salary_index]))
                    except ValueError:
                        print("Skipping non-numeric salary:", row[salary_index])
        
    print(salaries)
    if salaries:
        average_salary = sum(salaries) / len(salaries)
        print(f"Average Salary: ${average_salary:.2f}")
        max_salary = max(salaries)
        print(f"Maximum Salary: ${max_salary:.2f}")
        min_salary = min(salaries)
        print(f"Minimum Salary: ${min_salary:.2f}")
    else:
        print("No salary data found.")

else:
    print(f"Error: The file '{filename}' does not exist.")