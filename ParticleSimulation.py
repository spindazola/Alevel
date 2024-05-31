# Partha Khanna 
# Particle Motion Simulator
# A Level Computer Science Non-examined Project
# Python 3.11.1
# Module 2: Simulation
# Version 2.1.2

# Libraries Imported
import pygame
import pygame_widgets
from pygame_widgets.slider import Slider
from pygame_widgets.textbox import TextBox
from pygame_widgets.button import Button
from pygame_widgets.dropdown import Dropdown
import numpy as np
import csv, os, math, subprocess
import time as ti
import webbrowser

# Declaring the particle class
class Particle:
    # initialising all variables
    def __init__(self, pos, vel, acc, radius, density):
        self.pos = pos
        self.vel = vel
        self.acc = acc
        self.radius = radius
        self.density = density
        
    # updating the position and velocity as per the acceleration
    def update(self, fluid, dt):
        fluidForce = Fluid.drag_force(self)
        self.acc[1] = (4/3 * np.pi * (self.radius**3) * self.density) - fluidForce
        self.vel[1] += fluidForce / self.density * dt
        self.pos[1] += self.vel[1] * dt
        
class Fluid:
    # Create a Fluid Class and initialise variables
    def __init__(self, viscosity, density):
        self.viscosity = viscosity
        self.density = density
    
    # Fluid Drag force
    def drag_force(self, particle):
        re = self.reynolds_number(particle)
        if re < 2300:
            return 6 * math.pi * self.viscosity * particle.radius * particle.vel[1]
        else:
            return 0.44 * math.pi * particle.radius ** 2 * self.density * (particle.vel[1]**2)

    # Fluid Reynolds Number
    def reynolds_number(self, particle):
        return particle.density * particle.vel[1] * particle.radius / self.viscosity

# PROCEDURE: open csv file with all datapoints
def downloadFile():
    file = "particleData.csv" # File to open
    path = "C:\\Program Files\\Microsoft Office\\root\\Office16\\EXCEL.EXE" # Path to Excel application on Windows
    os.system(f'"{path}" "{os.path.abspath(file)}"') # Open the file in excel locally

# PROCEDURE: open the graph if view graph button is clicked and close the simulator
def graph():
        pygame.quit()
        ti.sleep(0.25)
        filename = "DataAnalysis.py"
        subprocess.run(["python", filename])

# Finding the drag force and using Newton's Second Law to find accel.
def accel(pMass, pRadius, fDensity, viscosity, vel, reynolds, pDensity):
    # grad = -3 * np.pi * viscosity * pRadius * reynolds * np.gradient(np.linalg.norm(vel[1])**2, vel[1])
    # curl = 2 * np.pi * np.cross(vel[1], np.array([0, 0, 1]))
    pMass = 4/3 * math.pi * pRadius**3 * pDensity
    if reynolds > 2500:
        # Drag Force = Drag due to viscosity (stokes' law) + Drag due to fluid (half x Drag coefficient) x Area of impact x velocity squared
        F_drag = (0.5 * 0.45 * fDensity * (np.pi * (pRadius)**2) * (vel[1])**2) # drag force on particle from Fluid Drag force
        # Note that the drag coefficient for a sphere is 0.45 according to University of Florida
    else:
        F_drag = (6 * np.pi * pRadius * viscosity * vel[1]) # Drag Force = Drag due to viscosity (stokes' law)
    F_net = (pMass * 9.81) - F_drag # net force on particle
    return F_net / pMass

# Function to invert paused when the button to play/pause is clicked
def invert(paused):
    paused = not paused

# Initialize Pygame
pygame.init()

# Set up the window
width = 1500
height = 700
window = pygame.display.set_mode((width, height))
pygame.display.set_caption("Particle in Fluid")

# Creating Fonts through a downloaded Google Fonts rather than using REST API (compilation)
fontA = pygame.font.Font('SourceSansPro-SemiBold.ttf', 30)
fontB = pygame.font.Font('SourceSansPro-SemiBold.ttf', 20)
fontC = pygame.font.Font('SourceSansPro-SemiBold.ttf', 19)

# Set up the particle
pRadius = 5
pos = [337, 50]
disp = [0, 0]
vel = [0, 0]
acc = [0, 0]
pDensity = 1
pMass = 4/3 * np.pi * pRadius**3 * pDensity

displacement = 0
velocity = 0
acceleration = 0

# Set up the fluid
fDensity = 1
viscosity = 0.250
# fluid = Fluid(0.250, 0.1)

# Set up the simulation
paused = True
timeSim = 0
sf = 3
scale = 10**sf

# ------------------------- SIMULATION TEXT -------------------------
expText = fontA.render("Experiment", True, (0, 0, 0))
expTextRect = expText.get_rect()
expTextRect.center = (337, 20)

paraText = fontA.render("Alter Parameters", True, (0, 0, 0))
paraTextRect = paraText.get_rect()
paraTextRect.center = (835, 20)

infoText = fontA.render("Information", True, (0, 0, 0))
infoTextRect = infoText.get_rect()
infoTextRect.center = (1275, 20)

viscText = fontB.render("Dynamic Viscosity in Pascal Seconds (Pas)", True, (0, 0, 0))
viscTextRect = viscText.get_rect()
viscTextRect.center = (835, 85)

pDensityText = fontB.render("Particle Density in g/(cm^3)", True, (0, 0, 0))
pDensityTextRect = pDensityText.get_rect()
pDensityTextRect.center = (835, 200)

pRadiusText = fontB.render("Particle Radius in cm", True, (0, 0, 0))
pRadiusTextRect = pRadiusText.get_rect()
pRadiusTextRect.center = (835, 315)

fDensityText = fontB.render("Fluid Density in g/(cm^3)", True, (0, 0, 0))
fDensityTextRect = fDensityText.get_rect()
fDensityTextRect.center = (835, 430)

scaleText = fontB.render("Scale", True, (0, 0, 0))
scaleTextRect = scaleText.get_rect()
scaleTextRect.center = (835, 545)

# ------------------------- SIMULATION SLIDERS -------------------------
viscSlider = Slider(window, 680, 100, 300, 15, min=0.001, max=5, step=0.001, color=(230, 131, 73))
viscOutput = TextBox(window, 810, 125, 45, 30, fontSize=20)
viscOutput.disable()
viscSlider.setValue(viscosity) 

pDensitySlider = Slider(window, 680, 220, 300, 15, min=1, max=20, step=0.01, color=(230, 131, 73))
pDensityOutput = TextBox(window, 810, 245, 45, 30, fontSize=20)
pDensityOutput.disable()
pDensitySlider.setValue(pDensity)

pRadiusSlider = Slider(window, 680, 340, 300, 15, min=1, max=40, step=5, color=(230, 131, 73))
pRadiusOutput = TextBox(window, 810, 365, 45, 30, fontSize=20)
pRadiusOutput.disable()
pRadiusSlider.setValue(pRadius)

fDensitySlider = Slider(window, 680, 465, 300, 15, min=1, max=1.3, step=0.01, color=(230, 131, 73))
fDensityOutput = TextBox(window, 810, 485, 45, 30, fontSize=20)
fDensityOutput.disable()
fDensitySlider.setValue(fDensity)

scaleSlider = Slider(window, 680, 570, 300, 15, min=1, max=6, step=1, color=(230, 131, 73))
scaleOutput = TextBox(window, 810, 605, 45, 30, fontSize=20)
scaleOutput.disable()
scaleSlider.setValue(sf)

# ------------------------- SIMULATION CONTROL -------------------------
# pause and play button and restart button
pauseButton = Button(window, 100, 650, 200, 50, text="Play/Pause", inactiveColour=(255, 0, 0), hoverColour=(0, 255, 0), pressedcolour=(0, 0, 255), radius=10, onClick=lambda: invert(paused))
restartButton = Button(window, 305, 650, 200, 50, text="Restart", inactiveColour=(255, 0, 0), hoverColour=(0, 255, 0), pressedcolour=(0, 0, 255), radius=10, onClick=lambda: invert(paused))

# button to open the csv file of all datapoints locally to download
downloadRect = pygame.Rect(640, 650, 205, 45)
downloadText = fontC.render("View experiment data", True, pygame.Color("white"))

# Button to open the graph settings page
graphRect = pygame.Rect(875, 650, 112, 45)
graphText = fontC.render("View Graph", True, pygame.Color("white"))

# ------------------------- INFORMATION PANEL CONTROL -------------------------
# Extra Buttons for Information Panel
OIRect = pygame.Rect(1100, 650, 120, 45) # Open Image
FOMRect = pygame.Rect(1300, 650, 135, 45)
OIText = fontC.render("Open Image", True, pygame.Color("white")) # Find Out more
FOMText = fontC.render("Find Out More", True, pygame.Color("white"))
# Create a Dropdown panel for the variable entities to inform the user
info = Dropdown(window, 1050, 50, 420, 50, name="Entities", choices=["Viscosity", "Density and Drag Force", "Reynolds Number", "Vector Calculus"])

# Information panel Images
reynoldsImg = pygame.image.load("Reynolds Number.png") # Image path
reynoldsImg = pygame.transform.scale(reynoldsImg, (350,520)) # Image resizing
reynoldsImgRect = reynoldsImg.get_rect() # Image placement
reynoldsImgRect.center = (1250, 375) # Image relocation on window

viscImg = pygame.image.load("Viscosity.png")
viscImg = pygame.transform.scale(viscImg, (350,520))
viscImgRect = viscImg.get_rect()
viscImgRect.center = (1250, 375)

densityImg = pygame.image.load("Density.png")
densityImg = pygame.transform.scale(densityImg, (375,400))
densityImgRect = densityImg.get_rect()
densityImgRect.center = (1260, 400)

vectImg = pygame.image.load("VectorCalculus.png")
vectImg = pygame.transform.scale(vectImg, (300,520))
vectImgRect = vectImg.get_rect()
vectImgRect.center = (1250, 380)

dt = 0 # variable to act as a stopwatch using the current time
# Set up CSV writer
with open('particleData.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Displacement', 'Velocity', 'Acceleration', 'Time'])
    # Main loop
    run = True
    clock = pygame.time.Clock()
    while run:
        # Handle events
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                pygame.quit()
                run = False
                exit()
            elif event.type == pygame.KEYDOWN:
                # On a key press...
                if event.key == pygame.K_SPACE:
                    # of Space bar - Start simulation
                    paused = False
                    tStart = ti.time()
                if event.key == pygame.K_p:
                    # p key to pause the simulation at any point
                    paused = not paused
                if event.key == pygame.K_UP:
                    # of up arrow key - restart simulation
                    # all variable reinitialised
                    pos = [337, 50]
                    disp = [0, 0]
                    vel = [0, 0]
                    acc = [0, 0]
                    displacement = 0
                    velocity = 0
                    acceleration = 0
                    tStart = ti.time()
                    dt = 0
            elif event.type == pygame.MOUSEBUTTONDOWN:
                # check where mouse cursor is and if it in in one of these locations the the following functions are executed
                if downloadRect.collidepoint(event.pos):
                    downloadFile() # Download button - download file
                if graphRect.collidepoint(event.pos):
                    graph() # Graph View button - Open Data Analysis Settings Page
                if OIRect.collidepoint(event.pos):
                    # Open Image button depending on the entity selected
                    if info.getSelected() == "Reynolds Number":
                        url = "https://raw.githubusercontent.com/PKhanna9/studious-rotary-phone/main/Reynolds%20Number.png"
                    elif info.getSelected() == "Viscosity":
                        url = "https://raw.githubusercontent.com/PKhanna9/studious-rotary-phone/main/Viscosity.png"
                    elif info.getSelected() == "Density and Drag Force":
                        url = "https://raw.githubusercontent.com/PKhanna9/studious-rotary-phone/main/Density.png"
                    elif info.getSelected() == "Vector Calculus":
                        url = "https://raw.githubusercontent.com/PKhanna9/studious-rotary-phone/main/VectorCalculus.png"
                    webbrowser.open_new_tab(url) # opens in the web browser
                if FOMRect.collidepoint(event.pos):
                    # Same for this but this is for more information
                    if info.getSelected() == "Reynolds Number":
                        url = "https://www.simscale.com/docs/simwiki/numerics-background/what-is-the-reynolds-number/"
                    elif info.getSelected() == "Viscosity":
                        url = "https://www.simscale.com/docs/simwiki/cfd-computational-fluid-dynamics/what-is-viscosity/"
                    elif info.getSelected() == "Density and Drag Force":
                        url = "https://courses.lumenlearning.com/suny-physics/chapter/5-2-drag-forces/"
                    elif info.getSelected() == "Vector Calculus":
                        url = "https://web.mit.edu/wwmath/vectorc/summary.html"
                    webbrowser.open_new_tab(url)

        if not paused:
            dt += 0.016 # Time increment

            timeSim = pygame.time.get_ticks()

            reynolds = (fDensity * velocity * displacement)/(viscosity)

            # Update particle velocity based on fluid density
            acc[1] = accel(pMass, pRadius, fDensity, viscosity, vel, reynolds, pDensity)
            dv = vel[1]
            #dt = ti.time() - tStart
            vel[1] += acc[1] * dt

            # Update particle position based on velocity
            disp[1] += 0.5 * (dv + vel[1]) * dt
            pos[1] += (0.5 * (dv + vel[1]) * dt)/scale

            displacement = np.array(disp)
            displacement = np.linalg.norm(displacement)

            velocity = np.array(vel)
            velocity = np.linalg.norm(velocity)

            acceleration = np.array(acc)
            acceleration = np.linalg.norm(acceleration)

            if pos[1] >= (600 - pRadius):
                paused = True

            # Write particle data to CSV
            writer.writerow([displacement, velocity, acceleration, dt])

            viscosity = viscSlider.getValue()
            pDensity = pDensitySlider.getValue()
            pRadius = pRadiusSlider.getValue()
            sf = scaleSlider.getValue()
            scale = 10**sf
            fDensity = fDensitySlider.getValue()/1000
            
        # ------------------------- DRAW ALL FEATURES -------------------------
        # Draw particle
        window.fill((255, 255, 255))
        pygame.draw.rect(window, (75, 193, 239), (139, 50, 397, 549))
        pygame.draw.circle(window, (255, 0, 0), [int(pos[0]), int(pos[1])], pRadius)
        pygame.draw.circle(window, (0, 0, 0), [int(pos[0]), int(pos[1])], pRadius, 2)

        # Draw play/pause button
        if paused:
            pygame.draw.rect(window, (0, 0, 0), (9, 9, 47, 47), border_radius=4)
            pygame.draw.rect(window, (255, 0, 0), (10, 10, 45, 45), border_radius=4)
            pygame.draw.rect(window, (0, 0, 0), (22, 17, 9, 32), border_radius=2)
            pygame.draw.rect(window, (0, 0, 0), (35, 17, 9, 32), border_radius=2)
            pygame.draw.rect(window, (255, 255, 255), (23, 18, 7, 30), border_radius=2)
            pygame.draw.rect(window, (255, 255, 255), (36, 18, 7, 30), border_radius=2)
        else:
            pygame.draw.rect(window, (0, 0, 0), (9, 9, 47, 47), border_radius=4)
            pygame.draw.rect(window, (0, 255, 0), (10, 10, 45, 45), border_radius=4)
            pygame.draw.polygon(window, (150, 150, 150), [(25, 20), (25, 40), (40, 30)])
            
        # Draw separator lines and other shapes
        pygame.draw.line(window, (0, 0, 0), (625, 0), (625, 700), 4)
        pygame.draw.line(window, (0, 0, 0), (1025, 0), (1025, 700), 4)
        pygame.draw.line(window, (3, 104, 190), (137, 50), (137, 600), 5)
        pygame.draw.line(window, (3, 104, 190), (537, 50), (537, 600), 5)
        pygame.draw.line(window, (3, 104, 190), (137, 600), (537, 600), 5)

        # Download and View graph buttons
        pygame.draw.rect(window, (0, 0, 0), downloadRect)
        window.blit(downloadText, (downloadRect.x + 10, downloadRect.y + 10))
        pygame.draw.rect(window, (0,0,0), graphRect)
        window.blit(graphText, (graphRect.x + 10, graphRect.y + 10))

        # Place all Text onto Window
        window.blit(expText, expTextRect)
        window.blit(paraText, paraTextRect)
        window.blit(infoText, infoTextRect)
        window.blit(viscText, viscTextRect)
        window.blit(pDensityText, pDensityTextRect)
        window.blit(pRadiusText, pRadiusTextRect)
        window.blit(fDensityText, fDensityTextRect)
        window.blit(scaleText, scaleTextRect)

        # Set the Lable under the slider to the value in the slider
        viscOutput.setText(viscSlider.getValue())
        pDensityOutput.setText(pDensitySlider.getValue())
        pRadiusOutput.setText(pRadiusSlider.getValue())
        fDensityOutput.setText(fDensitySlider.getValue())
        scaleOutput.setText(scaleSlider.getValue())

        # Buttons for Open Image and Find out more
        if info.getSelected() == "Reynolds Number":
            pygame.draw.rect(window, (0,0,0), OIRect)
            pygame.draw.rect(window, (0,0,0), FOMRect)
            window.blit(OIText, (OIRect.x + 10, OIRect.y + 10))
            window.blit(FOMText, (FOMRect.x + 10, FOMRect.y + 10))
            window.blit(reynoldsImg, reynoldsImgRect)
        elif info.getSelected() == "Viscosity":
            pygame.draw.rect(window, (0,0,0), OIRect)
            pygame.draw.rect(window, (0,0,0), FOMRect)
            window.blit(OIText, (OIRect.x + 10, OIRect.y + 10))
            window.blit(FOMText, (FOMRect.x + 10, FOMRect.y + 10))
            window.blit(viscImg, viscImgRect)
        elif info.getSelected() == "Density and Drag Force":
            pygame.draw.rect(window, (0,0,0), OIRect)
            pygame.draw.rect(window, (0,0,0), FOMRect)
            window.blit(OIText, (OIRect.x + 10, OIRect.y + 10))
            window.blit(FOMText, (FOMRect.x + 10, FOMRect.y + 10))
            window.blit(densityImg, densityImgRect)
        elif info.getSelected() == "Vector Calculus":
            pygame.draw.rect(window, (0,0,0), OIRect)
            pygame.draw.rect(window, (0,0,0), FOMRect)
            window.blit(OIText, (OIRect.x + 10, OIRect.y + 10))
            window.blit(FOMText, (FOMRect.x + 10, FOMRect.y + 10))
            window.blit(vectImg, vectImgRect)

        # Update the display
        pygame.display.flip()
        pygame_widgets.update(events)
        pygame.display.update()

        # Set the frame rate
        clock.tick(60)


# Quit Pygame
pygame.quit()