'''Password Strength Checker
Write a function check_password(password) that checks whether a password is strong.
A password is considered Strong if:
• It contains at least 8 characters.
• It contains at least one uppercase letter.
• It contains at least one lowercase letter.
• It contains at least one digit.
The function should return:
• "Strong Password" or
• "Weak Password"
The main program should accept a password from the user and display the result.'''
def check_password(password):
    if len(password) < 8:
        return "Weak Password"
    has_upper = any(char.isupper() for char in password)
    has_lower = any(char.islower() for char in password)
    has_digit = any(char.isdigit() for char in password)

    if has_upper and has_lower and has_digit:
        return "Strong Password"
    else:
        return "Weak Password"

# Main program
password = input("Enter a password: ")
print("Password Status:", check_password(password))