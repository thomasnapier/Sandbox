def main():
    print("Does it work? Y/N")
    user_choice = input()
    if user_choice == "y" or user_choice == "Y":
        print("Dont mess with it")
    elif user_choice == "n" or user_choice == "N":
        print("Did you mess with it? Y/N")
        user_choice = input()
    else:
        print("Please use the y or n key for yes or no")

main()