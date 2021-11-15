""" 
    shayanekat
    
    test script for some filtering
"""

from tkinter import *
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt

# %% BACKEND
# define variables
img = Image.open("tests\\input.png")
z = np.array(img)

# functions
def display(nz):
    plt.imshow(nz)
    plt.show()

def red():
    nz = z
    nz[:, :, 1] = np.zeros((nz.shape[0], nz.shape[1]))
    nz[:, :, 2] = np.zeros((nz.shape[0], nz.shape[1]))
    
    # display
    display(nz)
    
def green():
    nz = z
    nz[:, :, 0] = np.zeros((nz.shape[0], nz.shape[1]))
    nz[:, :, 2] = np.zeros((nz.shape[0], nz.shape[1]))
    
    # display
    display(nz)

def blue():
    nz = z
    nz[:, :, 0] = np.zeros((nz.shape[0], nz.shape[1]))
    nz[:, :, 1] = np.zeros((nz.shape[0], nz.shape[1]))
    
    # display
    display(nz)

def redgreen():
    nz = z
    nz[:, :, 2] = np.zeros((nz.shape[0], nz.shape[1]))
    
    # display
    display(nz)
    
def bluegreen():
    nz = z
    nz[:, :, 0] = np.zeros((nz.shape[0], nz.shape[1]))
    
    # display
    display(nz)

def bluered():
    nz = z
    nz[:, :, 1] = np.zeros((nz.shape[0], nz.shape[1]))
    
    # display
    display(nz)

def negative1():
    nz = z
    temp = nz[:, :, 0]
    nz[:, :, 0] = nz[:, :, 1]
    nz[:, :, 1] = nz[:, :, 2]
    nz[:, :, 2] = temp

    display(nz)

def negative2():
    nz = -z + 255
    display(nz)
    

# %% FRONTEND
# configuration
root = Tk()
root.title("lighting")

# first row : 1 color canal
br = Button(root, text="red canal", command=red)
br.grid(row=0, column=0, padx=5, pady=5)

bg = Button(root, text="green canal", command=green)
bg.grid(row=0, column=1, padx=5, pady=5)

bb = Button(root, text="blue canal", command=blue)
bb.grid(row=0, column=2, padx=5, pady=5)

# second row : 2 color canals
brg = Button(root, text="red-green canals", command=redgreen)
brg.grid(row=1, column=0, padx=5, pady=5)

bbg = Button(root, text="blue-green canals", command=bluegreen)
bbg.grid(row=1, column=1, padx=5, pady=5)

brb = Button(root, text="red-blue canals", command=bluered)
brb.grid(row=1, column=2, padx=5, pady=5)

# third row : negative
bn1 = Button(root, text="negative v1", command=negative1)
bn1.grid(row=2, column=0, padx=5, pady=5)

bn2 = Button(root, text="negative v2", command=negative2)
bn2.grid(row=2, column=1, padx=5, pady=5)

# fourth row : mirror
bmh = Button(root, text="horizontal mirror")
bmh.grid(row=3, column=0, padx=5, pady=5)

bmv = Button(root, text="vertical mirror")
bmv.grid(row=3, column=1, padx=5, pady=5)

bm = Button(root, text="mirror")
bm.grid(row=3, column=2, padx=5, pady=5)

# mainloop
root.mainloop()