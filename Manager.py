# Author: Yaroslav Kondaurov
# Description: Handles verifications with database, takes input from the GUI and tracks session timer

import time
import Database, Encryption
from argon2 import PasswordHasher

maxDuration = 60
sessionTime = None

ph = PasswordHasher()
key = Encryption.load_key()

# This file will not work until the database has been created first

# Handling first time registration with the application
def registration(userName, password):
    Database.setting_db() # Calls the function to create the new database for the new account if one does not exist already
    if not userName or not password:
        return "Password/Username cannot be an empty field", False
    elif len(userName) < 5 or len(password) < 5:
        return "Password/Username has to be a minimum of 5 characters", False
    
    checker = Database.login_validation(userName, password)
    if checker is True:
        return "Account with this username already exists", False

    hashedPassword = ph.hash(password)

    Database.store_login_db(userName, "adminWeb", hashedPassword)

    resetSession()
    return "Account created", True


# Handling login information
def login(userName, password):
    Database.setting_db() # Calls the function to create the new database for the new account if one does not exist already
    if not userName or not password:
        return "Password/Username cannot be an empty field", False
    
    checker = Database.login_validation(userName, password)

    if checker is False:
        return "Invalid password or username. If you don't have an account, would you like to register?", False

    resetSession()
    return "Login successful", True

def addPassword(userName, website, password):
    session = checkSession()
    if session is False:
        return "Session expired. Please login again", False

    if not userName or not website or not password:
        return "Username/Website/Password cannot be an empty field", False

    Database.store_password_db(userName, website, password, key)
    return "Details added", True

# WIP
# Handling session time to prompt users to log out after a period of inactivity
def checkSession():
    global sessionTime
    if sessionTime is None:
        return False
    elif time.time() - sessionTime > maxDuration:
        sessionTime = None
        return False
    resetSession()

def resetSession():
    global sessionTime
    sessionTime = time.time()
