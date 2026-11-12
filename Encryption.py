#Author: Wiktoria Socha
#For this exercise, we decided to use the AES-256 encryption algorithm to encrypt and decrypt the data. We chose it because it is a symmetric encryption algorithm, meaning the same key is used for both encryption and decryption. This makes it faster and more efficient than asymmetric encryption algorithms, which use different keys for encryption and decryption.
#Resources used: https://stackpractices.com/recipes/python-encrypt-decrypt-aes/
from cryptography.hazmat.primitives.ciphers.aead import AESGCM
import os
import base64

#The passwords saved in the database will be encrypted here. 

# Encryption function
def encrypt_password(password, key):
    nonce = os.urandom(12)  # Generate a random nonce (string of random numbers)
    aesgcm = AESGCM(key) # Creates an AESGCM object. This object will be used to perform the encryption operation.
    encrypted = aesgcm.encrypt(nonce, password.encode(), None) # Converts the string password into bytes, and then encrypts it using the AESGCM object.
    combined = nonce + encrypted # Nonce keeps the encryption unique even if the same password is used multiple times
    return base64.urlsafe_b64encode(combined).decode("ascii") # Combined is converted into base-64 encoded bytes. 'Decode' converts the bytes into a string, which is then returned by the function.

#Store encrypted passwords in encrypted_password.

# Decryption function
def decrypt_password(encrypted_password, key):
    combined = base64.urlsafe_b64decode(encrypted_password) # Converting the base64 string back into its original bytes
    nonce = combined[:12] # Takes the first 12 bytes of combined
    encrypted = combined[12:] # Takes everything from position 12 onwards
    aes = AESGCM(key)
    decrypted = aes.decrypt(nonce, encrypted, None)
    return decrypted.decode() # Returns the decoded password if everything is correct
