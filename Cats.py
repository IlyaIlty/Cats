from tkinter import *
from PIL import ImageTk
import requests
from io import BytesIO

from PyQt5.QtWidgets.QWidget import window
from spyder_kernels.utils.iofuncs import load_image

window = Tk()
window.title('Cats!')
window.geometry('600x400')

label = Label()
label.pack()

url = 'https://cataas.com/cat'
img = load_image(url)

if img:
    label.config(image=img)
    label.image = img

window.mainloop()

