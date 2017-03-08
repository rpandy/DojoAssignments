starList = [4,6,1,3,5,7,25]
def stars(starList):
    printValue = 0
    printString = ""
    #for loop will traverse through list.
    for i in range(0,len(starList)):
        #set printString back to empty after each loop has completed
        printString = ""
        printValue = starList[i]
        print printValue, "star(s) printed below:"
        #for loop will print stars for the stated (printValue) amount of times.
        #the number is added to printValue to make it more readable/"Pythonic"
        for i in range(1,printValue+1):
            printString = "*" + printString
        print printString
stars(starList)


starList2 = [4,"Tom",1,"Michael",5,7,"Jimmy Smith"]
def stars2(starList):
    printValue = 0
    printString = ""
    firstLowered = ""
    #for loop will traverse through list.
    for i in range(0,len(starList)):
        if type(starList[i]) is str:
            #set printString back to empty after each loop has completed
            printString = ""
            #pulls the first letter from the name string
            firstLetter = starList[i]
            #switches firstLetter to lowercase
            firstLowered = firstLetter[:1].lower()
            #calculates length of name string
            stringLength = len(starList[i])
            for i in range(1,stringLength+1):
                printString = firstLowered + printString
            print printString
            #print firstLowered[:1].lower()
            #print stringLength

        else:
        #set printString back to empty after each loop has completed
            printString = ""
            printValue = starList[i]
            for i in range(1,printValue + 1):
                printString = "*" + printString
            print printString
stars2(starList2)
