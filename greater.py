list1=[10,6,6,6,6,6,6,6,6,6,6,5,6,5,7]
list1.sort()
maximum=max(list1[0],list1[1])
secondMax=min(list1[0],list1[1])
print(maximum)
print(secondMax)
for i in list1[2:]:
    if i>maximum:
        secondMax=maximum
        maximum=i
    elif i==maximum:
        maximum=i

    elif i>secondMax:
        secondMax=i

print(secondMax)