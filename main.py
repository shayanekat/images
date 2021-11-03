""" 
Shayanekat

main script that will contain all algorithms of image processing.
"""

from tkinter import *
from tkinter import filedialog
from PIL import Image
import numpy as np
from numpy.core.fromnumeric import var

# %% BACKEND
# define variables
z = []

# functions
def main():
    """
    main function
    """
    global z
    
    # creation de la matrice
    img = Image.open("tests\\input.png")
    z = np.array(img)
    
    if bool(var2.get()):
        resize()
    
    if bool(var4.get()):
        light()
    
    New = np.array(z, dtype=np.uint8)
    img = Image.fromarray(New)
    img.save("processed_images\\processed.png")
    
def resize():
    """
        Function to resize an image
    """
    global z
    
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
    for i in dx[-1::-1]:
        z = np.delete(z, int(i), 0)
    for i in dy[-1::-1]:
        z = np.delete(z, int(i), 1)

def light():
    """
        main function for light managing
    """
    global z
    
    # extract light percentage
    lum = int(s3.get())
    
    # compute new values
    for i in range(z.shape[0]):
        for j in range(z.shape[1]):
            for k in range(z.shape[2]):
                nv = (z[i, j, k]*lum)//50
                if nv <= 255:
                    z[i, j, k] = nv
                else:
                    z[i, j, k] = 255

# %% FRONTEND
root = Tk()
root.title("image processing")


# row 0 : image browser
l0 = Label(root, text="browse image")
l0.grid(row=0, column=0)

LST_Types = [("images" , [".png", ".jpg", ".jpeg"])]
e01 = filedialog.askopenfilename(initialdir = "C:", title = "Select a File", filetypes = LST_Types)
l01 = Label(root, text=e01)
l01.grid(row=0, column=1, padx=5, pady=5)


# row 1 : resizing
l1 = Label(root, text="enter an image size that is lower than input image size")
l1.grid(row=1, column=0, padx=5, pady=5)

e1 = Entry(root)
e1.grid(row=1, column=1, padx=5, pady=5)


# row 2 : resizing checkbox
var2 = IntVar()
c2 = Checkbutton(root, text="allow resizing", variable=var2)
c2.grid(row=2, column=1, padx=5, pady=5)


# row 3 : lighting
l3 = Label(root, text="slider to select lighting percentage")
l3.grid(row=3, column=0, padx=5, pady=5)

s3 = Scale(root, from_=0, to=100, orient=HORIZONTAL)
s3.grid(row=3, column=1, padx=5, pady=5)


# row 4 : lighting checkbox
var4 = IntVar()
c4 = Checkbutton(root, text="allow lighting", variable=var4)
c4.grid(row=4, column=1, padx=5, pady=5)


# row 5 : button
b5 = Button(root, text="process image", command=main)
b5.grid(row=5, column=1, padx=5, pady=5)


root.mainloop()