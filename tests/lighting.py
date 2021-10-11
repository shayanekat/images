""" 
    shayanekat
    
    test script for managing light
"""

from tkinter import *
from PIL import Image
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
    for i in range(z.shape[0]):
        for j in range(z.shape[1]):
            for k in range(z.shape[2]):
                nv = (z[i, j, k]*lum)//50
                if nv <= 255:
                    z[i, j, k] = nv
                else:
                    z[i, j, k] = 255
    
    # create new image
    New = np.array(z, dtype=np.uint8)
    img = Image.fromarray(New)
    img.save("processed_images\\lighter.png")

# %% FRONTEND
root = Tk()
root.title("lighting")

l = Label(root, text="slider to select lighting percentage")
l.pack(padx=5, pady=5)

s = Scale(root, from_=0, to=100, orient=HORIZONTAL)
s.pack(padx=5, pady=5)

b = Button(root, text="change lighting", command=light)
b.pack(padx=5, pady=5)

root.mainloop()