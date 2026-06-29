'''
---------------------------------------------------Employee Performance Evaluation---------------------------------------------
Problem Statement 
An employee is evaluated using: 
• Project Score  
• Attendance Percentage  
• Client Feedback Score  
Rules: 
• Excellent → All scores above 90  
• Good → Scores above 75  
• Average → Scores above 60  
• Poor → Otherwise  
Additional Rule: 
• Attendance below 70% cannot receive more than Average rating.  
---------------------------------------------------------------
Sample Input 
Project Score: 95 
Attendance: 65 
Client Feedback: 92 
---------------------------------------------------------------
Sample Output 
Performance Rating: Average 
Reason: Attendance below 70% 
---------------------------------------------------------------
--------------------------------Coding--------------------------------
'''
project_score = int(input("Project Score: "))
attendance = float(input("Attendance: "))
client_feedback = int(input("Client Feedback: "))  
#-------------Validating the inputs----------------
if project_score < 0 or project_score > 100 or attendance < 0 or attendance > 100 or client_feedback < 0 or client_feedback > 100:
    exit("Enter valid scores between 0 and 100.")
#--------------------------------------------------
# Check attendance constraint first
if attendance < 70:
    if project_score > 60 and client_feedback > 60:
        print("---------------------------------------------------------------")
        print("Performance Rating: Average")
        print("Reason: Attendance below 70%")
        print("---------------------------------------------------------------")
    else:
        print("---------------------------------------------------------------")
        print("Performance Rating: Poor")
        print("Reason: Attendance below 70%")
        print("---------------------------------------------------------------")
else:
    # Apply normal rating rules if attendance >= 70%
    if project_score > 90 and client_feedback > 90:
        print("---------------------------------------------------------------")
        print("Performance Rating: Excellent")
        print("Reason: All scores above 90")
        print("---------------------------------------------------------------")
    elif project_score > 75 and client_feedback > 75:
        print("---------------------------------------------------------------")
        print("Performance Rating: Good")
        print("Reason: All scores above 75")
        print("---------------------------------------------------------------")
    elif project_score > 60 and client_feedback > 60:
        print("---------------------------------------------------------------")
        print("Performance Rating: Average")
        print("Reason: All scores above 60")
        print("---------------------------------------------------------------")
    else: 
        print("---------------------------------------------------------------")
        print("Performance Rating: Poor")
        print("Reason: One or more scores below 60")
        print("---------------------------------------------------------------")
#-----------------------------------------------------------------------------------------------------------------