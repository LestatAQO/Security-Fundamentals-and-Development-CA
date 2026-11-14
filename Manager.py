# Author: Yaroslav Kondaurov
# Description: Handles taking input from the GUI, verifying it to be valid information, sends passwords to be either hashed for 
#   login information or encrypt for storage.

import time # Time import to handle session timer
import Database, Encryption # Importing Database and Encryption files to call functions within
from argon2 import PasswordHasher

# Session timer variables
maxDuration = 60 # How long in seconds, an active session lasts
sessionTime = None

ph = PasswordHasher()
key = Encryption.load_key()

# This function handles registration by creating a new account
def registration(userName, password):
    Database.setting_db() # Calls the function to create the new table for the new account if one does not exist already
    # An if statement ensuring the fields entered are not empty and are of a minimum length, in this case being 5 characters
    # If something invalid is detected, return the error message along with a False boolean
    if not userName or not password:
        return "Password/Username cannot be an empty field", False
    elif len(userName) < 5 or len(password) < 5:
        return "Password/Username has to be a minimum of 5 characters", False

    # Checks with the database to see if an existing account already exists with the same username
    # If one exists, return the appropriate message
    checker = Database.login_validation(userName, password)
    if checker is True:
        return "Account with this username already exists", False

    # Hashes the new password
    hashedPassword = ph.hash(password)

    # Stores the new details with the new username, the hashed password. The website is irrelevant for login or registration
    Database.store_login_db(userName, "adminWeb", hashedPassword)

    return "Account created", True


# This function handles the login
def login(userName, password):
    Database.setting_db() # Calls the function to create the new table for the new account if one does not exist already
    # As previously in the registration, we check that the fields are not empty
    if not userName or not password:
        return "Password/Username cannot be an empty field", False

    # Checks with the database to see if an existing account already exists with the same username
    # If one doesn't exist, return the appropriate message
    checker = Database.login_validation(userName, password)
    if checker is False:
        return "Invalid password or username. If you don't have an account, would you like to register?", False

    # Run the resetSession function to start keeping a record on time
    resetSession()
    return "Login successful", True

# This function handles the adding of passwords from GUI
def addPassword(userName, website, password):
    # Calls the checkSession function to recheck if the session is valid
    session = checkSession()
    if session is False:
        return "Session expired. Please login again", False # If the session is invalid, end the function early and send the appropriate message for the user to log out

    # Check if the fields are not empty
    if not userName or not website or not password:
        return "Username/Website/Password cannot be an empty field", False

    # Call the database function to store passwords by passing the username, website and password. The key is also supplied to allow the correct encryption to be applied
    Database.store_password_db(userName, website, password, key)
    return "Details added", True

def getPasswords():
    return Database.getPasswords()

# Handling session time to prompt users to log out after a period of inactivity
def checkSession():
    global sessionTime # Gets the global sessionTime variable
    if sessionTime is None: # Checks if there is a valid session
        return False
    elif time.time() - sessionTime > maxDuration: # Checks how long the session has lasted since last refresh
        sessionTime = None
        return False
    # If the session is still valid, reset the session
    resetSession()

# Resets the sessionTime variable to the up to date time
def resetSession():
    global sessionTime
    sessionTime = time.time()