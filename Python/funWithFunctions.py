'''Odd/Even:
Create a function called odd_even that counts from 1 to 2000.
As your loop executes have your program print the number of that iteration
and specify whether it's an odd or even number.'''

for odd_even in range(1,2000):
    if odd_even % 2 == 0:
        print "The number is",odd_even, "- This is an even number"
    else:
        print "The number is",odd_even, "- This is an odd number"
'''Multiply:
Create a function called 'multiply' that iterates through each value in a list (e.g. a = [2, 4, 10, 16])
and returns a list where each value has been multiplied by 5.
The function should multiply each value in the list by the second argument.'''

myList = [2,4,10,16]
newList = []
def multiply(myList, num):
    for i in range(0,len(myList)): #range is 0 through lenghth
        myList[i] = myList[i] * num
    print myList

multiply(myList, 3)
