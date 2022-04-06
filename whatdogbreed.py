#!/usr/bin/env python3

#simple quiz to determine what kind of dog breed you are

#valid input
valid = ["A", "B", "C", "D"]

#QUESTIONS TODO: refactor this!!
print("It's Friday Night! What are your plans?")
fridayNight = input("A. PARTY TIME!\nB. Snoozin'\nC. Netflix binge\nD. Dinner with my fab friends\n")
fridayNight = fridayNight.upper()
while fridayNight not in valid:
    fridayNight = input("Please enter a letter (A, B, C, or D): ").upper()

print("How would you describe your body?")
bodyType = input("A. Tiny but mighty\nB. Athletic\nC. Tall and lanky\nD. I literally never think about this\n")
bodyType = bodyType.upper()
while bodyType not in valid:
    bodyType = input("Please enter a letter (A, B, C, or D): ").upper()

print("What's your go-to dance move?")
danceMove = input("A. All about the Fist Pump\nB. The Robot\nC. The Cha-Cha slide\nD. Judging everyone from the corner\n")
danceMove = danceMove.upper()
while danceMove not in valid:
    danceMove = input("Please enter a letter (A, B, C, or D): ").upper()

print("What kind of exercise do you prefer?")
exercise = input("A. Anything with a ball\nB. Sprints\nC. I'm a gym rat\nD. hunting, I'm nature's most efficient predator...\n")
exercise = exercise.upper()
while exercise not in valid:
    exercise = input("Please enter a letter (A, B, C, or D): ").upper()

print("How would your friends describe you?")
friendDesc = input("A. Aggressive and loud\nB. 60mph couch potato\nC. Too smart for my own good\nD. Aloof\n")
friendDesc = friendDesc.upper()
while friendDesc not in valid:
    friendDesc = input("Please enter a letter (A, B, C, or D): ").upper()

#Dog breed determination logic (possible options: chihuahua, greyhound, Dutch Shepherd, mixed-breed, cat)
