from tkinter import *
from PIL import ImageTk
import requests
from io import BytesIO

from PyQt5.QtWidgets.QWidget import window
from spyder_kernels.utils.iofuncs import load_image


def loade_image():
    try:
        responce = requests.get(url)
        responce.raise_for_status()
        image_data = BytesIO(responce.content)
        img = Image.open(image_data)
        return ImageTk.PhotoImage(img)
    except Exception as e:
        print(f'Проищошла ошибка: {e}')
        return None


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

