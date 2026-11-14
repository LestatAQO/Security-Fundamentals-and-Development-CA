#Author Olivier Nowak

import tkinter as tk
import Manager
from tkinter import ttk, messagebox #GUI import

class PasswordManager:

    def __init__(self, root):
        self.root = root
        self.root.title("Password Manager")
        self.root.geometry("1280x720")
        self.root.configure(bg="#9dbdec")
        #db connection to be added here
        self.loginScreen() #start on login screen for now, change to main menu later
        self.failedAttempts = 0

    def clearScreen(self):#clear screen
        for widget in self.root.winfo_children():
            widget.destroy()

    def loginScreen(self):#create window for login screen
        self.clearScreen()

        frame = tk.Frame(self.root, bg="white", padx=50, pady=50)
        frame.place(relx=0.5, rely=0.5, anchor="center")

        tk.Label(frame, text="Password manager", font=("Arial", 24), bg="white").pack(pady=15)

        tk.Label(frame, text="Username", bg="white").pack(anchor="w")
        self.username = tk.Entry(frame, width=35, font=("Arial", 12))
        self.username.pack(pady=8)

        tk.Label(frame, text="Password", bg="white").pack(anchor="w")
        self.password = tk.Entry(frame, width=35, font=("Arial", 12), show="*")
        self.password.pack(pady=8)

        tk.Button(frame, text="Login", font=("Arial", 12), width=5, command=self.attemptLogin).pack(pady=15)
        tk.Button(frame, text="Register", font=("Arial", 12), width=8, command=self.attemptRegistration).pack(pady=15)
    
    def displayPasswords(self):#create window for displaying passwords
        self.clearScreen()
        frame = tk.Frame(self.root, bg="white", padx=50, pady=50)
        frame.place(relx=0.5, rely=0.5, anchor="center")

        tk.Label(frame, text="Password manager", font=("Arial", 24), bg="white").pack(pady=15)

        tk.Button(frame, text="Add", font=("Arial", 12), width=5, command=self.addPassword).pack(pady=15)

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
        self.clearScreen()

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
        
root = tk.Tk()
app = PasswordManager(root)
root.mainloop()