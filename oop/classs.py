class Bike:
    def __init__(self,color,engineSize,power,torque):
        self.color=color
        self.engineSize=engineSize
        self.power=power
        self.torque=torque


    #def printDesc(self):
        #print("This bike is "+self.color +"with"+str(self.engineSize))
    def __str__(self):
        return("This bike is "+self.color +"with"+str(self.engineSize))
    def __str__(self):
        return ("This bike is " + self.torque + "with" + str(self.engineSize))

class Yamaha(Bike):
    def hasabs(self):
        return True
    def printDesc(self):
        print("my bike is yamaha")


myBike=Yamaha("black","1500","1300","1200")
'''yourBike=Bike("red","100","100","2000")
#myBike.color="blue"
myBike.printDesc()
#print(myBike.hasabs())
print(myBike.printDesc())
print(yourBike.printDesc())
'''
print(myBike)