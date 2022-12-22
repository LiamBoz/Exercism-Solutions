def rotate(text, key):
    #abcdefghijklmnopqrstuvwxyz

    # make translate function much smarter OR have a lower character translate and an upper
    sentence = 'The quick.'
    words = sentence.split(" ")
    key = 13

    translate_lower_chars = lambda c : chr((((ord(c)) - 97 + key) % 26) + 97)

    new_str = ""

    for word in words:

        for character in word:
        
            new_str = new_str + translate_f(character)

        new_str = new_str + " "

    return new_str

k = 0
string = ''
def addAs(n):
    global k
    global string
    string = string + 'a'
    k = k + 1
    if k < n:
        return addAs(n)
    else:
        return string

def MakeAs(n, astring):
    if n == 0:
        return astring
    else:
        return MakeAs(n - 1, astring = astring + "a")

print(MakeAs(100, ""))
        

    
# print(addAs(5))
# print(k)

# print(addAs(5))
# print(k)


    # ###### example scratch pad
    # input:
    # char = 'z'
    # key = 1
    # z_ord = 122
    # y_ord = 121
    # x_ord = 120
    

    # what is the eq?

    # step 1: z_ord-97 + key -> 26

    # step 2: 25 % 26 -> 0

    # step 3:  + 97

    # output:
    # answer = 'a'
    # a_ord = '97'

    # pass
