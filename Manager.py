# Author: Yaroslav Kondaurov
# Description: Handles verifications with database and takes input from the GUI

import time
import Database, Encryption

maxDuration = 300
sessionTime = None

# This file will not work until the database has been created first

# Handling first time registration with the application
def registration(userName, password):
    if userName is None or password is None:
        print("Password/Username cannot be an empty field")
        return False
    return

# Handling login information
def login(userName, password):
    checker = Database.login_validation(userName, password)
    if checker is False:
        print("Invalid password or username. If you don't have an account, would you like to register?")
    elif checker is True:
        global sessionTime 
        sessionTime = time.time()
        print("Login successful")

    # Testing
    print("Username: " + userName)
    print("Password: " + password)

# WIP
# Handling session time to log out users after a period of inactivity
def checkSession():
    if time.time() - sessionTime > maxDuration:
        print("Session expired. Please login")
        return