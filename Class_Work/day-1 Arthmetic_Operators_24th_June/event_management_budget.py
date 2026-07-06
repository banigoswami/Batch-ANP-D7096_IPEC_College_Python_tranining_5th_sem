'''Event Management Budget
Scenario:
An event manager wants to calculate the cost contribution per participant.
Problem Statement:
Write a Python program to calculate how much each participant should pay.
Input:
• Total Event Cost
• Number of Participants
Output:
• Amount per Participant'''
total_event_cost = float(input("Enter Total Event Cost: "))
number_of_participants = int(input("Enter Number of Participants: "))
#-------------Validating the inputs----------------
if total_event_cost < 0 or number_of_participants <= 0:
    exit("Enter valid values.")
amount_per_participant = total_event_cost / number_of_participants
print("Amount per Participant:", amount_per_participant)
