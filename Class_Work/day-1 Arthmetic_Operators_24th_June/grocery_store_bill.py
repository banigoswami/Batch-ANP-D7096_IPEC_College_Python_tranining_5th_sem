'''Grocery Store Bill
Scenario:
A customer purchases multiple packets of rice from a grocery store.
Problem Statement:
Write a Python program to calculate the total cost of rice packets purchased.
Input:
• Price per packet
• Number of packets
Output:
• Total Bill Amount'''
x = float(input("Enter Price per Packet: "))
y = int(input("Enter Number of Packets: "))
total_bill = x * y
print("Total Bill Amount:", total_bill)
