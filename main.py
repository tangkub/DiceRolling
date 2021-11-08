# DiceRolling

# Import module
import tkinter # making GUI
from tkinter import ttk
from PIL import Image, ImageTk # operating images in UI
import random # generating random numbers

# Generate main window
GUI = tkinter.Tk()
GUI.geometry('400x400') # window size
GUI.title('Dice Rolling') # window title

# Set up label
f1 = ("Century 16 bold italic") # set up font type
l0 = ttk.Label(GUI, text='') # add blank label
l0.pack() # attach label

l1 = ttk.Label(GUI, text="Let's roll!", font=f1) # add heading label
l1.pack() # attach label

# Set up label for image
# choice to random dice
dice = ['Dice1.png', 'Dice2.png', 'Dice3.png',
        'Dice4.png', 'Dice5.png', 'Dice6.png']

# Get dice image
dice_img = ImageTk.PhotoImage(Image.open('cover.jpg'))  # open image file
l3 = ttk.Label(GUI, image=dice_img) # generate label for image
l3.image = dice_img # add image to label
l3.pack(expand=True) # attach label

# Function: DiceRolling
def DiceRolling():
    choice = random.choice(dice) # random image
    dice_img = ImageTk.PhotoImage(Image.open(choice)) # open image
    l3.configure(image=dice_img) # update image
    l3.image = dice_img # generate label for image

# Add button to activate function
b1 = ttk.Button(GUI, text='Roll the dice', command=DiceRolling)
b1.pack(expand=True)

GUI.mainloop() # keep window open