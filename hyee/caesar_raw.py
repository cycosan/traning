'''testStr="isTHisuPPerCaseorlowerCaSE"
print(testStr.isupper())
print(testStr.capitalize())
lower="isthislower"
print(lower.islower())

for charter in testStr:
	if(charter.isupper()==True):
		print(charter,"this is upper")
	else:
		print(charter,"this is lower")'''

name=input("enter your name")
displacement=input("enter displacement")
finalstring=""
for char in name:
	asci=ord(char)+int(displacement)
	if(asci>122):
		asci=asci-122
		asci=96+asci
	elif(asci>90 and asci<97):
		asci=asci-90
		asci=65+asci
	finalstring=finalstring+chr(asci)

print(finalstring)	
	
	#temp=asci-10
	#print(chr(temp))
