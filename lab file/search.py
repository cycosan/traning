
fileName=input("enter file name")
searchItem=input("enter search word ")

fileToRead=open(fileName+".txt","r")
lines=fileToRead.readlines()
i=1

for country in lines:
    #i=(len(country)-2)
    if(country[:-1]==searchItem):#orif(country[==searchItem+"\n")#[:-1]indicates all the list excpet last one
        print(i)
    elif(country.lower()[:-1]==searchItem):#changes all the value in upper and comapares
        print(i)
    elif (country.upper()[:-1] == searchItem):
        print(i)
    i=i+1

print(lines)
fileToRead.close()