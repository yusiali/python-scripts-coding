message = input("Enter message: ")
message = message.upper()
output = ""
for letter in message:
    if letter.isupper():
        numVal = ord(letter) + 16
        letter = chr(numVal)
        if not letter.isupper():
            numVal -= 26
            letter = chr(numVal)
    output = output + letter
print(output)


