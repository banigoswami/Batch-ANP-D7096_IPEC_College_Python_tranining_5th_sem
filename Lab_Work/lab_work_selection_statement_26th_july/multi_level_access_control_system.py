'''Multi-Level Access Control System
Problem Statement
Assign access levels based on:
Roles:
• Admin
• Manager
• Employee
• Guest
Conditions:
• Admin + Security Clearance ≥ 5 → Full Access
• Manager + Experience > 5 Years → Department Access
• Employee + Experience > 2 Years → Limited Access
• Guest → Read-Only Access
• Inactive Account → No Access
Sample Input
Role: Admin
Security Clearance: 6
Account Status: Active
Sample Output
Access Level: FULL ACCESS'''
role = input("Enter your role (Admin/Manager/Employee/Guest): ").strip().lower()
# Validate role input
if role not in ["admin", "manager", "employee", "guest"]:
    exit("Invalid role. Please enter a valid role.")

# Validate other inputs (assuming they are provided)
security_clearance = int(input("Enter your security clearance (0-10): "))
experience_years = int(input("Enter your experience (in years): "))
account_status = input("Enter your account status (Active/Inactive): ").strip().lower()

# Validate security clearance
if security_clearance < 0 or security_clearance > 10:
    exit("Invalid security clearance. Please enter a value between 0 and 10.")

# Validate account status
if account_status not in ["active", "inactive"]:
    exit("Invalid account status. Please enter 'Active' or 'Inactive'.")

# Assign access level based on conditions
if role == "admin" and security_clearance >= 5:
    access_level = "FULL ACCESS"
elif role == "manager" and experience_years > 5:
    access_level = "DEPARTMENT ACCESS"
elif role == "employee" and experience_years > 2:
    access_level = "LIMITED ACCESS"
elif role == "guest":
    access_level = "READ-ONLY ACCESS"
elif account_status == "inactive":
    access_level = "NO ACCESS"
else:
    access_level = "NO ACCESS"

print(f"Access Level: {access_level}")