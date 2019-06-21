class Date:
    def __init__(self,Year,Month,Day):
        self.Year=Year
        self.Month=Month
        self.Day=Day
    def __add__(self,other):
        res=Date(self.Year+other.Year,self.Month+other.Month,self.Day+other.Day)
        a=res.Day//30
        b=res.Day%30
        res.Month=res.Month+a
        res.Day=b
        c=res.Month//12
        d=res.Month%12
        res.Year=res.Year+c
        res.Month=d
        return res
    def __sub__(self, other):
        res=Date(self.Year-other.Year,self.Month-other.Month,self.Day-other.Day)
        a = res.Day // 30
        b = res.Day % 30
        print(a)
        res.Month = res.Month + a
        res.Day = b
        c = res.Month // 12
        d = res.Month % 12
        res.Year = res.Year + c
        res.Month = d
        return res
    def getYear(self):
        '''if(len(str(self.Year))!=4):
         print("enter 4 letter year")
        else:'''
        return self.Year
    def getMonth(self):
        if(self.Month>12):
            print("enter month from 1 to 12 only")


        else:
            return self.Month
    def getDay(self):
        if(self.Day>31):
            print("enter month from 1 to 31 only")
        else:
            return self.Day
    def getNepaliDate(self):
        diff=Date(56,8,17)
        nep=self+diff
        return nep
    def __str__(self):
        return str(self.Year)+"/"+str(self.Month)+"/"+str(self.Day)
        print(self.Year)
    def convertNepali(self):
        blank=""
        blank1=""
        blank2=""
        for i in range(0,len(str(self.Year))):
            last=self.Year%10
            self.Year=self.Year//10
            blank=chr(2406+last)+blank
        for i in range(0,len(str(self.Month))):
            last=self.Month%10
            self.Month=self.Month//10
            blank1=chr(2406+last)+blank1
        for i in range(0,len(str(self.Day))):
            last=self.Day%10
            self.Day=self.Day//10
            blank2=chr(2406+last)+blank2
        print(blank)
        return Date(blank,blank1,blank2)

inpDate=Date(2019,6,5)
'''inpDate1=Date(4055,9,30)
#year=inpDate.getYear()
#month=inpDate.getMonth()
#day=inpDate.getDay()
#print(str(year)+"/"+str(month)+"/"+str(day))
z=inpDate+inpDate1
print(str(z.getYear())+"/"+str(z.getMonth())+"/"+str(z.getDay()))
sub=inpDate1-inpDate
print(str(sub.getYear())+"/"+str(sub.getMonth())+"/"+str(sub.getDay()))
'''
print(inpDate)
convert=inpDate.getNepaliDate()
print("the input date is",inpDate.getNepaliDate())
print("The converted one is",convert.convertNepali())
print(convert.getYear())