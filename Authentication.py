#Author: Sophie Quinn
#Authenticates user passwords for added security.
from argon2 import PasswordHasher
from argon2.exceptions import VerifyMismatchError

#This is the password hasher that will be used to hash the master password and verify it.
ph = PasswordHasher()

#Creating a test master password to hash and store in the MASTER_HASH variable. 
#Store this hash in the database later.
MASTER_HASH = ph.hash("test")

def check_master_password():
    attempt = input("Enter master password: ")

    try:
        if ph.verify(MASTER_HASH, attempt):
            print("Access granted!")
            return True

    except VerifyMismatchError:
        print("Wrong password.")
        return False

    return False


# Check the master password
if check_master_password():
    print("Showing saved password: testing")
else:
    print("Cannot show password.")