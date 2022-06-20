from tkinter import *
import time
win = Tk()
win.title("beach")
win.geometry("1340x815")

# background method2
canvas = Canvas(win, width=1340, height=815)
canvas.place(x=0, y=0)

Back = PhotoImage(file="terrariaBG.png")
canvas.create_image(0, 0, anchor=NW, image=Back)

# # background method1
# bgg = PhotoImage(file="terraria top.png")   # BG setting
# labwin = Label(win, image=bgg)              # use label to be win.bg
# labwin.place(x=0, y=0)                      # set pic to left&top
lab = Label(win, text="要讓誰過河?", bg="#323232", fg="white")


here = ["菜", "羊", "狼", "人"]
there = []
print("目前:", here, "~~~~~~~~~~", there)

select = {1: "菜", 2: "羊", 3: "狼", 4: "人"}
lastStep = [4]
clearStep1 = [2, 4, 3, 2, 1, 4, 2]
clearStep2 = [2, 4, 1, 2, 3, 4, 2]
turned = 0


print("1:菜 2:羊 3:狼 4:人 選擇:")
des = 0


# -----------------choose 4 moving------------------
# test amine
def CHOOSE_R(choose):
    if choose == 1:
        HuVegeR()
    elif choose == 2:
        HuSheepR()
    elif choose == 3:
        HuWolfR()
    elif choose == 4:
        HumanGoR()


def CHOOSE_L(choose):
    if choose == 1:
        HuVegeL()
    elif choose == 2:
        HuSheepL()
    elif choose == 3:
        HuWolfL()
    elif choose == 4:
        HumanGoL()

# ----------------Moving------------------
# sheep (4,185,0)
# wolf down 15 (3, 120, 15) remanber up15  (3,120,-15)
# vege (5,240,15) 同上 X,X,-15

# ---------human--------------------------------------------------------


def rotate():
    canvas.delete(6)
    canvas.create_image(350, 530, anchor=NW, image=humancan)


def rotateR():
    canvas.delete(2)
    canvas.create_image(900, 530, anchor=NW, image=humancanR)


def HumanGoR():  # 單 人右邊
    global humancan, humancanR
    canvas.move(2, 0, 0)
    for x in range(0, 110):

        win.update()
        canvas.move(2, 5, 0)
        time.sleep(0.01)
    canvas.move(2, 1, 0)
    canvas.delete(2)
    rotateR()


def HumanGoL():  # 單 人左邊
    # global humancan, humancanR
    canvas.move(6, 0, 0)
    for x in range(0, 110):
        canvas.move(6, -5, 0)
        win.update()
        time.sleep(0.01)
    canvas.move(6, 1, 0)
    canvas.delete(6)
    rotate()
    # canvas.delete(6)
    win.update()


# --------sheep--------------------------------------------------------
def HuSheepR():  # 人羊 右
    global sheepcan
    canvas.move(4, 185, 0)
    for x in range(0, 110):
        win.update()
        canvas.move(4, 5, 0)
        canvas.move(2, 5, 0)

        time.sleep(0.01)
    canvas.move(4, 185, 0)  # sheep上岸
    canvas.delete(2)  # del左邊的人
    rotateR()


def HuSheepL():  # 人羊 左
    # global humancan, sheepcan, humancanR
    canvas.move(4, -185, 0)
    for x in range(0, 110):
        win.update()
        canvas.move(4, -5, 0)
        canvas.move(6, -5, 0)

        time.sleep(0.01)
    canvas.move(4, -185, 0)  # sheep上岸
    canvas.delete(6)  # del右邊的人
    rotate()
    win.update()
# ------------ wolf--------------------------------------------------------
# 3


def HuWolfR():
    global wolfcan
    canvas.move(3, 120, 15)
    for x in range(0, 110):
        canvas.move(3, 5, 0)
        canvas.move(2, 5, 0)
        win.update()
        time.sleep(0.01)
    canvas.move(3, 120, -15)
    canvas.delete(2)
    canvas.create_image(900, 530, anchor=NW, image=humancanR)  # pic 1


def HuWolfL():
    # global  wolfcan
    canvas.move(3, -120, 15)
    for x in range(0, 110):
        canvas.move(3, 5, 0)
        canvas.move(6, 5, 0)
        win.update()
        time.sleep(0.01)
    canvas.move(3, 120, -15)
    canvas.delete(6)
    canvas.create_image(350, 530, anchor=NW, image=humancan)  # pic 1


# -------vege----------------------------------------------------------
def HuVegeR():
    global vegecan
    canvas.move(5, 240, 15)
    for x in range(0, 110):
        canvas.move(5, 5, 0)
        canvas.move(2, 5, 0)
        win.update()
        time.sleep(0.01)
    canvas.move(5, 240, -15)
    canvas.delete(2)
    canvas.create_image(900, 530, anchor=NW, image=humancanR)  # pic 1


def HuVegeL():
    # global  vegecan
    canvas.move(5, -240, 15)
    for x in range(0, 110):
        canvas.move(5, 5, 0)
        canvas.move(6, 5, 0)
        win.update()
        time.sleep(0.01)
    win.update()
    canvas.move(5, -240, -15)
    canvas.delete(6)
    canvas.create_image(350, 530, anchor=NW, image=humancan)  # pic 1


# ------------------------Game--------------------------
def Gameover(Here, There):
    if (("人" not in Here) & (("狼" in Here) & ("羊" in Here)) & ("菜" in Here)):
        return "羊吃了菜 & 狼吃了羊"   # w-200 s-100
    elif ("人" not in Here) & (("狼" in Here) & ("羊" in Here)):
        return "狼吃了羊"  # w-100
    elif (("人" not in Here) & (("羊" in Here)) & ("菜" in Here)):
        return "羊吃了菜"

    elif (("人" not in There) & (("狼" in There) & ("羊" in There)) & ("菜" in There)):
        return "羊吃了菜 & 狼吃了羊"
    elif ("人" not in There) & (("狼" in There) & ("羊" in There)):
        return "狼吃了羊"
    elif (("人" not in There) & (("羊" in There)) & ("菜" in There)):
        return "羊吃了菜"
    else:
        return "請繼續"


def output2lab(string):
    lab.config(text=string)


def keep(choose):
    global here, there, lastStep, clearStep1, clearStep2
    global des, turned, select

    if des == 1:
        win.destroy()
    select = {1: "菜", 2: "羊", 3: "狼", 4: "人"}
    lastStep.append(choose)  # 前一次選的   Ex2
    lab.config(text="要讓誰過河?")

    # 正解
    if (((choose == clearStep1[0]) | (choose == clearStep2[0])) & (turned == 0)):  # Ex2
        if select[choose] not in here:
            a = len(lastStep)
            del lastStep[a-1]
            print("此地無", select[choose])
            out = "此地無", select[choose]
            output2lab(out)
        else:
            del clearStep1[0]  # del 2
            del clearStep2[0]
            a = here.index(select[choose])  # del 2在here[]內的index
            del here[a]
            if "人" in here:
                a = here.index("人")
                del here[a]
                there.append("人")
            there.append(select[choose])
            CHOOSE_R(choose)  # test Anime
            # HuSheepL()
            turned = 1
            print("換右邊")
    elif (((choose == clearStep1[0]) | (choose == clearStep2[0])) & (turned == 1)):
        if select[choose] not in there:
            a = len(lastStep)
            del lastStep[a-1]
            print("此地無", select[choose])
            out = "此地無", select[choose]
            output2lab(out)
        else:
            del clearStep1[0]  # del 2
            del clearStep2[0]
            a = there.index(select[choose])  # del 2在there[]內的index
            del there[a]
            if "人" in there:
                a = there.index("人")
                del there[a]
                here.append("人")
            here.append(select[choose])
            CHOOSE_L(choose)  # test Anime
            turned = 0

            print("換左邊")
        # -------------------------------ok

    # 無動物在這
    elif (((select[choose] not in here) & (turned == 0)) | ((select[choose] not in there) & (turned == 1))):
        if lastStep != []:
            a = len(lastStep)
            del lastStep[a-1]
        print("此地無", select[choose])
        out = "此地無", select[choose]
        output2lab(out)
        # --------------------------------ok

    # 重複動作
    elif choose == lastStep[len(lastStep)-1]:
        if (turned == 0):
            a = here.index(select[choose])  # del 2在here[]內的index
            del here[a]
            if "人" in here:
                a = here.index("人")
                del here[a]
                there.append("人")
            there.append(select[choose])
            CHOOSE_R(choose)  # test Anime
            print("換右邊")
        else:
            a = there.index(select[choose])  # del 2在there[]內的index
            del there[a]
            if "人" in there:
                a = there.index("人")
                del there[a]
                here.append("人")
            here.append(select[choose])
            CHOOSE_L(choose)  # test Anime

            print("換左邊")
        turned += 1
        turned %= 2  # switch
        # --------------------------------ok

    else:
        print("你的選擇不再這地方")
        output2lab("你的選擇不再這地方")
    print("目前:", here, "~~~~~~~~~~", there)

    # win Game
    if here == []:
        print("恭喜你成功")
        output2lab("恭喜你成功")

    # Gameover
    if Gameover(here, there) != "請繼續":
        output2lab(Gameover(here, there)+"\n你輸了 請隨便按一個'Button'結束遊戲")
        print(Gameover(here, there))
        des = 1

        return 0

    if des != 1:
        print("1:菜 2:羊 3:狼 4:人 選擇:")


# # picutre
humancan = PhotoImage(file="Rright.png")  # 2
canvas.create_image(350, 530, anchor=NW, image=humancan)

wolfcan = PhotoImage(file="Rwolf.png")  # 3
canvas.create_image(280, 530, anchor=NW, image=wolfcan)

sheepcan = PhotoImage(file="Rsheep.png")  # 4
canvas.create_image(210, 530, anchor=NW, image=sheepcan)
vegecan = PhotoImage(file="Rvege.png")  # 5
canvas.create_image(140, 550, anchor=NW, image=vegecan)
humancanR = PhotoImage(file="Rleft.png")  # 6
# canvas.create_image(350, 530, anchor=NW, image=humancanR)

# ---------------------start-----------------------
# button
wolfBtn = Button(win, text="狼", bg="yellow",
                 fg="black", command=lambda: keep(3))
sheepBtn = Button(win, text="羊", bg="lightblue",
                  fg="black", command=lambda: keep(2))
vegetableBtn = Button(win, text="菜", bg="lightgreen",
                      fg="black", command=lambda: keep(1))
human = Button(win, text="人", bg="white", fg="black", command=lambda: keep(4))
wolfBtn.place(x=80, y=60)
sheepBtn.place(x=140, y=60)
vegetableBtn.place(x=200, y=60)
human.place(x=260, y=60)
lab.place(x=250, y=90)

win.mainloop()
