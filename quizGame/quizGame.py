print("Welcome to my computer quiz!")

playing = input("Do you want to play? ")

if playing != "yes":
    quit()

print("Ok! Let's play: :)")

answer = input("What does GPU stand for? ")
if answer == "graphics processing unit":
    print("Correct")
else:
    print("Incorrect")

answer1 = input("What does RAM stand for? ")
if answer1 == "random access memory":
    print("Correct")
else:
    print("Incorrect")

answer2 = input("What does PSU stand for? ")
if answer2 == "power supply":
    print("Correct")
else:
    print("Incorrect")


