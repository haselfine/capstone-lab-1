# This program creates a list of the user's classes

class_list = []

class_number = int(input("How many classes are you taking? "))

for x in range(class_number):
    class_name = input("What is the name of class #" + str(x+1) + "? ")
    class_list.append(class_name)

print("Your classes are the following: ")
for course in class_list:
    print("\t" + course)