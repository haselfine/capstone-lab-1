class_list = []

class_number = int(input("How many classes are you taking?"))

for x in range(class_number):
    class_name = input("What is the name of class #" + str(x) + "?")
    class_list.append(class_name)

for course in class_list:
    print(course)