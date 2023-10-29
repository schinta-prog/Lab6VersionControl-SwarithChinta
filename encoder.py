#Lab 6 Version Control Encoder by Swartith Chinta

#Encode program
def encode(number):
    en = ""
    for i in number:
        if 0 <= int(i) < 7:
            p = int(i) + 3
            en = en + str(p)
        if int(i) == 7:
            en = en + "0"
        if int(i) == 8:
            en = en + "1"
        if int(i) == 9:
            en = en + "2"
    return en

#Main Loop
while True:
    x = int(input(
"""Menu
-------------
1. Encode
2. Decode
3. Quit

Please enter an option: """))

    if x == 1:
        num = input("Please enter your password to encode: ")
        y = encode(num)
        print("Your password has been encoded and stored!")
        print()