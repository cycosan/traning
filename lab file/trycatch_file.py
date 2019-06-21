'''file=open("new_file.txt","w")
file.writelines("HEllo")
file.close()'''

fileToRead=open("new_file.txt","r")#open newfile in read mode
lines=fileToRead.readlines() #read all linees and store in lines
for country in lines:   #read each country in each lines
    #i=(len(country)-2)
    if(country[-2]=="n"): #last letter having n prints
        print(country)
#print(lines)
fileToRead.close()
try:                          #try
    fileToRead = open("new_file", "r")#throws excption no file name
    lines = fileToRead.readline()
    print(lines)
    fileToRead.close()
except Exception:
    print("exception")
myStr="abcdefgh"
print(myStr[-1])