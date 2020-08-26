from datetime import datetime


# This program displays responses to the user's name and birth month



name = input("What is your name? ")
month = input("What month were you born in? ")

name_digits = 0

for letters in name:
    name_digits = name_digits + 1       # Increment count of letters in name

print(f"Hello {name}!")     # Uses string formatting to add variables
print(f"The number of letters in your name is {str(name_digits)}.")     # Convert int to string

current_date = datetime.today()     # Retrieve current date
current_month = current_date.strftime('%B')     # Format current month to string

if month.lower() == current_month.lower():
    print(f"Happy birth month, {name}!")
else:
    print(f"I love the weather in {month}.")