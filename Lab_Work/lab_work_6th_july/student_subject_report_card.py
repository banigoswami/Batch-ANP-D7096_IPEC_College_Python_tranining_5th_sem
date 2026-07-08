'''Student Subject Report Card
Problem Statement:
Create a nested dictionary to store marks of students in three subjects.
Example:
{
'Rahul': {'Math': 85, 'Science': 90, 'English': 88},
'Priya': {'Math': 78, 'Science': 95, 'English': 82},
'Ankit': {'Math': 91, 'Science': 89, 'English': 94}
}
Write a program to:
• Calculate the total marks of each student.
• Calculate the average marks of each student.
• Display the topper based on total marks.
• Display the subject-wise highest marks along with the student's name.
• Display students whose average is greater than or equal to 85.'''
dict = {}
# Input marks for 3 students in 3 subjects
for i in range(3):
    name = input(f"Enter name of student {i + 1}: ")
    math_marks = float(input(f"Enter Math marks for {name}: "))
    science_marks = float(input(f"Enter Science marks for {name}: "))
    english_marks = float(input(f"Enter English marks for {name}: "))
    dict[name] = {'Math': math_marks, 'Science': science_marks, 'English': english_marks}
    print(f"Added {name} with marks: Math={math_marks}, Science={science_marks}, English={english_marks}.")
Total_marks_dict = {}
# Calculate total and average marks for each student
for student, marks in dict.items():
    total_marks = sum(marks.values())
    average_marks = total_marks / len(marks)
    Total_marks_dict[student] = {'Total': total_marks, 'Average': average_marks}
    print(f"{student}: Total Marks={total_marks}, Average Marks={average_marks:.2f}")
# Display the topper based on total marks
topper = max(Total_marks_dict, key=lambda x: Total_marks_dict[x]['Total'])
print(f"\nTopper: {topper} with Total Marks={Total_marks_dict[topper]['Total']}")
# Display subject-wise highest marks along with the student's name
subject_highest = {}
for subject in ['Math', 'Science', 'English']:
    highest_student = max(dict, key=lambda x: dict[x][subject])
    subject_highest[subject] = (highest_student, dict[highest_student][subject])
    print(f"Highest in {subject}: {highest_student} with Marks={dict[highest_student][subject]}")
# Display students whose average is greater than or equal to 85
print("\nStudents with Average Marks >= 85:")
for student, marks in Total_marks_dict.items():
    if marks['Average'] >= 85:
        print(f"{student}: Average Marks={marks['Average']:.2f}")
        