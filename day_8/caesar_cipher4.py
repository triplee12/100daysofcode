#!/usr/bin/python3
import string

"""Caesar cipher encryption"""

logo = '''

                                                                            $$\           $$\
                                                                            \__|          $$ |
 $$$$$$$\  $$$$$$\   $$$$$$\   $$$$$$$\  $$$$$$\   $$$$$$\         $$$$$$$\ $$\  $$$$$$\  $$$$$$$\   $$$$$$\   $$$$$$\
$$  _____|$$  __$$\  \____$$\ $$  _____| \____$$\ $$  __$$\       $$  _____|$$ |$$  __$$\ $$  __
$$\ $$  __$$\ $$  __$$\
$$ /      $$$$$$$$ | $$$$$$$ |\$$$$$$\   $$$$$$$ |$$ |  \__|      $$ /      $$ |$$ /  $$ |$$ |  $$ |$$$$$$$$ |$$ |  \__|
$$ |      $$   ____|$$  __$$ | \____$$\ $$  __$$ |$$ |            $$ |      $$ |$$ |  $$ |$$ |  $$ |$$   ____|$$ |
\$$$$$$$\ \$$$$$$$\ \$$$$$$$ |$$$$$$$  |\$$$$$$$ |$$ |            \$$$$$$$\ $$ |$$$$$$$  |$$ |  $$ |\$$$$$$$\ $$ |
 \_______| \_______| \_______|\_______/  \_______|\__|             \_______|\__|$$  ____/ \__|  \__| \_______|\__|
                                                                                $$ |
                                                                                $$ |
                                                                                \__|
'''
print(logo)
alphabet = list(string.ascii_letters.lower())
sysmbols = ["'", '"', ",", " ", ".", "?", "!", "@", "#", "$",
        "%", "^", "&", "*"]
numbers = list(string.digits)
alphabet.extend(sysmbols)
alphabet.extend(numbers)

go_again = "yes"

while(go_again == 'yes'):
    direction = input("Type 'encode' to encrypt or 'decode' to decrypt:\n").lower()
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    def ceasar(text, shift, direction):
        encrypted = ""
        decrypted = ""
        for i in text:
            position = alphabet.index(i)
            if direction == "encode":
                position += shift
                encrypted += alphabet[position]
            elif direction == "decode":
                position -= shift
                decrypted += alphabet[position]
        if direction == "encode":
            print(f"Your encoded text is: {encrypted}")
        elif direction == "decode":
            print(f"Your decoded text is: {decrypted}")

    ceasar(text, shift, direction)

    go_again = input("Type 'yes' to enter continue or 'no' to exit\n").lower()
