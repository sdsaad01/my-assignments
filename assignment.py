'''
1.   Defines a function named factorial that takes a number as an argument and calculates its factorial using a loop or recursion.
2.   Returns the calculated factorial.
3.   Calls the function with a sample number and prints the output.
 
'''
#task 1 
def factorial(x):
    if x < 2:
        return 1 
    else:
        return x * (factorial(x-1)) 
result= factorial(4)

print("Your factorial is ", result)

#Task 2 
'''''
Asks the user for a number as input.
2.   Uses the math module to calculate the:
o   Square root of the number
o   Natural logarithm (log base e) of the number
o   Sine of the number (in radians)
3.   Displays the calculated results.
'''   
import math
user_1 = int(input("enter your number  :"))
square1 = (math.sqrt(user_1))
print( "square root of :", square1)
log1 = (math.log(user_1))
print("your log value is: ",log1)
sin1 = (math.sin(user_1))
print("your sine value is : ", sin1)
