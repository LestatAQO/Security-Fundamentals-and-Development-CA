#Author: Lestat Azariel Alvarez Quintana Ordiz
#For the porpuse of this exercise we decided to save data on a database on sqlite for the ease of set up and the ease of sharing to other users so they can use the app with the database on their own devices more easily thanks to not needing a server. 
#RESOURCE USED: https://www.geeksforgeeks.org/python/introduction-to-sqlite-in-python/
import sqlite3

#This function is to set the database.
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

def store_db(userName, email, password):
     connect = sqlite3.connect("userData.db")
     cursor = connect.cursor()

     #insering the information in to the table.
     cursor.execute("""
        INSERT INTO userData(user_name, email, password)
        VALUES (?,?,?)""",(userName, email, password)) #Reference:https://cheatsheetseries.owasp.org/cheatsheets/SQL_Injection_Prevention_Cheat_Sheet.html
        #I was Reading about weaknesses that a database can have and I found out that we where weak against SQL injection, I found how to reinforce that weakness, by putting the "?" as a placeholder we avoid that the attackers could send queries directly with malisious code that would then be executed on our database. I(Previously I used F strings and the parameters where part of the query.)

     connect.commit()
     connect.close()

#This fucntion is to compare the log in information and see if the user is registered.
def login_validation(userName,password):
    #Same as before we need to connect and a cursor.
    connect = sqlite3.connect("userData.db") 
    cursor = connect.cursor()

    #We need this next part to search in the dabase, it will check if the password is in the database WHERE the user name exist.
    cursor.execute("""
        SELECT password FROM userData
        WHERE user_name = ?
        """, (userName,)) #Reference: https://docs.python.org/3/library/sqlite3.html
    #Reference: https://stackoverflow.com/questions/59547851/why-is-there-a-comma-after-the-variable-in-this-sqlite-query
    #When the data is only one parameter we need to add that extra coma so it doesnt devide our strings in to multiple parameters making it understand that is a tuple.

    #our getter for the validation
    valid = cursor.fetchone()
    connect.close()

    #We check for the existence of the user
    if valid is None:
        return False
    #We check for the stored password is the same as the password written by user. 
    if valid[0] == password:
        return True
    else: 
        return False
    
    


