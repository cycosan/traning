class Stack:
    def __init__(self,*args):
        self.data=list(args)
    def push(self,item):

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
    def checkdata(self):
        d=len(self.data)
        return d
if (__name__=="__main__"):
    a=Stack(1,2,3)
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


