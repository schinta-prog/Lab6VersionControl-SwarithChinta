#Lab 6 Version Control Encoder by Swarith Chinta

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


# Decoder - Luke Barcenas
def decode(encoded_pass):
    encoded_pass = str(encoded_pass)
    decoded_pass = []
    # subtract 3 by each number. if the number is less than
    # zero, change accordingly
    for i in range(len(encoded_pass)):
        temp_char = int(encoded_pass[i]) - 3
        if temp_char == -1:
            decoded_pass.append("9")
        elif temp_char == -2:
            decoded_pass.append("8")
        elif temp_char == -3:
            decoded_pass.append("7")
        else:
            decoded_pass.append(str(temp_char))
    decoded_pass = "".join([str(i) for i in decoded_pass])
    return decoded_pass


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

    elif x == 2:
        print(f"The encoded password is {y}, and the original password is {decode(y)}.")

    elif x == 3:
        break
