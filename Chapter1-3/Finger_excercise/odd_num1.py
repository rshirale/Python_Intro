"""
Write a program to ask the user to input 10 integers, and then
prints the largest odd that was entered. If no odd number was entered
it should print a message to that effect
"""
# Prompt user for name

odds = []
while True:
    s = int(input("Item: "))
    if s%2 == 0:
        print(f"Please enter only Odd numbers")
        break
    odds.append(s)

for item in sorted(odds):
    print(item)
