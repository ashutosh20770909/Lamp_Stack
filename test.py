import os
import time
directory = 'C:\passwords'
files = os.listdir(directory)

# Define the Caesar cipher function
def caesar_cipher(text, shift):
    result = ''
    for char in text:
        if char.isalpha():
            if char.isupper():
                result += chr((ord(char) + shift - 65) % 26 + 65)
            else:
                result += chr((ord(char) + shift - 97) % 26 + 97)
        else:
            result += char
    return result

# Open the file and read its contents

for file in files:
    with open('C:\passwords'+"\\"+ file,'r') as f:
        print('opening file: ',file)
        store=[]
        ceasor_strings=[]
        data = f.readlines()
        for i in data:
            formatted_i = i[0:-1]
            store.append(formatted_i)
            ceasor_strings.append(caesar_cipher(formatted_i,1)+'\n')
        with open('C:\mudit\mudit.txt','a') as m:
            m.write(file+"\n")
            m.writelines(ceasor_strings)
            m.write("-------------------------\n")


        

    # with open(file, 'r') as f:
    #     lines = f.readlines()

    # # Loop through each line and check if it contains the password
    # for line in lines:
    #     print(line)
    #     if 'password' in line:
    #         # Get the encrypted password from the line
    #         encrypted_password = line.split(':')[1].strip()
    #         print(encrypted_password)
    #         # Decrypt the password using Caesar cipher with shift 3
    #         decrypted_password = caesar_cipher(encrypted_password, -3)

    #         # Print the decrypted password
    #         print("Decrypted password:", decrypted_password)
    #         break
    # else:
    #     print("Password not found in file.")
