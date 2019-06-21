class Account:
    _balance=0

    def getBalance(self):
        return self._balance

    def setBalance(self,bal):
        if (bal >= 0):
            self._balance = bal
        elif(bal!=int):
            Print("Enter integeres")
    def __init__(self,amt):
        self._balance=amt
    def transferTo(self,payee,amt):
        if(self._balance <amt):
            print("Balance not suffiencient")
            return False
        elif amt<0:
            return False
        else:
            self._balance=self._balance-amt
            temp=payee.getBalance()+amt
            setBalance(temp)
            return True

myAccount=Account(100)
yourAccount=Account(90)
print("my",myAccount.getBalance())
print("Your",yourAccount.getBalance())
check=myAccount.transferTo(yourAccount,-200)
if(check):
    print("transcation sucessfull")
else:
    print("Trasncation not sucessfull")
print("my",myAccount.getBalance())
print("Your",yourAccount.getBalance())


