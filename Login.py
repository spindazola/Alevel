# Partha Khanna 
# Particle Motion Simulator
# A Level Computer Science Non-examined Project
# Python 3.11.1
# Module 1: Login and Sign up page
# Version 2.2.0

# Libraries Imported
import customtkinter as ctk
import tkinter as tk
from tkinter import messagebox
from tkinter import *
import hashlib
import csv, subprocess
from csv import writer
import pywhatkit
import time
from PIL import Image

# GUI window colour and themes
ctk.set_appearance_mode("Dark")
ctk.set_default_color_theme("blue")

# Class for creating the Pop-up windows (i.e. when a button is clicked windows under this class, a new window is opened)
class ToplevelWindow(ctk.CTkToplevel):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs) # Inheriting basic window properties

# The main GUI window inheriting the basic window properties and further top level windows as methods
class GUIWindow(ctk.CTk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Main GUI window config
        self.geometry("900x600")
        self.title("Login/Signup for Fluid Particle Simulator")
        self.toplevelWindow = None
    
    # Help Window
    def openHelp(self):
        self.helpWindow = ToplevelWindow(self)  # create window if its None or destroyed
        self.helpWindow.geometry("1075x700")
        self.helpWindow.title("Help Window")
        ctk.CTkLabel(self.helpWindow, text="Login", font=("Consolas", titleText)).grid(row=0, column=0, padx=10, pady=20)
        ctk.CTkLabel(self.helpWindow, text="1. Enter your username in the Username box, the one that was entered during registration", font=("Consolas", fieldText)).grid(row=1, column=0, padx=10, pady=3, sticky=W)
        ctk.CTkLabel(self.helpWindow, text="2. Enter the equivalent password that had been entered previously in during registration", font=("Consolas", fieldText)).grid(row=2, column=0, padx=10, pady=3, sticky=W)
        ctk.CTkLabel(self.helpWindow, text="2a. If you fail to remember this value then click on Forgotten Password enter the same username as\nin part 1 to be able to recieve a whatsapp message which allows you to change the password\nand re-login to the system                                                                ", font=("Consolas", fieldText)).grid(row=3, column=0, padx=10, pady=3, sticky=W)
        ctk.CTkLabel(self.helpWindow, text="3. Click on the Login Button to Continue", font=("Consolas", fieldText)).grid(row=4, column=0, padx=10, pady=3, sticky=W)

        ctk.CTkLabel(self.helpWindow, text="SignUp", font=("Consolas", titleText)).grid(row=5, column=0, padx=10, pady=20)
        ctk.CTkLabel(self.helpWindow, text="1. Enter any username, this should be something memorable. This should be between 5 and 15 character\nand unused by all other users or an error message will be shown. This is a required field.", font=("Consolas", fieldText)).grid(row=6, column=0, padx=10, pady=3, sticky=W)
        ctk.CTkLabel(self.helpWindow, text="2. Enter an associated email that will be used for the forgotten password functioality and allow for\nan email to be sent. It should be in the form of 'email@example.com' and should be unique \n- there hasn't been an account registered on that email address. This is a Required Field.", font=("Consolas", fieldText)).grid(row=7, column=0, padx=10, pady=3, sticky=W)
        ctk.CTkLabel(self.helpWindow, text="3. Enter the phone number as shown: +[country code][Number] e.g. +4412345678900. This isn't required", font=("Consolas", fieldText)).grid(row=8, column=0, padx=10, pady=3, sticky=W)
        ctk.CTkLabel(self.helpWindow, text="4. Enter the Password for your account. This should be memorable and kept secure preferably by using\nan Alphanumeric Password using Uppercase, lowercase, symbols, numbers. Confirm Password is\nalso required which should match you password. This should be between 8 and 15 characters.", font=("Consolas", fieldText)).grid(row=9, column=0, padx=10, pady=3, sticky=W)
        ctk.CTkLabel(self.helpWindow, text="5. Choose the type of User. This must be selected to enter the simulation as a student or a teacher.\nA student is able to access the simulation but a teacher can access more features such as \nto present it to the class etc.                                                         ", font=("Consolas", fieldText)).grid(row=10, column=0, padx=10, pady=3, sticky=W)
        ctk.CTkLabel(self.helpWindow, text="6. Click on the SignUp Button to Continue", font=("Consolas", fieldText)).grid(row=11, column=0, padx=10, pady=3, sticky=W)

    # About Window
    def openAbout(self):
        self.aboutWindow = ToplevelWindow(self)  # create window if its None or destroyed
        self.aboutWindow.geometry("1075x550")
        self.aboutWindow.title("About Window")
        ctk.CTkLabel(self.aboutWindow, text="This is part of the Fluid Particle Simualtor Application and is a system designed to allow users to \nregister as required and login to the system in order to access the Simulator.", font=("Consolas", fieldText)).grid(row=0, column=0, columnspan=2, sticky=W, padx=15, pady=10)

        ctk.CTkLabel(self.aboutWindow, text="Version", font=("Consolas", titleText)).grid(row=1, column=0, padx=15, pady=10)
        ctk.CTkLabel(self.aboutWindow, text="Alterations", font=("Consolas", titleText)).grid(row=1, column=1, padx=15, pady=10)

        n = 8
        ctk.CTkLabel(self.aboutWindow, text="2.2.0", font=("Consolas", fieldText)).grid(row=n-6, column=0, sticky=W, padx=15, pady=10)
        ctk.CTkLabel(self.aboutWindow, text="Minor Updates and Bug Fixes", font=("Consolas", fieldText)).grid(row=n-6, column=1, sticky=W, padx=15, pady=10)

        ctk.CTkLabel(self.aboutWindow, text="2.1.0", font=("Consolas", fieldText)).grid(row=n-5, column=0, sticky=W, padx=15, pady=10)
        ctk.CTkLabel(self.aboutWindow, text="Creation of Help and About buttons to guide users to the use of this system\nand the system versioning with alterations performed", font=("Consolas", fieldText)).grid(row=n-5, column=1, sticky=W, padx=15, pady=10)

        ctk.CTkLabel(self.aboutWindow, text="2.0.0", font=("Consolas", fieldText)).grid(row=n-4, column=0, sticky=W, padx=15, pady=10)
        ctk.CTkLabel(self.aboutWindow, text="System Integration into donwloadable file (via .exe)", font=("Consolas", fieldText)).grid(row=n-4, column=1, sticky=W, padx=15, pady=10)

        ctk.CTkLabel(self.aboutWindow, text="1.1.0", font=("Consolas", fieldText)).grid(row=n-3, column=0, sticky=W, padx=15, pady=10)
        ctk.CTkLabel(self.aboutWindow, text="Addition of Forgotten Password Field - Allowing the user to enter a valid Username\nand be sent a Whatsapp message as per their entered phone number", font=("Consolas", fieldText)).grid(row=n-3, column=1, sticky=W, padx=15, pady=10)

        ctk.CTkLabel(self.aboutWindow, text="1.0.2", font=("Consolas", fieldText)).grid(row=n-2, column=0, sticky=W, padx=15, pady=10)
        ctk.CTkLabel(self.aboutWindow, text="Minor Bug Fixes - Password field character limit", font=("Consolas", fieldText)).grid(row=n-2, column=1, sticky=W, padx=15, pady=10)    

        ctk.CTkLabel(self.aboutWindow, text="1.0.1", font=("Consolas", fieldText)).grid(row=n-1, column=0, sticky=W, padx=15, pady=10)
        ctk.CTkLabel(self.aboutWindow, text="Minor Bug Fixes - Username field character limit", font=("Consolas", fieldText)).grid(row=n-1, column=1, sticky=W, padx=15, pady=10)

        ctk.CTkLabel(self.aboutWindow, text="1.0.0", font=("Consolas", fieldText)).grid(row=n, column=0, sticky=W, padx=15, pady=10)
        ctk.CTkLabel(self.aboutWindow, text="System Creation", font=("Consolas", fieldText)).grid(row=n, column=1, sticky=W, padx=15, pady=10)

# Basic formatting - creating a window
window = GUIWindow()

# Text sizes
titleText = 35
fieldText = 19
btnText = 22

# Procedure: Logging in with user authentication
def login():
    # Acquiring user inputs
    un = loginUsernameBox.get()
    ps = loginPasswordBox.get()
    valid = False
    # Check if there exists a username and password combination in a separate csv file
    with open("userData.csv", "rt") as f:
        users = csv.reader(f, delimiter=',')
        for row in users:
            if un in row:
                if str(hashlib.sha256(ps.encode('utf-8', errors='strict')).hexdigest()) == row[2]:
                    valid = True
            else:
                valid = False
    
    # Opening the Simulator if the user has logged in correctly
    if valid == True:
        messagebox.showinfo(title="Successful", message="You have logged in\nThe simulator will open shortly")
        window.destroy()
        time.sleep(0.25)
        filename = "ParticleSimulation.py"
        subprocess.run(["python", filename], check =True)
    else:
        # Error message if incorrectly logged in
        messagebox.showwarning(title="Invalid Login", message="Your Username and/or Password were incorrect.\nPlease try again.")

# Function: Storing user data after signing up in a csv file
def store(un, em, ph, hashps, type):
    # All data to be stored put in an array and then written in a new line
    Userdata = [str(un), str(em), str(ph), str(hashps), str(type)]
    with open("userData.csv", "a+", newline='') as f:
        write = writer(f)
        write.writerow(Userdata)
    return True

# Signup: Signing up to the system with validation checks
def signUp():
    data = (signupUsernameBox.get(), signupEmailBox.get(), signupPasswordBox.get(), signupPasswordConfirmBox.get(), signupPhoneBox.get())
    # Validation checks (length and presence check)
    errorMessage = ""

    # ------------------------- USERNAME LENGTH CHECK -------------------------
    if 15 >= len(data[0]) >= 5:
        valid = True
    else:
        errorMessage += "Username should be between 5 and 15 characters.\n"
        valid = False
          
    # ------------------------- EMAIL FORMAT CHECK -------------------------
    if not('@' in data[1]):
        errorMessage += "Email is in incorrect format.\n"
        valid = False
    else:
        valid = True
    
    # ------------------------- PASSWORD LENGTH CHECK -------------------------
    if 20 >= len(data[2]) >= 5:
        valid = True
    else: 
        errorMessage += "Password should be between 5 and 20 characters.\n"
        valid = False
    
    # ------------------------- PASSWORD AND PASSWORD CONFIRMATION CHECK -------------------------
    if str(hashlib.sha256(data[2].encode('utf-8', errors='strict')).hexdigest()) == str(hashlib.sha256(data[3].encode('utf-8', errors='strict')).hexdigest()):
        valid = True
    else:
        errorMessage += "Password and Password Confirmation must match.\n"
        valid = False

    # ------------------------- USER TYPE PRESENCE CHECK -------------------------
    if (userType() == "student") or (userType() == "teacher"):
        valid = True
    else:
        valid = False
        errorMessage += "Please select Student or Teacher\n"

    # ------------------------- EXISTING RECORD CHECK -------------------------
    with open("userData.csv", "rt") as f:
        users = csv.reader(f, delimiter=',')
        # Traverse through each row
        for row in users:
            # Check if the email entered is already previously entered
            if data[1] in row:
                valid = False
                errorMessage += "Email is already Registered\n"
            # Check if the username entered is already previously entered
            if data[0] in row:
                valid = False
                errorMessage += "Username is already Registered, Please login or use a different Username\n"

    # ------------------------- STORE DETAILS -------------------------
    # if all validations checks are passed then pass the user onto the next stage, otherwise show an error
    if valid == True and errorMessage == "":
        if data[4] == "":
            store(data[0], data[1], str(hashlib.sha256(data[2].encode('utf-8', errors='strict')).hexdigest()), userType())
        else:
            store(data[0], data[1], str(hashlib.sha256(data[2].encode('utf-8', errors='strict')).hexdigest()), userType(), data[4])
        messagebox.showinfo(title="Account Created", message="You have entered valid details and have now created an account for the simulation.\nPlease login.")
    else:   
        messagebox.showerror(title="Error", message=errorMessage)
        exit    

# Procedure: Clear text to remove any text in boxes once a Button is clicked
def clearText():
    # Clearing all entries
    loginUsernameBox.delete(0, len(loginUsernameBox.get()))
    loginPasswordBox.delete(0, len(loginPasswordBox.get()))
    
    signupUsernameBox.delete(0, len(signupUsernameBox.get()))
    signupEmailBox.delete(0, len(signupEmailBox.get()))
    signupPhoneBox.delete(0, len(signupPhoneBox.get()))
    signupPasswordBox.delete(0, len(signupPasswordBox.get()))
    signupPasswordConfirmBox.delete(0, len(signupPasswordConfirmBox.get()))
    value.set("0")

def ForgotPassword():
    # Procedure: if the user forgets their password then they can change it
    message = "Hello there!\nTo change your password please contact you system administrator"
    # User enters username and if there is a phone number enteres then a whatsapp emssage is sent otherwise an email is sent
    with open("userData.csv", "rt") as f:
        users = csv.reader(f, delimiter=',')
        forgot = ctk.CTkInputDialog(text="Enter your Username to recieve a message to change your password", title="Forgot Password")
        un = forgot.get_input()
        for row in users:
            if un in row:
                phone = row[2]
                if phone == "N/A":
                    # To be completed by setting up an SMTP server
                    pass
                else:
                    pywhatkit.sendwhatmsg_instantly(phone, message)

def userType():
    # Function: User types associated with the user entery via radio buttons
    # If user selects 1, then student is returned, if 2 is selected then teacher is returned
    if value.get() == "1":
        return "student"
    elif value.get() == "2":
        return "teacher"

# Setting up the variable to store the radio button entry for user type
value = tk.StringVar()
value.set("0")

# Button images (for help and about)
aboutImg = ctk.CTkImage(Image.open("info.png"), size=(30,30))
helpImg = ctk.CTkImage(Image.open("help.png"), size=(30,30))

# ------------------------- INFORMATION PANEL -------------------------
infoFrame = ctk.CTkFrame(window, width = 66, height = 35)
# help and about buttons
helpButton = ctk.CTkButton(infoFrame, image=helpImg, text="", width=25, height=35, command=window.openHelp).grid(row=0, column=0, padx=3, sticky=W)
aboutButton = ctk.CTkButton(infoFrame, image=aboutImg, text="", width=25, height=35, command=window.openAbout).grid(row=0, column=1, padx=3, sticky=W)
infoFrame.grid(row=0, column=0, sticky=W)

# Main Title text
mainText = ctk.CTkLabel(window, text="Fluid Particle Simulator", font=("Consolas", 40)) # Main Header Text
mainText.grid(row=1, column=0, columnspan=6, pady=10)

# ------------------------- LOGIN PANEL -------------------------
# Creating the login Frame with its appropriate widgets
frameLogin = ctk.CTkFrame(window, width=500, height = 250, border_width=3, border_color='#beebce')

# Login Title Text
loginText = ctk.CTkLabel(frameLogin, text="Login", font=("Consolas", titleText)) # Login Header Text
loginText.grid(row=0, column=0, columnspan=2, pady=30)

# Username text and entry box
loginUsername = ctk.CTkLabel(frameLogin, text="Username", font=("Consolas", fieldText)) # Username Text
loginUsername.grid(row=1, column=0, padx=10, pady=5)
loginUsernameBox = ctk.CTkEntry(frameLogin, font=("Consolas", fieldText), width=200, placeholder_text="Username") # Username CTkEntry Box
loginUsernameBox.grid(row=1, column=1, padx=20)

# Password Text and Entry Box
loginPassword = ctk.CTkLabel(frameLogin, text="Password", font=("Consolas", fieldText)) # Password Text
loginPassword.grid(row=2, column=0, padx = 10, pady=5)
loginPasswordBox = ctk.CTkEntry(frameLogin, show="•", font=("Consolas", fieldText), width=200, placeholder_text="Password") # Password CTkEntry Box
loginPasswordBox.grid(row=2, column=1)

# Login Button
loginButton = ctk.CTkButton(frameLogin, text="Login", font=("Consolas", btnText), command=lambda: [login(), clearText()]) # Continue CTkButton
loginButton.grid(row=3, column=0, columnspan=2, pady=30)

# Forgot Password button
toForgotButton = ctk.CTkButton(frameLogin, text="Forgotten Password?", command=ForgotPassword, font=("Consolas", btnText)) # Continue CTkButton
toForgotButton.grid(row=4, column=0, columnspan=2, pady=30)

frameLogin.grid(row=2, column=0, columnspan=3, padx=30)

# ------------------------- SIGN UP PANEL -------------------------
# Creating the signup Frame with its appropriate widgets
frameSignUp = ctk.CTkFrame(window, width=500, height = 250, border_width=3, border_color='#f7eaad')

# Sign Up Title Text
signUpText = ctk.CTkLabel(frameSignUp, text="Sign Up", font=("Consolas", titleText)) # SignUp Header Text
signUpText.grid(row=0, column=0, columnspan=2, pady=30)

# Username Text and Entry Box
signupUsername = ctk.CTkLabel(frameSignUp, text="Username*", font=("Consolas", fieldText)) # Username Text
signupUsername.grid(row=1, column=0, padx=5, pady=5)
signupUsernameBox = ctk.CTkEntry(frameSignUp, font=("Consolas", fieldText), width=200, placeholder_text="Username") # Username CTkEntry Box
signupUsernameBox.grid(row=1, column=1, padx=20)

# Email Text and Entry Box
signupEmail = ctk.CTkLabel(frameSignUp, text="Email*", font=("Consolas", fieldText)) # Username Text
signupEmail.grid(row=2, column=0, padx=5, pady=5)
signupEmailBox = ctk.CTkEntry(frameSignUp, font=("Consolas", fieldText), width=200, placeholder_text="Email") # Username CTkEntry Box
signupEmailBox.grid(row=2, column=1, padx=20)

# Phone Number Text and Entry Box
signupPhone = ctk.CTkLabel(frameSignUp, text="Phone Number", font=("Consolas", fieldText)) # Username Text
signupPhone.grid(row=3, column=0, padx=5, pady=5)
signupPhoneBox = ctk.CTkEntry(frameSignUp, font=("Consolas", fieldText), width=200, placeholder_text="Phone Number") # Username CTkEntry Box
signupPhoneBox.grid(row=3, column=1, padx=20)

# Password Text and Entry Box
signupPassword = ctk.CTkLabel(frameSignUp, text="Password*", font=("Consolas", fieldText)) # Password Text
signupPassword.grid(row=4, column=0, pady=5)
signupPasswordBox = ctk.CTkEntry(frameSignUp, show="•", font=("Consolas", fieldText), width=200, placeholder_text="Password") # Password CTkEntry Box
signupPasswordBox.grid(row=4, column=1)

# Confirm Password Text and Entry Box
signupPasswordConfirm = ctk.CTkLabel(frameSignUp, text="Confirm Password*", font=("Consolas", fieldText)) # Password Confirmation Text
signupPasswordConfirm.grid(row=5, column=0, pady=5, padx = 7)
signupPasswordConfirmBox = ctk.CTkEntry(frameSignUp, show="•", font=("Consolas", fieldText), width=200, placeholder_text="Confirm Password") # Password Confirmation CTkEntry Box
signupPasswordConfirmBox.grid(row=5, column=1, padx = 5)

# Person Type
personType = ctk.CTkFrame(frameSignUp)
# Password Text and Radio Buttons
ctk.CTkLabel(personType, text="Type*", font=("Consolas", fieldText)).grid(row=0, column=0, padx=15, pady=10)

student = ctk.CTkRadioButton(personType, text="Student", variable = value, value = 1, font=("Consolas", btnText))
student.grid(row=0, column=1, sticky=W, padx=15, pady=10)

teacher = ctk.CTkRadioButton(personType, text="Teacher", variable = value, value = 2, font=("Consolas", btnText))
teacher.grid(row=0, column=2, sticky=W, padx=15, pady=10)

personType.grid(row = 6, column = 0, columnspan = 2, pady= 8)

# Sign Up button
signupButton = ctk.CTkButton(frameSignUp, text="Sign Up", font=("Consolas", btnText), command=lambda: [signUp(), clearText()]) # Continue CTkButton
signupButton.grid(row=7, column=0, columnspan=2, pady=30)

frameSignUp.grid(row=2, column=4, padx=30, pady=30)

# Centre Window in the screen
window.eval('tk::PlaceWindow . center')

window.mainloop()