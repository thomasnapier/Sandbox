def main():
    print("Please enter your age: ")
    age = int(input())
    if age <= 0:
        print("Please enter a real number")
    elif age < 18:
        print("You are too young to vote")
    else:
        print("You are allowed to vote")
main()

