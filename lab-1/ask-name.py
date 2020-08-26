from datetime import datetime

#This program 

name = input("What is your name? ")
month = input("What month were you born in? ")

name_digits = 0

for letters in name:
    name_digits = name_digits + 1

print(f"Hello {name}!")
print(f"The number of letters in your name is {str(name_digits)}.")

current_date = datetime.today()
current_month = current_date.strftime('%B')

if month.lower() == current_month.lower():
    print(f"Happy birth month, {name}!")
else:
    print(f"I love the weather in {month}")