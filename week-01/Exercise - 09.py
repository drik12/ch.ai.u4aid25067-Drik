score1 = int(input("Enter score of Exam 1: "))
score2 = int(input("Enter score of Exam 2: "))

if not (0 <= score1 <= 100 and 0 <= score2 <= 100):
    print("Invalid score entered")
elif score1 >= 50 and score2 >= 50:
    print("You passed!")
else:
    print("You need to retake some exams")
