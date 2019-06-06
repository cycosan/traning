'''file=open("new_file.txt","w")
file.writelines("HEllo")
file.close()'''

fileToRead=open("new_file.txt","r")
lines=fileToRead.readlines()
for country in lines:
    #i=(len(country)-2)
    if(country[-2]=="n"):
        print(country)
#print(lines)
fileToRead.close()
try:
    fileToRead = open("new_file", "r")
    lines = fileToRead.readline()
    print(lines)
    fileToRead.close()
except Exception:
    print("exception")
myStr="abcdefgh"
print(myStr[-1])