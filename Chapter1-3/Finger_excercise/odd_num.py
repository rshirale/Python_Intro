"""
Write a program that examines three variables-x,y and z -and
prints the largest odd number among them. If none of them are odd,
it should print a message to that effect
"""
# Prompt user for name
s= input(f"Sir, please enter your name:")
print(f"Hello, {s}, Welcome to largest odd number game\n")

# Prompt user for x
x = int(input("Enter 1st number:"))

# Prompt user for y
y = int(input("Enter 2nd number:"))

# Prompt user for y
z = int(input("Enter 3rd number:"))

print()

# Perform arithmetic to check if variables are odd

if x%2 != 0 and y%2 != 0 and z%2 != 0:
    print(f"{x},{y},{z} are all odd numbers.\nWe are working on finding the largest odd number \n")
    if x > y and x > z:
        print (f"{x} is the largest odd numbers between {x},{y},{z}")
    elif y > x and y > z:
        print (f"{y} is the largest odd numbers between {x},{y},{z}")
    else:
        print (f"{z} is the largest odd numbers between {x},{y},{z}")
else:
    print(f"One of variables in {x},{y},{z} even,\n Cannot continue the\
            operation. \n Enter all odd numbers")
