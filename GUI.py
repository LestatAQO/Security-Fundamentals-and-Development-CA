#Author Olivier Nowak

import tkinter as tk
from tkinter import ttk, messagebox #GUI import

class PasswordManager:

    def __init__(self, root):
        self.root = root
        self.root.title("Password Manager")
        self.root.geometry("1280x720")
        self.root.configure(bg="#9dbdec")
        #db connection to be added here
        self.loginScreen() #start on login screen for now, change to main menu later


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

    def attemptLogin(self):#authenticate login credentials
        username = self.username.get()#get username and password from entry fields
        password = self.password.get()

        from Manager import login#login function from manager.py
        login(username, password)

    def attemptRegistration(self):#authenticate registration credentials
        username = self.username.get()#get username and password from entry fields
        password = self.password.get()

        from Manager import registration#registration function from manager.py
        registration(username, password)


root = tk.Tk()
app = PasswordManager(root)
root.mainloop()