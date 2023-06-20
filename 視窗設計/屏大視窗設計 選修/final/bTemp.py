from tkinter import *
from PIL import Image
win = Tk()
win.title("beach")
win.geometry("1340x815")

# background method2
canvas = Canvas(win, width=1340, height=815)
canvas.place(x=0, y=0)

Back = PhotoImage(file="terrariaBG.png")
canvas.create_image(0, 0, anchor=NW, image=Back)


humancan=PhotoImage(file="Rright.png")
canvas.create_image(350, 530, anchor=NW, image=humancan)


win.mainloop()
