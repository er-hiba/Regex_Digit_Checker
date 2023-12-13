import re

def digit_check(string):
    # Using a regular expression to check for the presence of digits
    return bool(re.search(r'\d', string))

# Take input from the user
text = input("Enter a string: ")

# Check if the entered string contains digits
result = digit_check(text)

if result:
    print("The entered string contains digits.")
else:
    print("The entered string does not contain any digits.")

