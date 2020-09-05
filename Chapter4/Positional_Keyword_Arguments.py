# -*- coding: utf-8 -*-
"""
Created on Thu Sep  3 06:47:22 2020
Example of Postional and Keyword arguments
@author: rshirale
"""
# The function assumes firstName and lastName are strings and that reverse is a Boolean
# If reverse == True, it prints lastName, firstName, otherwise it prints firstName lastName
def printName(firstName, lastName, reverse):
    if reverse:
        print(lastName + ', ' + firstName)
    else:
        print(firstName, lastName)

# Each of the following is an equivalent invocation of printName

printName('Olga', 'Punchmajerova', False)
printName('Olga', 'Punchmajerova', reverse = False)
printName('Olga', lastName = 'Punchmajerova', reverse = False)
printName(lastName = 'Punchmajerova',firstName = 'Olga', reverse = False)

# Below statement outputs error, because it is not legal to follow a keywork argument with a non-keyword argument
printName('Olga', lastName = 'Punchmajerova', reverse)
