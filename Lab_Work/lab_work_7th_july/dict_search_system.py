'''Dictionary Search System
Write a Python program that defines a function search_student(student_dict, roll_no).
The function should:
• Accept a dictionary where:
o Key = Roll Number
o Value = Student Name
• Search for the given roll number.
• Return the student name if found; otherwise return "Student Not Found".
The main program should:
• Create a dictionary of at least 5 students.
• Accept a roll number from the user.
• Display the search result'''
def search_student(student_dict, roll_no):
    return student_dict.get(roll_no, "Student Not Found")

# Create a dictionary of at least 5 students
students = {
    "001": "Alice",
    "002": "Bob",
    "003": "Charlie",
    "004": "David",
    "005": "Eve"
}

# Accept a roll number from the user
roll_number = input("Enter the roll number to search: ")

# Display the search result
print("Student Name:", search_student(students, roll_number))               