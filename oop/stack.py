class Stack:
    def __init__(self,*args):
        self.data=list(args)
    def push(self,item):
        if (len(self.data)>=6):

            print("Stack overflow")
        else:
            self.data.append(item)

    def __str__(self):
        blank=""

        for i in self.data:
            blank=blank+str(i)+","
        return blank

    def pop(self):
        a=len(self.data)
        if (a==0):
            print("Stack empty")
        else:
            temp=self.data[-1]
            self.data=self.data[:-1]
            return temp

a=Stack()
while True:

    print("1.Push")
    print("2.Pop")
    print("3.ShowData")
    print("4.Exit")
    Decision=int(input("enter the number"))
    if(Decision==2):
        a.pop()
    elif(Decision==1):
        pushValue=int(input("enter push item"))
        a.push(pushValue)
    elif(Decision==4):
        break
    elif(Decision==3):
        print(a)

'''
print(a)
a.pop()
a.pop()
a.pop()
a.pop()
a.pop()
print(a)
#print(a)
#a.pop()
#print(a)
a.push(5)
print(a)
'''

