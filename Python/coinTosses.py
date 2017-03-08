

def coinTosses():
    headCount = 0
    tailCount = 0
    print "Starting program"
    for i in range(1,5000):
        import random
        randNum = random.random()
        randNum = round(randNum)
        #print randNum
        if (randNum == 1):
            randNum = "heads"
            headCount = headCount + 1
            print "Attempt #",i,"Throwing a coin... It's a head! ... Got",headCount,"head(s) so far and",tailCount,"tail(s) so far"
        else:
            randNum = "tails"
            tailCount = tailCount + 1
            print "Attempt #",i,"Throwing a coin... It's a tail! ... Got",headCount,"head(s) so far and",tailCount,"tail(s) so far"
    print "End of program, thank you!"

coinTosses()
