import argon2; 
from argon2 import PasswordHasher; #Hashs passwords
from argon2.exceptions import VerifyMismatchError; #Matches the hash to the unhashed password
import sqlite3 #Importing the sqlite for the dabase.
from Database import setting_db #Importing our database.
from Encryption import encrypt_password, decrypt_password #For encryption. These functions encrypt the passwords before they're inserted into the database, and decrypt them when they've been retrieved.
# ^^ KEEP THIS!!! 

# 5 use cases, 1 per member. A use case is defined as a 'structured description of how a system interacts with an external actor to achieve a specific goal, outlining both success and failure scenarios'.
# List your use cases here.
# Wiktoria: Encryption/decryption.
# Lestat: Database management.
# Sophie: Authorisation.
# Olivier: GUI.
# Yarick: Credential management.

#Testing the imports
ph = PasswordHasher()

password = "thetestpassword"; #Set a password to be hashed
hashed = ph.hash(password); #Put the hashed password into a variable

print("Password hashed successfully!")
print(hashed)

print("Password verification test: ", ph.verify(hashed, password)); #ph.verify checks if the hashed matches the unhashed. If yes, returns true. If not, return false.

