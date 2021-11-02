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


# row 0
l0 = Label(root, text="browse image")
l0.grid(row=0, column=0)

LST_Types = [("images" , [".png", ".jpg", ".jpeg"])]
e01 = filedialog.askopenfilename(initialdir = "C:", title = "Select a File", filetypes = LST_Types)
l01 = Label(root, text=e01)
l01.grid(row=0, column=1, padx=5, pady=5)


root.mainloop()