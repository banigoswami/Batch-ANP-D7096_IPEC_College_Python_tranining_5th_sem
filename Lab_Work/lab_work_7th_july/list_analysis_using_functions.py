''' List Analysis using Functions
Write a Python program that defines the following functions:
• find_max(numbers)
• find_min(numbers)
• find_average(numbers)
The program should:
• Accept a list of 10 integers from the user.
• Call all three functions.
• Display the maximum value, minimum value, and average of the list'''
def find_max(numbers):
    return max(numbers)

def find_min(numbers):
    return min(numbers)

def find_average(numbers):
    return sum(numbers) / len(numbers)

# Accept a list of 10 integers from the user
numbers = []
for i in range(10):
    num = int(input(f"Enter integer {i + 1}: "))
    numbers.append(num)

# Call all three functions
max_value = find_max(numbers)
min_value = find_min(numbers)
average_value = find_average(numbers)

# Display the results
print("Maximum value:", max_value)
print("Minimum value:", min_value)
print("Average:", average_value)