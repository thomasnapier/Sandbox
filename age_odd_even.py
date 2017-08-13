def main():
    age = 0
    valid_input = False
    while not valid_input:
        try:
            age = int(input("Age: "))
            if age < 0:
                print("Age must be greater than 0")
            else:
                valid_input = True
        except ValueError:
            print('Invalid input. Enter a number')

    if is_even(age):
        print("{} is even".format(age))
    else:
        print("{} is odd".format(age))


def is_even(number):
    if number % 2 == 0:
        return True
    else:
        return False
main()