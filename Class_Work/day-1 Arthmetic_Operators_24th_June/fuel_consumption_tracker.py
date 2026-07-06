'''Fuel Consumption Tracker
Scenario:
A person wants to calculate the average fuel consumption of a car.
Problem Statement:
Write a Python program to find the average mileage of a car.
Input:
• Total distance traveled (km)
• Fuel consumed (liters)
Output:
• Mileage (km/l)'''
distance = float(input("Enter Total Distance Traveled (km): "))
fuel_consumed = float(input("Enter Fuel Consumed (liters): "))
#-------------Validating the inputs----------------
if distance < 0 or fuel_consumed <= 0:
    exit("Enter valid values.")

mileage = distance / fuel_consumed
print("Mileage (km/l):", mileage)