'''Employee Information System
Problem Statement:
Create a dictionary where:
• Employee ID is the key.
• Value is another dictionary containing:
o Name
o Department
o Salary
Perform the following operations:
• Display all employee details.
• Search for an employee using Employee ID.
• Increase the salary of all employees by 10%.
• Display employees belonging to a specific department entered by the user'''
dict = {}
# Input employee details for 5 employees
for i in range(5):
    emp_id = input(f"Enter Employee ID for employee {i + 1}: ")
    name = input(f"Enter Name for employee {emp_id}: ")
    department = input(f"Enter Department for employee {emp_id}: ")
    salary = float(input(f"Enter Salary for employee {emp_id}: "))
    dict[emp_id] = {"Name": name, "Department": department, "Salary": salary}
    print(f"Added employee {emp_id} with details: Name={name}, Department={department}, Salary={salary}.")
    employee_id = input("\nEnter Employee ID to search: ")
# Search for an employee using Employee ID
if employee_id in dict:
    employee_details = dict[employee_id]
    print(f"Employee ID: {employee_id}, Name: {employee_details['Name']}, Department: {employee_details['Department']}, Salary: {employee_details['Salary']}")
elif employee_id not in dict:
    print(f"Employee with ID {employee_id} not found.")
# Increase the salary of all employees by 10%
for emp_id in dict:
    dict[emp_id]["Salary"] *= 1.10
    print(f"Updated salary for employee {emp_id}: {dict[emp_id]['Salary']}")
# Display employees belonging to a specific department entered by the user
department_to_search = input("\nEnter Department to search for employees: ")
print(f"\nEmployees in department '{department_to_search}':")
for emp_id, details in dict.items():
    if details["Department"] == department_to_search:
        print(f"Employee ID: {emp_id}, Name: {details['Name']}, Salary: {details['Salary']}")
        