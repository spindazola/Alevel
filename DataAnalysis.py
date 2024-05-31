# Partha Khanna 
# Particle Motion Simulator
# A Level Computer Science Non-examined Project
# Python 3.11.1
# Module 3: Data Analysis
# version 2.3.1

# Libraries Imported
import pandas as pd
import matplotlib.pyplot as plt
import tkinter as tk
from tkinter import *
from tkinter import messagebox
import customtkinter as ctk
from PIL import Image
import subprocess

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
        self.geometry("930x450")
        self.title("Setting Page for Data Analysis")
        self.toplevelWindow = None

    # Help window
    def openHelp(self):
        self.helpWindow = ToplevelWindow(self)  # create window if its None or destroyed
        self.helpWindow.geometry("675x590")
        self.helpWindow.title("Help Window")
        ctk.CTkLabel(self.helpWindow, text="X-axis", font=("Consolas", titleText)).grid(row=0, column=0, padx=10, pady=10)
        ctk.CTkLabel(self.helpWindow, text="1. Select the Quantity you would like to see on the x-axis of the graph", font=("Consolas", fieldText)).grid(row=1, column=0, padx=10, pady=3, sticky=W)
        
        ctk.CTkLabel(self.helpWindow, text="Y-axis", font=("Consolas", titleText)).grid(row=2, column=0, padx=10, pady=10)
        ctk.CTkLabel(self.helpWindow, text="1. Select the Quantity you would like to see on the y-axis of the graph", font=("Consolas", fieldText)).grid(row=3, column=0, padx=10, pady=3, sticky=W)
        
        ctk.CTkLabel(self.helpWindow, text="Graph Type", font=("Consolas", titleText)).grid(row=4, column=0, padx=10, pady=10)
        ctk.CTkLabel(self.helpWindow, text="1. Select the Type of graph you would like to see:", font=("Consolas", fieldText)).grid(row=5, column=0, padx=10, pady=3, sticky=W)
        ctk.CTkLabel(self.helpWindow, text="1a. A Line graph shows a clear line (or best fit line) using the datapoints\ncollected in the experiment", font=("Consolas", fieldText)).grid(row=6, column=0, padx=10, pady=3, sticky=W)

        ctk.CTkLabel(self.helpWindow, text="Colour", font=("Consolas", titleText)).grid(row=7, column=0, padx=10, pady=10)
        ctk.CTkLabel(self.helpWindow, text="1. Enter the amount of Red, Blue and Green to see in the colour from 0 to 255", font=("Consolas", fieldText)).grid(row=8, column=0, padx=10, pady=3, sticky=W)
        ctk.CTkLabel(self.helpWindow, text="2. Click on See Colour to view the colour form the entered values\nand also store the colour in the system", font=("Consolas", fieldText)).grid(row=9, column=0, padx=10, pady=3, sticky=W)

        ctk.CTkLabel(self.helpWindow, text="Create Graph", font=("Consolas", titleText)).grid(row=10, column=0, padx=10, pady=10)
        ctk.CTkLabel(self.helpWindow, text="1. Once the X-axis, Y-axis, Graph Type and Colour have been chosen,\nyou can proceed to view the Graph", font=("Consolas", fieldText)).grid(row=11, column=0, padx=10, pady=3, sticky=W)

    # About Window
    def openAbout(self):
        self.aboutWindow = ToplevelWindow(self)  # create window if its None or destroyed
        self.aboutWindow.geometry("825x475")
        self.aboutWindow.title("About Window")
        ctk.CTkLabel(self.aboutWindow, text="This is part of the Fluid Particle Simualtor Application and is a system designed to allow users to \ncustomise the graph by changing the type of graph chown and with their preferences in colour.", font=("Consolas", fieldText)).grid(row=0, column=0, columnspan=2, sticky=W, padx=15, pady=10)

        ctk.CTkLabel(self.aboutWindow, text="Version", font=("Consolas", titleText)).grid(row=1, column=0, padx=15, pady=10)
        ctk.CTkLabel(self.aboutWindow, text="Alterations", font=("Consolas", titleText)).grid(row=1, column=1, padx=15, pady=10)

        n = 8
        ctk.CTkLabel(self.aboutWindow, text="2.3.0", font=("Consolas", fieldText)).grid(row=n-6, column=0, sticky=W, padx=15, pady=10)
        ctk.CTkLabel(self.aboutWindow, text="Addition of the return to Simualtor button and other minor upgrades", font=("Consolas", fieldText)).grid(row=n-6, column=1, sticky=W, padx=15, pady=10)

        ctk.CTkLabel(self.aboutWindow, text="2.2.0", font=("Consolas", fieldText)).grid(row=n-5, column=0, sticky=W, padx=15, pady=10)
        ctk.CTkLabel(self.aboutWindow, text="Creation of Help and About buttons to guide users to the use of this system\nand the system versioning with alterations performed", font=("Consolas", fieldText)).grid(row=n-5, column=1, sticky=W, padx=15, pady=10)

        ctk.CTkLabel(self.aboutWindow, text="2.1.0", font=("Consolas", fieldText)).grid(row=n-4, column=0, sticky=W, padx=15, pady=10)
        ctk.CTkLabel(self.aboutWindow, text="System Reformatting and addition of Graph type and Colour", font=("Consolas", fieldText)).grid(row=n-4, column=1, sticky=W, padx=15, pady=10)

        ctk.CTkLabel(self.aboutWindow, text="2.0.0", font=("Consolas", fieldText)).grid(row=n-3, column=0, sticky=W, padx=15, pady=10)
        ctk.CTkLabel(self.aboutWindow, text="System Integration with Particle Fluid Simualtor and Login Page", font=("Consolas", fieldText)).grid(row=n-3, column=1, sticky=W, padx=15, pady=10)

        ctk.CTkLabel(self.aboutWindow, text="1.0.2", font=("Consolas", fieldText)).grid(row=n-2, column=0, sticky=W, padx=15, pady=10)
        ctk.CTkLabel(self.aboutWindow, text="Minor Bug Fixes - Graph Creation", font=("Consolas", fieldText)).grid(row=n-2, column=1, sticky=W, padx=15, pady=10)    

        ctk.CTkLabel(self.aboutWindow, text="1.0.1", font=("Consolas", fieldText)).grid(row=n-1, column=0, sticky=W, padx=15, pady=10)
        ctk.CTkLabel(self.aboutWindow, text="Minor Bug Fixes - X-axis and Y-axis Radio Button", font=("Consolas", fieldText)).grid(row=n-1, column=1, sticky=W, padx=15, pady=10)

        ctk.CTkLabel(self.aboutWindow, text="1.0.0", font=("Consolas", fieldText)).grid(row=n, column=0, sticky=W, padx=15, pady=10)
        ctk.CTkLabel(self.aboutWindow, text="System Creation", font=("Consolas", fieldText)).grid(row=n, column=1, sticky=W, padx=15, pady=10)

# FUCNTION: Convert RGB values entered by user into a hex code
def rgbToHex(r, g, b):
    try:
        # Try to convert the values into an integer
        r = int(r)
        g = int(g)
        b = int(b)
    except:
        # If there is an error then send an error message and return back
        messagebox.showerror(title="Error", message="Please enter data for rgb")
        return
    # Otherwise check if the values are between 0 and 255 inclusive
    if not(255 >= r >= 0) or not(255 >= g >= 0) or not(255 >= b >= 0):
        # If there is an error then send an error message and return back
        messagebox.showerror(title="Error", message="Please enter data for rgb between 0 and 255")
        return
    global fill
    # If there are no errors then convert it into a hex code using the format key
    fill = '#{:02x}{:02x}{:02x}'.format(r, g, b)
    # Update the colour of the rectangle so that the user is able to see the new colour
    colOut.itemconfig(colourShow, fill=fill)

# FUCNTION: Graph Validaiton Checks
def displayGraph():
    # Check to make sure the user has entered data for all 4 panels (x, y, graph type and rgb)
    if vx.get() == "":
        messagebox.showerror(title="Error", message="Please enter data for x value")
        return
    if vy.get() == "":
        messagebox.showerror(title="Error", message="Please enter data for y value")
        return
    if r.get() == "":
        messagebox.showerror(title="Error", message="Please enter data for type of graph")
        return
    if fill == "":
        messagebox.showerror(title="Error", message="Please enter data for rgb values")
        return

    # The options that the user chose are saved into these respective variables
    xchoice = entities.get(vx.get())
    ychoice = entities.get(vy.get())

    # As per the user's choice of variables, the relevant data is selected and stored into the these variables
    xData = pd.read_csv("particleData.csv", usecols=[xchoice])
    yData = pd.read_csv("particleData.csv", usecols=[ychoice])

    # This is used to produce an output of the graph with the matplotlib library
    if int(r.get()) == 1:
        # Line graph
        plt.plot(xData, yData, color = fill)
    else:
        # Scatter Graph
        plt.scatter(xData, yData, color = fill, marker="x")

    plt.xlabel(xchoice)
    plt.ylabel(ychoice)
    plt.grid()
    plt.show()

# FUNCTION: If the user clicks the go back to simulator button, close the settings window and open the simulator window
def simulator():
    window.destroy()
    filename = "ParticleSimulation.py"
    subprocess.run(["python", filename], check =True)

# Basic GUI formatting for Tkinter
# Basic formatting - creating a window
window = GUIWindow()

titleText = 35
fieldText = 15
btnText = 14

# Values for creating radio buttons in tkinter
vx = tk.StringVar()
vy = tk.StringVar()
r = tk.StringVar()
r.set("")
fill = ""

# Dictionary to store the available entities to display on the x or y axis
entities = {"1" : "Time",
            "2" : "Displacement",
            "3" : "Velocity",
            "4" : "Acceleration"}

# Creating the GUI and adding all features onto it

# Button images (for help and about)
aboutImg = ctk.CTkImage(Image.open("info.png"), size=(30,30))
helpImg = ctk.CTkImage(Image.open("help.png"), size=(30,30))

# ------------------------- INFORMATION PANEL -------------------------
infoFrame = ctk.CTkFrame(window, width = 66, height = 35)
helpButton = ctk.CTkButton(infoFrame, image=helpImg, text="", width=25, height=35, command=window.openHelp).grid(row=0, column=0, padx=3, sticky=W)
aboutButton = ctk.CTkButton(infoFrame, image=aboutImg, text="", width=25, height=35, command=window.openAbout).grid(row=0, column=1, padx=3, sticky=W)
infoFrame.grid(row=0, column=0, sticky=W)

# ------------------------- RETURN TO SIMULATION -------------------------
previous = ctk.CTkButton(window, text="Return to Simulator", command=simulator, height=35, font=("Consolas", btnText)).grid(row=0, column=3, sticky=E)

#------------------------- TITLE -------------------------
settings = ctk.CTkLabel(window, text="Settings", font=("Consolas", 40)) # Header Text
settings.grid(row=1, column=0, columnspan=4, pady=10)

#------------------------- X AXIS FRAME -------------------------
xframe = ctk.CTkFrame(window, border_width=3, border_color='#ffb3ba')

xaxis = ctk.CTkLabel(xframe, text="X Axis", font=("Consolas", titleText)) # Header Text
xaxis.grid(row=0, column=0, columnspan=2, pady=30, padx=15)

# Creating the radio buttons by iterating through the dictionary and producing a radio button per value
for (value, text) in entities.items():
    ctk.CTkRadioButton(xframe, text = text, variable = vx, value = value, font=("Consolas", btnText)).grid(row = value, column = 0, sticky=W, padx=15, pady=5)

xframe.grid(row=3, column=0, padx=10, sticky=W)

#------------------------- Y AXIS FRAME -------------------------
# Creating the y axis Frame with its appropriate widgets
yframe = ctk.CTkFrame(window, width=250, height=300, border_width=3, border_color='#ffffba')
# yframe = tk.Frame(window, highlightbackground="blue", highlightthickness=2)

yaxis = ctk.CTkLabel(yframe, text="Y axis", font=("Consolas", titleText)) # Header Text
yaxis.grid(row=0, column=0, columnspan=2, pady=30, padx=15)

for (value, text) in entities.items():
    ctk.CTkRadioButton(yframe, text = text, variable = vy, value = value, font=("Consolas", btnText)).grid(row = value, column = 0, sticky=W, padx=15, pady=5)

yframe.grid(row=3, column=1, padx=10)

#------------------------- GRAPH TYPE FRAME -------------------------
plotframe = ctk.CTkFrame(window, width=250, height=300,  border_width=3, border_color='#baffc9')

graphType = ctk.CTkLabel(plotframe, text="Graph Type", font=("Consolas", titleText)) # Header Text
graphType.grid(row=0, column=0, pady=30, padx=15)

line = ctk.CTkRadioButton(plotframe, text="Line Graph", variable = r, value = 1, font=("Consolas", btnText))
line.grid(row=1, column=0, sticky=W, padx=100, pady=5)

scatter = ctk.CTkRadioButton(plotframe, text="Scatter Graph", variable = r, value = 2, font=("Consolas", btnText))
scatter.grid(row=2, column=0, sticky=W, padx=100, pady=5)
plotframe.grid(row = 3, column = 2, padx=10)

#------------------------- COLOUR SELECTION FRAME -------------------------
colorframe = ctk.CTkFrame(window, width=250, height=300, border_width=3, border_color='#bae1ff')

colorText = ctk.CTkLabel(colorframe, text="Colour", font=("Consolas", titleText)) # Header Text
colorText.grid(row=0, column=0, columnspan=2, pady=10)

Red = ctk.CTkLabel(colorframe, text="Red", text_color='#fc4242', font=("Consolas", fieldText))
Red.grid(row=1, column=0, padx=5, pady=5)
RedBox = ctk.CTkEntry(colorframe, font=("Consolas", 13), width=40)
RedBox.grid(row=1, column=1, padx=20, sticky=W)

Green = ctk.CTkLabel(colorframe, text="Green", text_color='#5cfa7c', font=("Consolas", fieldText))
Green.grid(row=2, column=0, padx=5, pady=5)
GreenBox = ctk.CTkEntry(colorframe, font=("Consolas", 13), width=40)
GreenBox.grid(row=2, column=1, padx=20, sticky=W)

Blue = ctk.CTkLabel(colorframe, text="Blue", text_color='#34b4eb', font=("Consolas", fieldText))
Blue.grid(row=3, column=0, padx=5, pady=5)
BlueBox = ctk.CTkEntry(colorframe, font=("Consolas", 13), width=40)
BlueBox.grid(row=3, column=1, padx=20, sticky=W)

colOutBtn = ctk.CTkButton(colorframe, text="See Colour", command=lambda: rgbToHex(RedBox.get(), GreenBox.get(), BlueBox.get()), font=("Consolas", btnText), width=80, height=30)
colOutBtn.grid(row=4, column=0, pady=10, padx=10)

colOut = Canvas(colorframe, width=50, height=30, bg='#2b2b2b')
colOut.grid(row=4, column=1, padx=20, sticky=W)
colourShow = colOut.create_rectangle(0, 0, 90, 50, fill="white")

colorframe.grid(row = 3, column = 3, padx=10)

#------------------------- END BUTTON -------------------------
# The end button to destroy the window once clicked so that the GUI can be ended and a graph can be produced
end = ctk.CTkButton(window, text="Create Graph", height = 40, width = 200, command=lambda: displayGraph(), font=("Consolas", btnText+3))
end.grid(row=4, column=0, columnspan = 9, pady=30)

window.eval('tk::PlaceWindow . center')

window.mainloop()