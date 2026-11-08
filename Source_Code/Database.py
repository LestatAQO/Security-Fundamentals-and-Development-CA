#Author: Lestat Azariel Alvarez Quintana Ordiz
#For the porpuse of this exercise we decided to save data on a database on sqlite for the ease of set up and the ease of sharing to other users so they can use the app with the database on their own devices more easily thanks to not needing a server. 
#RESOURCE USED: https://www.geeksforgeeks.org/python/introduction-to-sqlite-in-python/
import sqlite3

def setting_db():
    connect = sqlite3.connect("userData.db") #The connect manages the "communication" with the database that we created, also if the database file doesnt exist it will create it automatically.  
    cursor = connect.cursor() #The cursor is the object in charge of retriving query results and executing the statements. 

    cursor.execute("""
            CREATE TABLE IF NOT EXISTS userData(
            user_id INTEGER PRIMARY KEY,
            user_name TEXT NOT NULL,
            email TEXT NOT NULL,
            password TEXT NOT NULL 
            )""") #SQLite doesnt need autoincrement. When the primary key is an integer it automatically is set to auto increment.

    connect.commit() #Saves the changes made-
    connect.close() #Closes connection to the server.


