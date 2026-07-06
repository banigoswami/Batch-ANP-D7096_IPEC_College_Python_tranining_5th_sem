'''Mobile Recharge Plan
Scenario:
A telecom company charges a fixed amount per GB of data.
Problem Statement:
Write a Python program to calculate the total recharge amount based on the data pack selected.
Input:
• Cost per GB
• Number of GBs
Output:
• Total Recharge Cost'''
cost_per_gb = float(input("Enter Cost per GB: "))
number_of_gbs = float(input("Enter Number of GBs: "))
#-------------Validating the inputs----------------
if cost_per_gb < 0 or number_of_gbs < 0:
    exit("Enter valid values.")
total_recharge_cost = cost_per_gb * number_of_gbs
print("Total Recharge Cost:", total_recharge_cost)
