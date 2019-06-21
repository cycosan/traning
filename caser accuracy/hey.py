from caesarcipher import CaesarCipher
import function
import random


def generaterandomstring():#defining function
    #
    blank = "" #assigning blank ,count,sum
    count = 0
    sum = 0
    for i in range(0, 100): #to loop the same program from 0 to 100

        rand = random.randint(65, 122) #taking a random variable from 65 to 122 for A to z
        rando=random.randint(0,30)
        ch = chr(rand) #converting asci value to alphabet
        define1 = CaesarCipher(ch, offset=rando) #passing charater and displace to orignal function
        logic1 = function.caeser_cipher(ch, rando) #passingto made fuction
        a=define1.encoded #calling the funtion
        b=logic1
        print("DEFINE", a)
        print("made", b)
        blank = blank + ch #adding each charcter to form a string
        if(a == b):
            count = count + 1 #if original and made equal incarease the count
            print(count)

    # average = (count + sum)
    # sum = average
    # avg = sum / 10
    # print("So avearage is:", avg, "%")

    print(blank) #print whole sting
    cipher = CaesarCipher(blank, offset=rando) #pass whole string
    print(cipher.encoded)
    output = function.caeser_cipher(blank,rando)
    print(output)
    print("Accuracy=", count, "%")
generaterandomstring()

