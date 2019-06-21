enterWord=input("Enter the word")
file=open("word.txt","w")
file.writelines(enterWord)
file.close()

fileToread=open("word.txt","r")
blank=""
count=3
hey=fileToread.readline()
print(hey)

while count>0:
    userWord = input("Enter the letter")
    for words in hey:
        if userWord in hey:

            for letter in words:
                if userWord in letter:
                    blank=blank+" "+letter
                else:
                    blank=(blank+" _")

        else:
            count=count=count-1
            print(count)
    print(blank)
    if(count==0):
        break





