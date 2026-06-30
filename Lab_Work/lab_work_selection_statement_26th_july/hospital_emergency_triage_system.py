'''Hospital Emergency Triage System
Problem Statement
A hospital prioritizes patients based on:
• Critical Condition
• Age
• Oxygen Level
Rules:
• Critical condition → Immediate Treatment
• Oxygen below 90 → High Priority
• Age above 65 → Medium Priority
• Others → Normal Priority
Sample Input
Critical Condition (Y/N): N
Age: 70
Oxygen Level: 94
Sample Output
Patient Priority: Medium Priority
Reason: Senior Citizen'''
critical_condition = input("Critical Condition (Y/N): ").strip().upper()
age = int(input("Age: "))
oxygen_level = int(input("Oxygen Level: "))
# Validate inputs
if critical_condition not in ['Y', 'N']:
    exit("Invalid input for critical condition. Please enter 'Y' or 'N'.")
if age < 0:
    exit("Invalid age. Please enter a non-negative value.")
if oxygen_level < 0 or oxygen_level > 100:
    exit("Invalid oxygen level. Please enter a value between 0 and 100.")   
    