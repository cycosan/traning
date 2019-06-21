'''name1=input("enter your name")
displacement1=input("enter displacement")'''


def caeser_cipher(name,displacement):
	finalstring=""
	finalstri1=""
	for char in name:
		test=ord(char)
		if(test>=60and test<=90):
			asci=ord(char)+int(displacement)
	
		
			if(asci>90):
				asci=asci-90
				asci=64+asci
				finalstring=finalstring+chr(asci)
			else:
				finalstring=finalstring+chr(asci)
			
		elif(test>=97 and test<=122):
			asci=ord(char)+int(displacement)
		
			
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
