readUser=input("enter name")
file=open("face.txt","a")
file.writelines(readUser+"\n")

i=3
count=1

fileOpen=open("face.txt","r")
for j in fileOpen.readlines():
    if(count==i):
        print(j)
    else:
        count=count+1
