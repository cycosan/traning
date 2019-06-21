string=input("enter the name")
array=string.split(" ")
for i in array:
	space = " "
	check=len(i)
	if(check % 2==0):
		count=(len(i))/2
		space=space+(i[int(count-1)]+i[int(count)])
	elif(check % 2!=0):
		count=(len(i))/2
		count=count-0.5
		space=(i[int(count)])+space


print(space)
	
	


	

	