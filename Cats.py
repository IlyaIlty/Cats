from tkinter import *
from tkinter import ttk
from PIL import ImageTk
import requests
from io import BytesIO

#from PyQt5.QtWidgets.QWidget import window
#from spyder_kernels.utils.iofuncs import load_image

Allowed_tags = ['sleep','play','jump','fight','black','white','siames','cute',]

def load_image(url):
    try:
        responce = requests.get(url)
        responce.raise_for_status()
        image_data = BytesIO(responce.content)
        img = Image.open(image_data)
        img.thumbnail((600,480), Image.Resampling.LANCZOS)
        return ImageTk.PhotoImage(img)
    except Exception as e:
        print(f'Проищошла ошибка: {e}')
        return None


def open_new_window():
    tag = tag_combobox.get()
    url_tag = f"https://cataas.com/cat/{tag}" if tag else "https://cataas.com/cat"
    img = load_image(url_tag)

    if img:
        new_window = Toplevel()
        new_window.title('Картинка с котиком')
        new_window.geometry('600x480')
        label = Label(new_window, image=img)
        label.pack()
        label.image = img

def exit():
    window.destroy()


window = Tk()
window.title('Cats!')
window.geometry('600x520')


menu_bar = Menu(window)
window.config(menu=menu_bar)

file_menu = Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label='Файл', menu=file_menu)
file_menu.add_command(label='Загрузить фото', command=open_new_window)
file_menu.add_separator()
file_menu.add_command(label='Выход', command=exit)

url = 'https://cataas.com/cat'

tag_label = Label(text='Выбери тэг')
tag_label.pack()

tag_combobox = ttk.Combobox(values=Allowed_tags)
tag_combobox.pack()

load_button = Button('загрузить по тэгу', command=open_new_window)
load_button.pack()

window.mainloop()

