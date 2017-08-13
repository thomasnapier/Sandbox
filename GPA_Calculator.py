IN_FILE = 'grades.txt'
grade = 0
total_grade = 0
grade_count = 0

in_file = open(IN_FILE, 'r')
for line in in_file:
    score = int(line)
    grade_count += 1
    if score >= 85:
        grade = "HD"
        print("{} - {}".format(score, grade))
        total_grade += 7
    elif 85 > score >= 75:
        grade = "D"
        print("{} - {}".format(score, grade))
        total_grade += 6
    elif 75 > score >= 65:
        grade = "C"
        print("{} - {}".format(score, grade))
        total_grade += 5
    elif 65 > score >= 50:
        grade = "P"
        print("{} - {}".format(score, grade))
        total_grade += 4
    else:
        grade = "N"
        print("{} - {}".format(score, grade))
        total_grade += 3
total_grade = total_grade / grade_count
print("Your GPA is {:.2f}".format(total_grade))
in_file.close()
