import os
searchItem=input("Enter the item to be search")
location=input("enter the location to be searched")
print(os.getcwd())
os.chdir(location)
print(os.getcwd())
fileList=os.listdir()
print(os.listdir())
for lists in fileList:
    if(os.path.isdir(lists)):
        os.chdir(location+"/"+lists)
        #print(os.chdir(location+"/"+lists))
        fileList1=os.listdir()
        for list1 in fileList1:
            folder=open(list1)
            i=1
            for text in folder.readlines():
                if searchItem in text:
                    print("found")
                    print(i)
                i=i+1
    else:
        file=open(lists)
        path=file.readlines()
        i=1
        for line in path:

            if searchItem in line:
                print("Found")
                print(i)
            i=i+1