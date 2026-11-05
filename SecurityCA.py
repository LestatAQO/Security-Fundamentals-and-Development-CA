import argon2; 
from argon2 import PasswordHasher; #Hashs passwords
from argon2.exceptions import VerifyMismatchError; #Matches the hash to the unhashed password
# ^^ KEEP THIS!!! 

# We might need a database for all of these passwords. Or a list? An array? Something that doesn't reset with every run of the program.

#Testing the imports
ph = PasswordHasher()

password = "thetestpassword"; #Set a password to be hashed
hashed = ph.hash(password); #Put the hashed password into a variable

print("Password hashed successfully!")
print(hashed)

print("Password verification test: ", ph.verify(hashed, password)); #ph.verify checks if the hashed matches the unhashed. If yes, returns true. If not, return false.
