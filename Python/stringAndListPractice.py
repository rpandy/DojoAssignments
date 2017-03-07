'''Find and Replace

In this string: str = "If monkeys like bananas, then I must be a monkey!"
print the position of the first instance of the word "monkey". Then create a new string where the word
"monkey" is replaced with the word "alligator".'''

str = "If monkeys like bananas, then I must be a monkey!"

print str.find("monkeys")

print str.replace("monkeys","alligators")

'''Min and Max

Print the min and max values in a list like this one: x = [2,54,-2,7,12,98].
Your code should work for any list.'''

x = [2,54,-2,7,12,98]

print min(x)
print max(x)

'''First and Last

Print the first and last values in a list like this one: x = ["hello",2,54,-2,7,12,98,"world"].
Now create a new list containing only the first and last values in the original list.
Your code should work for any list.'''

x = ["hello",2,54,-2,7,12,98,"world"]

print x[0]
print x[7]

newX = [x[0],x[7]]
print newX

'''New List

Start with a list like this one: x = [19,2,54,-2,7,12,98,32,10,-3,6].
Sort your list first. Then, split your list in half.
Push the list created from the first half to position 0 of the list created from the second half.
The output should be: [[-3, -2, 2, 6, 7], 10, 12, 19, 32, 54, 98].
Stick with it, this one is tough!'''

x = [19,2,54,-2,7,12,98,32,10,-3,6]

x.sort()
print x

firstHalf = x[0:5]
secondHalf = x[5:]

print firstHalf
print secondHalf

secondHalf.insert(0,firstHalf)

print secondHalf
