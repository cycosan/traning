import os
#fileName=input("enter file name")
searchItem=input("enter search word ")

fileToRead=open("new_file.txt","r")
lines=fileToRead.readlines()

i = 1

for country in lines:
    i=int(len(country)-2)
    k=int(len(searchItem))
    if(country[0].lower()==searchItem[0]):#for intial term onlu
        if searchItem in country.lower():
            print(country)
    elif(country[0].upper()==searchItem[0]):#for intial term onlu
        if searchItem in country.upper():
            print(country)
            #print(country)



        #if searchItem in country.lower(): #for any term in between or any place
            #print(country)

#print(lines)
fileToRead.close()