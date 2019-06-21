StrWord="GeeksForGeeks"
blank=''
i=list(StrWord[0].lower())
for j in StrWord[1:]:
    f=ord(j)
    if (f>=65 and f <=90):
        i.append("_")
        i.append(j.lower())
    else:
        i.append(j)

print(''.join(i))
for word in i:
    blank = blank +word
print(blank)