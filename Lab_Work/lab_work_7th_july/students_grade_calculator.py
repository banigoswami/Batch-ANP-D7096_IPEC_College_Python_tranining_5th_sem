'''Student Grade Calculator
Write a Python program that defines a function calculate_grade(marks).
The function should:
• Accept marks (0–100) as a parameter.
• Return the grade according to the following criteria:
o 90 and above → A+
o 75–89 → A
o 60–74 → B
o 40–59 → C
o Below 40 → Fail
The main program should:
• Accept marks of 5 students.
• Call the function for each student.
• Display the marks and corresponding grade'''
def calculate_grade(marks):
    if marks >= 90:
        return "A+"
    elif marks >= 75:
        return "A"
    elif marks >= 60:
        return "B"
    elif marks >= 40:
        return "C"
    else:
        return "Fail"
marks_list = []
# Accept marks of 5 students
for i in range(5):
    marks = float(input(f"Enter marks of student {i + 1}: "))
    marks_list.append(marks)

# Display the marks and corresponding grade
for i, marks in enumerate(marks_list, start=1):
    grade = calculate_grade(marks)
    print(f"Student {i}: Marks = {marks}, Grade = {grade}")
    