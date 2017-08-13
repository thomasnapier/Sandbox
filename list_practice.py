try:
    scores = []
    score = int(input("Score: "))
    while score >= 0:
        scores.append(score)
        score = int(input("Score: "))
    print("Your highest score is", max(scores))

except ValueError:
    print("Enter in some real values first")