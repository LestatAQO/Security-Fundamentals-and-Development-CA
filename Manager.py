# Author: Yaroslav Kondaurov
# Description: Handles verifications with database, takes input from the GUI and tracks session timer

import time
import Database, Encryption

maxDuration = 300
sessionTime = None
key = Encryption.load_key()

# This file will not work until the database has been created first

# Handling first time registration with the application
def registration(userName, password):
    Database.setting_db() # Calls the function to create the new database for the new account
    if not userName or not password:
        return "Password/Username cannot be an empty field", False
    
    checker = Database.login_validation(userName, password, key)

    if checker is True:
        return "Account with this username already exists", False

    Database.store_db(userName, "adminWeb", "an encrypted password", key)
    return "Account created", True


# Handling login information
def login(userName, password):
    global sessionTime

    if not userName or not password:
        return "Password/Username cannot be an empty field", False
    
    checker = Database.login_validation(userName, password, key)

    if checker is False:
        return "Invalid password or username. If you don't have an account, would you like to register?", False
    else:
        sessionTime = time.time()
        return "Login successful", True

# WIP
# Handling session time to log out users after a period of inactivity
def checkSession():
    if time.time() - sessionTime > maxDuration:
        print("Session expired. Please login")
        return