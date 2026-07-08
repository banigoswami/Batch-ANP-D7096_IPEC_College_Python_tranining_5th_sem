'''Student Marks Management
Problem Statement:
Create a dictionary to store the marks of 5 students, where the key is the student's name and the
value is their marks.
Perform the following operations:
• Display all student names and marks.
• Add a new student with marks.
• Update the marks of an existing student.
• Delete a student by name.
• Display the student who scored the highest marks'''
marks_dict = {}
# Input marks for 5 students
for i in range(5):
    name = input(f"Enter name of student {i + 1}: ")
    marks = float(input(f"Enter marks of {name}: "))
    marks_dict[name] = marks
    print(f"Added {name} with marks {marks}.")
# Display all student names and marks
print("\nStudent Names and Marks:")
for name, marks in marks_dict.items():
    print(f"{name}: {marks}")
# Add a new student with marks
new_name = input("\nEnter name of new student: ")
new_marks = float(input(f"Enter marks of {new_name}: "))
marks_dict[new_name] = new_marks
print(f"Added {new_name} with marks {new_marks}.")
# Update the marks of an existing student
update_name = input("\nEnter name of student to update marks: ")
if update_name in marks_dict:
    updated_marks = float(input(f"Enter new marks for {update_name}: "))
    marks_dict[update_name] = updated_marks
    print(f"Updated {update_name}'s marks to {updated_marks}.")
else:
    print(f"Student {update_name} not found.")
# Delete a student by name
delete_name = input("\nEnter name of student to delete: ")
if delete_name in marks_dict:
    del marks_dict[delete_name]
    print(f"Deleted student {delete_name}.")
else:
    print(f"Student {delete_name} not found.")
# Display the student who scored the highest marks
if marks_dict:
    highest_student = max(marks_dict, key=marks_dict.get)
    highest_marks = marks_dict[highest_student]
    print(f"\nStudent with highest marks: {highest_student} with {highest_marks} marks.")
    