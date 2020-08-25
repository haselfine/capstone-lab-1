name = input("What is your name? ")
month = input("What month were you born in? ")

name_digits = 0

for letters in name:
    name_digits = name_digits + 1

print("Hello " + name)
print("The number of letters in your name is " + str(name_digits))

if month == "August":
    print("Happy birth month!")
else:
    print("Your birth month is not August")