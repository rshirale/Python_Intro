"""
While loop example
How many times should Print letter X
"""
numX = int(input(f"How many times should I print the letter X? "))
toPrint = "X"
num = numX
while (num != 0):
    num -= 1
    print (toPrint, end ="")
