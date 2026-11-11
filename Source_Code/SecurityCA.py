import argon2; 
from argon2 import PasswordHasher; #Hashs passwords
from argon2.exceptions import VerifyMismatchError; #Matches the hash to the unhashed password
import sqlite3 #Importing the sqlite for the dabase.
from Database import setting_db #Importing our database.
from cryptography.hazmat.primitives.ciphers.aead import AESGCM #For encryption/decryption
# ^^ KEEP THIS!!! 

# 5 use cases, 1 per member. A use case is defined as a 'structured description of how a system interacts with an external actor to achieve a specific goal, outlining both success and failure scenarios'.
# List your use cases here.
# Wiktoria: Encryption/decryption.
# Lestat: Database.
# Sophie: Authentication.
# Olivier: GUI.
# Yarick: Credential management.

#Testing the imports
ph = PasswordHasher()

password = "thetestpassword"; #Set a password to be hashed
hashed = ph.hash(password); #Put the hashed password into a variable

print("Password hashed successfully!")
print(hashed)

print("Password verification test: ", ph.verify(hashed, password)); #ph.verify checks if the hashed matches the unhashed. If yes, returns true. If not, return false.

#There should be a master password that lets the user into the manager. This will be hashed. The passwords in the database will be encrypted. Difference between being hashed and being encrypted is that encryption can be reversed, but hashing can't be -Wiki. 

#We should have a collection of about 5 sample users/emails/passwords that we can use to test the database and the encryption. Do NOT insert the plain password into the database. Defeats the whole point of encrypting them. Could use a for loop to encrypt/decrypt multiple passwords at once. Just lmk and I can implement the functions. -Wiki.

#Im going to write how you would connect and save the data in to the database, yous just need to put the variable names where I put the place holders-. 

#Connecting to database and creating the object for the cursor.
connect = sqlite3.connect("userData.db")
cursor = connect.cursor()

#insering the information in to the table. 
cursor.execute(f"""
    INSERT INTO userData(user_name, email, password)
    VALUES ('{userName}','{email}','{TheHashedPasswordVariableImPrettySure}')""")

connect.commit()
connect.close()