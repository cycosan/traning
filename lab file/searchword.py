import os
#fileName=input("enter file name")
searchItem=input("enter search word ")

fileToRead=open("new_file.txt","r")
lines=fileToRead.readlines()

i = 1

for country in lines:
    i=int(len(country)-2)
    k=int(len(searchItem))
    for l in range(0,k):
        for j in range(0,i):
            if(country[j+l]==searchItem[l]):
                print(country)




#print(lines)
fileToRead.close()