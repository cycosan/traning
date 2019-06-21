import os
searchItem=input("Enter the item to be search")
location=input("enter the location to be searched")
print(os.getcwd())
os.chdir(location)
print(os.getcwd())
def recu_function():
    fileList=os.listdir()
    print(fileList)

    for lists in fileList:
        if(os.path.isdir(lists)):
            os.chdir(location+"/"+lists)
            #print(os.chdir(location+"/"+lists))
            recu_function()
            print(os.getcwd())
            os.chdir("../")
            print(os.getcwd())
        else:
            file=open(lists)
            path=file.readlines()
            i=1
            for line in path:

                if searchItem in line:
                    print(searchItem,"Found")
                    print(i)
                i=i+1
recu_function()