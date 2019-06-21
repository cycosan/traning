class circularQueue:
    data=[]
    def __init__(self,*args,maxsize=10):
        self.data=list(args)
        self.maxsize=maxsize
    def enqueue(self,item):
        if (len(self.data)>=self.maxsize):
            temp=self.data[:-1]
            self.data=[item]
            for i in temp:
                self.data.append(i)
        else:
            temp=self.data
            self.data=[item]
            for i in temp:
                self.data.append(i)


    def dequeue(self):
        a = len(self.data)
        if (a == 0):
            print("Queue empty")
        else:
            temp = self.data[-1]
            self.data = self.data[:-1]
            return temp
if (__name__=="__main__"):
    q1=circularQueue(3,2,1,maxsize=6)
    print(q1.data)
    print(q1.maxsize)
    q1.enqueue(4)
    q1.enqueue(5)
    q1.enqueue(6)
    q1.enqueue(7)
    q1.enqueue(8)
    q1.enqueue(9)
    q1.enqueue(10)
    q1.dequeue()
    q1.dequeue()
    q1.dequeue()
    q1.dequeue()
    q1.dequeue()
    q1.dequeue()
    q1.dequeue()
    q1.enqueue(4)
    q1.enqueue(5)
    q1.enqueue(6)
    q1.enqueue(7)
    q1.enqueue(8)
    q1.enqueue(9)
    q1.enqueue(10)
    print(q1.data)