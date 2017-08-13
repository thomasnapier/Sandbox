vowel_count = 0
letter_count = 0
name = input("Enter in your name: ")
for char in name:
    if char == "a" or char == "e" or char == "i" or char == "o" or char == "u":
        vowel_count += 1
    letter_count +=1
print("Out of {} letters, {} has {} vowels".format(letter_count, name, vowel_count))
