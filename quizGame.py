print("Welcome to my computer quiz!")

playing = input("Do you want to play? ")

if playing != "yes":
    quit()

print("Ok! Let's play: :)")
score = 0

answer = input("What does GPU stand for? ").lower()
if answer == "graphics processing unit":
    print("Correct")
    score = score + 1
else:
    print("Incorrect")

answer1 = input("What does RAM stand for? ").lower()
if answer1 == "random access memory":
    print("Correct")
    score = score + 1
else:
    print("Incorrect")

answer2 = input("What does PSU stand for? ").lower()
if answer2 == "power supply":
    print("Correct")
    score = score + 1
else:
    print("Incorrect")

print("You got " + str(score) + " questions correct!")
print("You got " + str((score / 4) * 100) + "%")



""" text = ("FILLER ESTUFF""
print(text.lower()) """