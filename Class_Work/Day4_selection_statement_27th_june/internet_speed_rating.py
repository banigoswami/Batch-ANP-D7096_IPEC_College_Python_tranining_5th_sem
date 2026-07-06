'''Internet Speed Rating
Problem Statement
An Internet Service Provider categorizes connection quality based on download speed.
• Less than 25 Mbps → Slow
• 25–99 Mbps → Good
• 100 Mbps or above → Excellent
Write a Python program to display the connection quality.
Sample Input
120
Sample Output
Excellent Connection'''
download_speed = float(input("Enter the download speed (Mbps): "))
# Validating the input
if download_speed < 0:
    exit("Enter valid values.")
    
if download_speed < 25:
    print("Slow Connection")
elif download_speed < 100:
    print("Good Connection")
else:
    print("Excellent Connection")
    