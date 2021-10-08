""" 
Shayanekat

test script for resizing an image (only reducing it's size).
"""

from tkinter import *
from PIL import Image
import numpy as np

# %% BACKEND
# functions
def resize():
    """
        Function to resize an image
    """
    # creation de la matrice
    img = Image.open("tests\\input.png")
    z = np.array(img)
    
    # extract new size from input
    try:
        x, y = str(e1.get()).split("x")
        x, y = int(x), int(y)
        
        if x > z.shape[0] and y > z.shape[1]: # too high size case
            print("Enter size that is less than 512x512")
            return 0
        
    except ValueError: # not number case
        print("Enter two numbers by format 512x512")
        return 0
    
    # compute lines and column to remove
    dx = np.linspace(0, z.shape[0]-1, z.shape[0]-x)
    dy = np.linspace(0, z.shape[1]-1, z.shape[1]-y)
    
    # remove the lines and columns
    print(z.shape)
    for i in dx[-1::-1]:
        z = np.delete(z, int(i), 0)
    for i in dy[-1::-1]:
        z = np.delete(z, int(i), 1)
    
    # create new image and save it
    New = np.array(z, dtype=np.uint8)
    img = Image.fromarray(New)
    img.save("processed_images\\resized.png")

# %% FRONTEND
root = Tk()
root.title("resize image")


l1 = Label(root, text="Input image is an image of sphere of size 512x512. Enter below the new size that must be less than 512x512")
l1.pack(padx=5, pady=5)

e1 = Entry(root)
e1.pack(padx=5, pady=5)

b = Button(root, text="resize", command=resize)
b.pack(padx=5, pady=5)


root.mainloop()