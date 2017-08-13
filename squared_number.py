def main():
    number = int(input("Number: "))
    squared_number = calc_square(number)
    print(squared_number)

def calc_square(num):
    num = num ** 2
    return num

main()