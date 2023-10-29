#Lab 6 Version Control Encoder by Swartith Chinta

#Encode program
def encode(number):
    en = ""
    for i in number:
        p = int(i) + 3
        en = en + str(p)
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