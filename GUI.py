#Author Olivier Nowak

import tkinter as tk
import Manager
from tkinter import ttk, messagebox

class PasswordManager:

    def __init__(self, root):
        self.root = root
        self.root.title("Password Manager")
        self.root.geometry("1280x720")
        self.root.configure(bg="#9dbdec")
        self.loginScreen() #start on login screen for now, change to main menu later
        self.failedAttempts = 0

    def clearScreen(self):#clear screen
        for widget in self.root.winfo_children():#loop through and destroy all widgets to clear screen
            widget.destroy()

    def loginScreen(self):#create window for login screen
        self.clearScreen()

        frame = tk.Frame(self.root, bg="white", padx=50, pady=50)#basic frame we can reuse
        frame.place(relx=0.5, rely=0.5, anchor="center")#center the frame in the middle of the screen

        tk.Label(frame, text="Password manager", font=("Arial", 24), bg="white").pack(pady=15)#title text

        tk.Label(frame, text="Username", bg="white").pack(anchor="w")#text inpout label
        self.username = tk.Entry(frame, width=35, font=("Arial", 12))#text input field
        self.username.pack(pady=8)#padding for visibility

        tk.Label(frame, text="Password", bg="white").pack(anchor="w")#reusing above
        self.password = tk.Entry(frame, width=35, font=("Arial", 12), show="*")
        self.password.pack(pady=8)

        tk.Button(frame, text="Login", font=("Arial", 12), width=5, command=self.attemptLogin).pack(pady=15)#login button calls attemptLogin
        tk.Button(frame, text="Register", font=("Arial", 12), width=8, command=self.attemptRegistration).pack(pady=15)#above but for registration
    
    def displayPasswords(self):#create window for displaying passwords
        self.clearScreen()

        frame = tk.Frame(self.root, bg="white", padx=50, pady=50)#reusing above gui elements for consistency and convenience
        frame.place(relx=0.5, rely=0.5, anchor="center")

        tk.Label(frame, text="Password manager", font=("Arial", 24), bg="white").pack(pady=15)

        columns = ("website", "username", "password")#list labels
        tree = ttk.Treeview(frame, columns=columns, show="headings", height=15)#tkinter treeview to display the passwords in a table
        for col in columns:#loop to make the columns and headings
            tree.heading(col, text=col.capitalize()) #capitalise headers
            tree.column(col, width=250)#set width to fit website lengths

        scrollbar = ttk.Scrollbar(frame, orient="vertical", command=tree.yview)#scrollbar for hypothetical user with a lot of passwords
        tree.configure(yscrollcommand=scrollbar.set)#set the scrollbar to the treeview
        tree.pack(side="left", pady=10)#align to left and padding for visuals
        scrollbar.pack(side="left", fill="y", pady=10)#same as above

        for user_id, website, username, password in Manager.getPasswords():#loop through the passwords and add them to the list
            tree.insert("", "end", iid=user_id, values=(website, username, password))#add passwords to list

        tk.Button(self.root, text="Add", font=("Arial", 12), width=5, command=self.addPassword).place(relx=0.5, rely=0.92, anchor="center")

    def attemptLogin(self):#authenticate login credentials
        if self.failedAttempts >= 3:#if failed attempts is greater than or equal to 3, show error message
            self.showError("Too many failed attempts. Please try again later.")#this serves to lockout the user after 3 failed attempts to prevent brute force attacks
            return
        username = self.username.get()#get username and password from entry fields
        password = self.password.get()

        message, success = Manager.login(username, password)#login function from manager.py
        if success:
            self.displayPasswords()#display passwords if login is successful
        else:
            self.showError(message)#else show error message from manager.py
            self.failedAttempts += 1


    def attemptRegistration(self):#authenticate registration credentials
        username = self.username.get()#get username and password from entry fields
        password = self.password.get()

        message, success = Manager.registration(username, password)#registration function from manager.py
        if success:
            messagebox.showinfo("Success", message)
        else:
            self.showError(message)

    def showError(self, message):#show error message from manager.py
        messagebox.showerror("Error", message)

    def addPassword(self):
        self.clearScreen()#reusing above code for gui again for consistency and convenience

        frame = tk.Frame(self.root, bg="white", padx=50, pady=50)
        frame.place(relx=0.5, rely=0.5, anchor="center")

        tk.Label(frame, text="Add Password", font=("Arial", 24), bg="white").pack(pady=15)

        tk.Label(frame, text="Username", bg="white").pack(anchor="w")
        self.username = tk.Entry(frame, width=35, font=("Arial", 12))
        self.username.pack(pady=8)

        tk.Label(frame, text="Password", bg="white").pack(anchor="w")
        self.password = tk.Entry(frame, width=35, font=("Arial", 12))#no need to obfuscate password here as user has to be logged in to add a password anyway so we can confirm its them adding the password and not someone else also if we obfuscate the password it may lead to a typo
        self.password.pack(pady=8)

        tk.Label(frame, text="Website", bg="white").pack(anchor="w")
        self.website = tk.Entry(frame, width=35, font=("Arial", 12))
        self.website.pack(pady=8)

        tk.Button(frame, text="Add", font=("Arial", 12), width=5, command=self.attemptAddPassword).pack(pady=15)

    def attemptAddPassword(self):
        username = self.username.get()#get username, password and website from entry fields
        password = self.password.get()
        website = self.website.get()

        message, success = Manager.addPassword(username, password, website)
        if success:
            self.displayPasswords()#display passwords if add password is successful
        else:
            self.showError(message)#else show error message from manager.py
        
root = tk.Tk()#tkinter root window
app = PasswordManager(root)#tkinter app class
root.mainloop()#tkinter main loop