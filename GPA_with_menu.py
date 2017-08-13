def main():
    choice = 0
    grade = 0
    user_name = input("Enter name: ")
    print("Hello {}. Choose: ".format(user_name))
    choice = get_menu_choice()
    while choice != "Q":
        if choice == "D":
            grade = calculate_grade(choice, grade)
            print("You got a {}".format(grade))
        elif choice == "C":
            calculate_GPA()
        else:
            print("Invalid choice")
        choice = get_menu_choice()
def get_menu_choice():
    print("""(D)etermine Grade
(C)alculate GPA
(Q)uit""")
    choice = input(">>> ").upper()
    return choice

def calculate_grade(choice, grade):
    grade = 0
    valid_input = False
    while not valid_input:
        try:
            score = int(input("What is your score? "))
            if score < 0 or score > 100:
                print("Enter in a real grade")
                score = int(input("What is your score? "))
            if score >= 85:
                grade = "HD"
                valid_input = True
            elif 85 > score >= 75:
                grade = "D"
                valid_input = True
            elif 75 > score >= 65:
                grade = "C"
                valid_input = True
            elif 65 > score >= 50:
                grade = "P"
                valid_input = True
            else:
                grade = "N"
                valid_input = True
        except ValueError:
            print("Enter a real number")
    return grade

main()