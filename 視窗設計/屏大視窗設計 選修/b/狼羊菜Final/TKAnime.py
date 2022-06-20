from pygame import mixer   # 必須要 pip install pygame
from tkinter import *
from winsound import *
import time

win = Tk()
win.title("beach")
win.geometry("1340x815")

# background method2
canvas = Canvas(win, width=1340, height=815)
canvas.place(x=0, y=0)

Back = PhotoImage(file="terrariaBG.png")
canvas.create_image(0, 0, anchor=NW, image=Back)

lab = Label(win, text="要讓誰過河?", font=30, bg="yellow")

LabSignName = Label(win, text="國立屏東大學 資工系 李宇弘", font=30)


here = ["菜", "羊", "狼", "人"]
there = []
print("目前:", here, "~~~~~~~~~~", there)

select = {1: "菜", 2: "羊", 3: "狼", 4: "人"}
lastStep = [4]
clearStep1 = [2, 4, 3, 2, 1, 4, 2]
clearStep2 = [2, 4, 1, 2, 3, 4, 2]
turned = 0


print("1:菜 2:羊 3:狼 4:人 選擇:")


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
# # -----------clear correct-sound--------------------
# mixer.init()


# def play_music():
#     mixer.music.load("correct.mp3")
#     mixer.music.play()
# ---------human--------------------------------------------------------


def HumanGoR():  # 單 人右邊
    canvas.move(2, 0, 0)
    for x in range(0, 100):
        win.update()
        canvas.move(2, 5, 0)
        time.sleep(0.01)


def HumanGoL():  # 單 人左邊
    canvas.move(2, 0, 0)
    for x in range(0, 100):
        canvas.move(2, -5, 0)
        win.update()
        time.sleep(0.01)


# --------sheep--------------------------------------------------------
def HuSheepR():  # 人羊 右
    global sheepcan
    canvas.move(4, 190, 15)
    for x in range(0, 100):
        win.update()
        canvas.move(4, 5, 0)
        canvas.move(2, 5, 0)

        time.sleep(0.01)
    canvas.move(4, 190, -15)  # sheep上岸


def HuSheepL():  # 人羊 左
    canvas.move(4, -190, 15)
    for x in range(0, 100):
        win.update()
        canvas.move(4, -5, 0)
        canvas.move(2, -5, 0)

        time.sleep(0.01)
    canvas.move(4, -190, -15)  # sheep上岸
# ------------ wolf--------------------------------------------------------


def HuWolfR():
    global wolfcan
    canvas.move(3, 134, 15)
    for x in range(0, 100):
        canvas.move(3, 5, 0)
        canvas.move(2, 5, 0)
        win.update()
        time.sleep(0.01)
    canvas.move(3, 134, -15)


def HuWolfL():
    # global  wolfcan
    canvas.move(3, -134, 15)
    for x in range(0, 100):
        canvas.move(3, -5, 0)
        canvas.move(2, -5, 0)
        win.update()
        time.sleep(0.01)
    canvas.move(3, -134, -15)

# -------vege----------------------------------------------------------


def HuVegeR():
    global vegecan
    canvas.move(5, 256, 15)
    for x in range(0, 100):
        canvas.move(5, 5, 0)
        canvas.move(2, 5, 0)
        win.update()
        time.sleep(0.01)
    canvas.move(5, 256, -15)


def HuVegeL():
    # global  vegecan
    canvas.move(5, -256, 15)
    for x in range(0, 100):
        canvas.move(5, -5, 0)
        canvas.move(2, -5, 0)
        win.update()
        time.sleep(0.01)
    win.update()
    canvas.move(5, -256, -15)

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
        # play_music()
        print("恭喜你成功")
        output2lab("恭喜你成功!! 按Restart再玩一次!")

    # Gameover
    if Gameover(here, there) != "請繼續":
        output2lab(Gameover(here, there)+"\n你輸了 請按一個'Restart'重新開始")
        print(Gameover(here, there))

        return 0


def restart():
    global lab, lastStep, clearStep1, clearStep2, turned, here, there

    lab.config(text="要讓誰過河?")

    REhere = ["菜", "羊", "狼", "人"]
    REthere = []
    RElastStep = [4]
    REclearStep1 = [2, 4, 3, 2, 1, 4, 2]
    REclearStep2 = [2, 4, 1, 2, 3, 4, 2]
    REturned = 0

    here = REhere
    there = REthere
    lastStep = RElastStep
    clearStep1 = REclearStep1
    clearStep2 = REclearStep2
    turned = REturned
    print("1:菜 2:羊 3:狼 4:人 選擇:")

    canvas.moveto(2, x='350', y='530')
    canvas.moveto(3, x='280', y='530')
    canvas.moveto(4, x='215', y='530')
    canvas.moveto(5, x='150', y='550')

    win.update()


# # picutre
Boat2 = PhotoImage(file="Rboat.png")  # 2
canvas.create_image(350, 530, anchor=NW, image=Boat2)

wolfcan = PhotoImage(file="Rwolf.png")  # 3
canvas.create_image(280, 530, anchor=NW, image=wolfcan)

sheepcan = PhotoImage(file="Rsheep.png")  # 4
canvas.create_image(215, 530, anchor=NW, image=sheepcan)
vegecan = PhotoImage(file="Rvege.png")  # 5
canvas.create_image(150, 550, anchor=NW, image=vegecan)

# ---------------------start-----------------------
# button

wolfBtn = Button(win, text="狼", image=wolfcan, height=67,
                 fg="black", bg="skyblue", command=lambda: keep(3))
sheepBtn = Button(win, text="羊", image=sheepcan,
                  fg="black", bg="skyblue", command=lambda: keep(2))
vegetableBtn = Button(win, text="菜", image=vegecan, width=60, height=67,
                      fg="black", bg="skyblue", command=lambda: keep(1))
human = Button(win, width=180, height=67, bg="skyblue", text="人",
               image=Boat2, fg="black", command=lambda: keep(4))

RE = Button(win, fg="black", bg="skyblue",
            text="~Restart~", command=lambda: restart())
RE.place(x=1100, y=60)
wolfBtn.place(x=630, y=60)
sheepBtn.place(x=510, y=60)
vegetableBtn.place(x=400, y=60)
human.place(x=765, y=60)
lab.place(x=560, y=140)
LabSignName.place(x=500, y=0)
win.mainloop()
