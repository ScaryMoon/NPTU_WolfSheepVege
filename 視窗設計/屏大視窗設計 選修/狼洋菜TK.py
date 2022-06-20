from tkinter import *
win=Tk()
win.title("beach")

win.geometry("600x400")
Btn1=Button(win,text="Qtest1",bg="yellow",fg="black")
Btn2=Button(win ,text="QQtest2",bg="lightblue",fg="black")
Btn3=Button(win,text="QQQtest3",bg="lightgreen",fg="black")

lab=Label(win,text="Label is here",bg="black",fg="white")


Btn1.place(x=80,y=60)
Btn2.place(x=260,y=60)
Btn3.place(x=440,y=60)
lab.place(x=250,y=80)


win.mainloop()
#-------------------------------------------------


# Btn1.pack(anchor=NW,side=LEFT,pady=30,padx=30)  #anchor=位置  side=置左右上下, pady=與上下格多少, padx=與左右格多少
# Btn2.pack(anchor=NW,side=LEFT,pady=30,padx=30)  #直接設方位會有擋道的問題 可能就要用grid
# Btn3.pack(anchor=NW,side=LEFT,pady=30,padx=30)
# lab.pack(side=LEFT)

# Btn1.grid(row=1,column=3)  # grid只能用在有某個方塊的的乓邊 大視窗很難用
# Btn2.grid(row=2,column=6)  # 考慮xy座標去完成
# Btn3.grid(row=5,column=9)
