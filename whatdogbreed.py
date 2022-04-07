#!/usr/bin/env python3

#A simple quiz to determine what kind of dog breed you are

#valid input list
valid = ["A", "B", "C", "D"]

#variable to hold total points, used to determine breed
total = 0

#list of questions
questions = [
    "It's Friday Night! What are your plans?\nA. PARTY TIME!\nB. Netflix binge\nC. Snoozin'\nD. Dinner with my fab friends\n",
    "How would you describe your body?\nA. Tiny but mighty\nB. Athletic\nC. Tall and lanky\nD. I literally never think about this\n",
    "What's your go-to dance move?\nA. All about the Fist Pump\nB. The Robot\nC. The Cha-Cha slide\nD. Judging everyone from the corner\n",
    "What kind of exercise do you prefer?\nA. Anything with a ball\nB. I'm a gym rat\nC. Sprints\nD. hunting, I'm nature's most efficient predator...\n",
    "How would your friends describe you?\nA. Aggressive and loud\nB. Too smart for my own good\nC. 60mph couch potato\nD. Aloof\n"
]

#function to get user's answer to question
def getAnswer():
    answer = input("Enter a letter (A, B, C, or D): ")
    answer = answer.upper()
    while answer not in valid:
        answer = input("Please enter a letter (A, B, C, or D): ").upper()
    return answer

#function to get the points associated with the users answer       
def getPoints(answer):
    points = 0
    if answer == "A":
        points = points + 1
    elif answer == "B":
       points = points + 2
    elif answer == "C":
        points = points + 3
    else:
       points = points + 4
    return points

#function to determine what breed based on total points
def getBreed(total):
    print("\nCongratulations")
    if total >= 16:
        print("You're not a dog, you're a cat!")
    elif total >= 12:
        print("You're a Greyhound!")
    elif total >= 8:
        print("You're a Dutch Shepherd!")
    elif total > 5:
        print("You're a mixed-breed!")
    else:
        print("You're a chihuahua!")

def askQuestions():
    total = 0
    i = 0
    for question in questions:
        print(questions[i])
        answer = getAnswer()
        total = total + getPoints(answer)
        i += 1
    return total


#determine what breed you are
totalpoints = askQuestions()
getBreed(totalpoints)


