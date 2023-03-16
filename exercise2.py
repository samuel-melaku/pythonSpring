x = input("Pick a number: ")
y = int(x)
currentnum = 0
previousnum = 0
sum = 0

print("Printing current and previous number sum in a range (" + x + ')')

while currentnum <= y:
    print("Current Number", currentnum, "Previous Number", previousnum, "Sum:", sum)
    previousnum = currentnum
    currentnum = currentnum + 1
    sum = previousnum + currentnum