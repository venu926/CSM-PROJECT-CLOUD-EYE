from cryptography.fernet import Fernet

key=Fernet.generate_key()
print(key)

#Encryption part

fernet=Fernet(key)
with open('key.key','wb') as filekey:
    filekey.write(key)

with open('key.key','rb') as filekey:
    key=filekey.read()

with open('Recording.m4a',"rb") as file:
    orginalaudio=file.read()

encrypted=fernet.encrypt(orginalaudio)

with open('voice encrytion.m4a','wb') as encrypted_file:
    encrypted_file.write(encrypted)

#Decryption
with open('voice encrytion.m4a','rb') as enc_file:
    encrypted=enc_file.read()

decrypted=fernet.decrypt(encrypted)

with open('voice decryption.m4a','wb') as dec_file:
    dec_file.write(decrypted)