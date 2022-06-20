# import tkinter as tk
from tkinter import *

win = Tk()  # 建立主視窗
win.title("過河遊戲")

# Button
btn0 = Button(text="wolf")
btn1 = Button(text="sheep")
btn2 = Button(text="vegetable")
btn3 = Button(text="people")

btn0.config(bg="white")
btn1.config(bg="white")
btn2.config(bg="white")
btn3.config(bg="white")


btn0.config(width=10, height=5)
btn1.config(width=10, height=5)
btn2.config(width=10, height=5)
btn3.config(width=10, height=5)


btn0.pack()  # 布局
btn1.pack()  # 布局
btn2.pack()  # 布局
btn3.pack()  # 布局


# 大小
win.geometry("")  # 左右 x 上下
win.minsize(width=500, height=300)  # 最小視窗
# win.minsize(width=1920,height=1080)#最大
win.resizable(False, False)  # 不給縮放

# 背景顏色
win.config(bg="skyblue")

# 透明
# win.attributes("-alpha",0.5)


win.mainloop()  # 視窗持續開啟 = system("pause")
