import dictionary as dict

# Code to convert plain text into Morse code
def encryptor(text):
    encrypted_text= ""
    for letter in text:
        if letter != " ":

            
            encrypted_text= encrypted_text + dict.MORSE_CODE_DICT.get(letter) + " "
        else:
            
            encrypted_text += " "
    print("Your encrypted morse code is : ",encrypted_text)
    return(encrypted_text)
    