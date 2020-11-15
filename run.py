


import encrypt as cipher
import decrypt as decipher                           

print("\t\t//////////////////////////////////////////////")
print("\t\t                                              ")
print("\t\t Encryption and Decryption Tool ")
print("\t\t                                               ")
print("\t\t//////////////////////////////////////////////")
print("\n")

ch= input("To encrypt type 'E' or 'e' , and to decrypt type 'D'  or 'd' ")
print("\n")
print("\n")


if (ch=='E' or ch== 'e'):
    plain_Text= input("Type your plain text for encryption: ").upper()
    print("\n")
    
    
    cipher.encryptor(plain_Text)

elif (ch=='D' or ch== 'd'):
    morse_code= input("Type your morse code for decryption:  ")
    print("\n")
    
    
    decipher.decryptor(morse_code)

else:
    print("Your input is incorrect. Please run again and type your input correctly :)")        