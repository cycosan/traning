import random
filewead=open("check.txt","w")
filewead.write("hellp")
fileRead=open("words.txt","r")
readLines=fileRead.readlines()
randomWords=random.choice(readLines)
print(randomWords)
addtionWord=""
tempList1 =list(randomWords)
tempList=tempList1[:-1]
j=len(randomWords)
print(type(j))
for i in range(j-1):
    if(i==0):
        tempList[0]=randomWords[0]
    elif(i==random.randint(1,j)):
        tempList[i]=randomWords[i]
    else:
        tempList[i]=" _"
def printString():
    blank=""
    for j in tempList:
        blank=blank+j
    print(blank)
printString()


print(tempList)
life=3

while (life>0):
    print("You have life {}".format(life))
    searchWords=input("enter words")

    if searchWords in randomWords:
        index=0
        if searchWords in addtionWord:
            print("Already entered")
        else:
            for letter in randomWords:
                if(letter==searchWords):
                    tempList[index]=searchWords
                index+=1
            if(life==0):
                print("Your dead")
    else:

        if searchWords in addtionWord:
            print("Already entered")
        elif (life==0):
            print("Your dead")
        else:
            life = life - 1

    addtionWord = addtionWord + searchWords
    printString()
