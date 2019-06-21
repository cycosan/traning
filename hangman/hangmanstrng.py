import random
fileRead=open("words.txt","r")
readLines=fileRead.readlines()
randomWords=random.choice(readLines)
print(randomWords)
blank=""
addtionWord=""
tempList=""

j=len(randomWords)
hello=""
print(type(j))
for i in range(j-1):
        tempList=tempList+" _"


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
                    tempList=searchWords
                else:
                    tempList=tempList

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
    print(tempList)
