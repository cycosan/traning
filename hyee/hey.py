from caesarcipher import CaesarCipher
import function
import random


def generaterandomstring():
    #
    blank = ""
    count = 0
    sum = 0
    for i in range(0, 100):

        rand = random.randint(65, 122)
        rando=random.randint(0,30)
        ch = chr(rand)
        define1 = CaesarCipher(ch, offset=rando)
        logic1 = function.caeser_cipher(ch, rando)
        a=define1.encoded
        b=logic1
        print("DEFINE", a)
        print("made", b)
        blank = blank + ch
        if(a == b):
            count = count + 1
            print(count)

    # average = (count + sum)
    # sum = average
    # avg = sum / 10
    # print("So avearage is:", avg, "%")

    print(blank)
    cipher = CaesarCipher(blank, offset=rando)
    print(cipher.encoded)
    output = function.caeser_cipher(blank,rando)
    print(output)
    print("Accuracy=", count, "%")
generaterandomstring()

