import argon2; 
from argon2 import PasswordHasher; #Hashs passwords
from argon2.exceptions import VerifyMismatchError; #Matches the hash to the unhashed password
# ^^ KEEP THIS!!! 

# 5 use cases, 1 per member. A use case is defined as a 'structured description of how a system interacts with an external actor to achieve a specific goal, outlining both success and failure scenarios'.
# List your use cases here.
# Wiktoria: Password hashing. Does the program correctly identify correct/incorrect passwords when comparing them to their hashed counterparts? How do: 2 users. One will enter password correctly. One will not.
# Lestat:
# Sophie:
# Olivier:
# Yarick: 

#Testing the imports
ph = PasswordHasher()

password = "thetestpassword"; #Set a password to be hashed
hashed = ph.hash(password); #Put the hashed password into a variable

print("Password hashed successfully!")
print(hashed)

print("Password verification test: ", ph.verify(hashed, password)); #ph.verify checks if the hashed matches the unhashed. If yes, returns true. If not, return false.
