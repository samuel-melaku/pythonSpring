string = input("Enter a word: ")
x = len(string)
y = 0
repeats = 0
letters = [*string]

while repeats < x:
    print(letters[y])
    y = y + 2
    repeats = repeats + 2
