""" 
    shayanekat
    
    test script for managing light
"""

from PIL import Image
from tkinter import *
import numpy as np

# %% BACKEND
# function
def light():
    """
        main function for light managing
    """
    # creation de la matrice
    img = Image.open("tests\\input.png")
    z = np.array(img)
    
    # extract light percentage
    lum = int(s.get())
    
    # compute new values
    z = (z*lum)//50
    
    # create new image

# %% FRONTEND
root = Tk()
root.title("lighting")

l = Label(root, text="slider to select lighting percentage")
l.pack(padx=5, pady=5)

s = Scale(root, from_=0, to=100, orient=HORIZONTAL)
s.pack(padx=5, pady=5)

b = Button(root, text="change lighting")
b.pack(padx=5, pady=5)

root.mainloop()