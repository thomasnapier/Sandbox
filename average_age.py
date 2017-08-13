age = 1
number_of_people = 0
previous_age = 0
while age > 0:
    print("Enter in age")
    age = int(input(">>> "))
    if age > 0:
        number_of_people = number_of_people + 1
        previous_age = previous_age + age
        age = previous_age
        average_age = age / number_of_people
        print("The average as so far is: " + str(average_age))
    else:
        print("Please use real numbers")
