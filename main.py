""" 
Shayanekat

main script that will contain all algorithms of image processing.
"""

from tkinter import *
from tkinter import filedialog
from PIL import Image
import numpy as np

# %% BACKEND

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

c1 = Checkbutton(root,text="allow resizing")



root.mainloop()