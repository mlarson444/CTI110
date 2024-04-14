# Matthew Larson
# 14 April 2024
# P4HW1
# This program uses a loop to display score average and a letter grade.

#Prompt user to enter the number of scores (num_scores)
#Initialize an empty list to store scores (scores)
#Loop from 1 to num_scores (inclusive)
#Prompt user to enter a score
#Validate if the score is between 0 and 100
#If valid, add the score to the scores list
#If invalid, notify the user and ask for a valid score until one is provided
#Calculate the lowest score in the scores list
#Remove the lowest score from the scores list
#Calculate the average of the modified scores list
#Determine the letter grade based on the average score
#Display the lowest score, modified scores list, average score, and letter grade to the user

num_scores = int(input("How many scores do you want to enter? "))

scores = []

for i in range(1, num_scores + 1):
    while True:
        try:
            score = float(input(f"Enter score #{i}: "))
            if 0 <= score <= 100:
                scores.append(score)
                break
            else:
                print("INVALID Score entered!!!! Score should be between 0 and 100")
        except ValueError:
            print("Invalid input! Please enter a number.")

lowest_score = min(scores)

scores.remove(lowest_score)

average_score = sum(scores) / len(scores)

if 90 <= average_score <= 100:

    grade = 'A'

elif 80 <= average_score < 90:

    grade = 'B'

elif 70 <= average_score < 80:

    grade = 'C'

elif 60 <= average_score < 70:

    grade = 'D'

else:

    grade = 'F'

print("\n--------------Results-----------")

print(f"Lowest Score  : {lowest_score}")

print("Modified List :", scores)

print(f"Scores Average: {average_score:.2f}")

print(f"Grade         : {grade}")
