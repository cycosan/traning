'''name1=input("enter your name")
displacement1=input("enter displacement")'''


def caeser_cipher(name,displacement): #definig a fucniton
	finalstring=""
	finalstri1=""
	for char in name: #definig each char in name
		test=ord(char) #Asci value of char
		if(test>=60and test<=90): #if it is captial letter
			asci=ord(char)+int(displacement) #add the displacement in  char
	
		
			if(asci>90):#if displace  yelid value more than Z start from begining
				asci=asci-90
				asci=64+asci
				finalstring=finalstring+chr(asci)
			else:
				finalstring=finalstring+chr(asci)#just add it to the final string
			
		elif(test>=97 and test<=122):
			asci=ord(char)+int(displacement) #For lowercase
		
			
			if(asci>122):
				asci=asci-122
				asci=96+asci
				finalstring=finalstring+chr(asci)
			else:
				finalstring=finalstring+chr(asci)
		else:
			asci=ord(char)
			finalstring = finalstring + chr(asci)
			
	return finalstring
	'''hey=caseser_cypher(name1,displacement1)
print("your encoded code is="+hey)'''

'''for charar in finalstring:
	temp=ord(charar)-int(displacement)
	finalstri1=finalstri1+chr(temp)

print("your decoded="+finalstri1)'''
