'''
arr = [1,2,3,4]
maxs=max(arr[0],arr[1])
mins=min(arr[0],arr[1])
a=len(arr)+2
for i in arr[2:a]:
    if i >maxs:
        mins=maxs
        maxs=i
        print (mins)
    else:
        if i > mins:
            min=i

print(min)
'''
list1 = [10, 20, 4, 45, 99]

max = max(list1[0], list1[1])
secondmax = min(list1[0], list1[1])

for i in range(2, len(list1)):
    if list1[i] > max:
        secondmax = max
        max = list1[i]
    else:
        if list1[i] > secondmax:
            secondmax = list1[i]

print("Second highest number is : ", str(secondmax))