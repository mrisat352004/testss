#-------------------------------------------------------------------------------
# Program Name: 
# Author: Zahed Khan
# Date: 5/16/2021
# Program Objective: 
#-------------------------------------------------------------------------------
# Pseudocode: 1. 
#             2. 
#                (The amount is entered)
#                (The amount entered is a number)
#                (The amount is between 1 and 20)
#             2.
#                (The grade is entered)
#                (The grade entered is a number)
#                (The grade is less than 100)
#             3. 
#                (Show the average value of the grades entered)
#                (Show the minimum value of the grades entered)
#                (Show the Maximum Value of the Grades entered)
#-------------------------------------------------------------------------------
# Program Inputs: 3 numbers from the user.
# Program Outputs: 
#-------------------------------------------------------------------------------

def rev_string(pFirst, pSecond, pThird):
    pFirst = pFirst[::-1]
    pSecond = pSecond[::-1]
    pThird = pThird[::-1]
    reverse = pFirst+pSecond+pThird;
    return reverse

First = (input("First number: "))
Second = (input("Second number: "))
Third = (input("Third number: "))

rev = rev_string(First, Second, Third)
print(rev)
    




