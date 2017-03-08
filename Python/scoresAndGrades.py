'''Assignment: Scores and Grades
Write a function that generates ten scores between 60 and 100.
Each time a score is generated, your function should display what the grade is for a particular score.
Here is the grade table:

Score: 60 - 69; Grade - D Score: 70 - 79; Grade - C Score: 80 - 89; Grade - B Score: 90 - 100; Grade - A'''


#import random number 60 to 100 (inclusive)
#performing if statements before running next loop of new random number

def scoresAndGrades():
    for i in range(1,10):
        from random import randint
        randGrade = (randint(60,100))
        #print randGrade
        if (randGrade >= 60 and randGrade <= 69):
            print "Your grade is",randGrade,"and you received a D... Ouch..."
        elif(randGrade >= 70 and randGrade <= 79):
            print "Your grade is",randGrade,"and you received a C."
        elif(randGrade >= 80 and randGrade <= 89):
            print "Your grade is",randGrade,"and you received a B."
        elif(randGrade >= 90 and randGrade <= 100):
            print "Your grade is",randGrade,"and you received a A! GREAT JOB!!"
    print "End of program! bye bye!"

result = scoresAndGrades()
