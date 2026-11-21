from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk
window=Tk()
window.title("My Photo Album")
window.config(bg='white')
window.geometry("450x500")
titlelabel=Label(window,text="My photo album",font=("arial",20,"bold"),bg="blue",fg="white",width=20)
titlelabel.pack(pady=15)
