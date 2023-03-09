num1 = 20
num2 = 30
# expected output is 700

def productCheck(num1, num2):
    if num1 * num2 <= 1000:
        return num1 * num2
    else:
        return num1 + num2