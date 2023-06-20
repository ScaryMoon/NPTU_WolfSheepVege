from tkinter import *
win = Tk()
win.title("beach")
win.geometry("1340x815")
bgg = PhotoImage(file="terrariaBG.png") #BG setting
labwin = Label(win, image=bgg)# use label to be win.bg
labwin.place(x=0, y=0) # set pic to left&top
lab = Label(win, text="讓誰過河?", bg="#323232", fg="white")


here = ["菜", "羊", "狼", "人"]
there = []
print("目前:", here, "~~~~~~~~~~", there)

select = {1: "菜", 2: "羊", 3: "狼", 4: "人"}
lastStep = [4]
clearStep1 = [2, 4, 3, 2, 1, 4, 2]
clearStep2 = [2, 4, 1, 2, 3, 4, 2]
turned = 0


def Gameover(Here, There):
    if (("人" not in Here) & (("狼" in Here) & ("羊" in Here)) & ("菜" in Here)):
        return "羊吃了菜 & 狼吃了羊"
    elif ("人" not in Here) & (("狼" in Here) & ("羊" in Here)):
        return "狼吃了羊"
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


print("1:菜 2:羊 3:狼 4:人 選擇:")
des = 0


def keep(choose):
    global here, there, lastStep, clearStep1, clearStep2
    global des, turned, select

    if des == 1:
        win.destroy()
    select = {1: "菜", 2: "羊", 3: "狼", 4: "人"}
    lastStep.append(choose)  # 前一次選的   Ex2
    lab.config(text="讓誰過河?")

    # 正解
    if (((choose == clearStep1[0]) | (choose == clearStep2[0])) & (turned == 0)):  # Ex2
        if select[choose] not in here:
            a = len(lastStep)
            del lastStep[a-1]
            print("此地無", select[choose])
            out = "此地無", select[choose]
            output2lab(out)
        del clearStep1[0]  # del 2
        del clearStep2[0]
        a = here.index(select[choose])  # del 2在here[]內的index
        del here[a]
        if "人" in here:
            a = here.index("人")
            del here[a]
            there.append("人")
        there.append(select[choose])
        turned = 1
        print("換右邊")
    elif (((choose == clearStep1[0]) | (choose == clearStep2[0])) & (turned == 1)):
        if select[choose] not in there:
            a = len(lastStep)
            del lastStep[a-1]
            print("此地無", select[choose])
            out = "此地無", select[choose]
            output2lab(out)
        del clearStep1[0]  # del 2
        del clearStep2[0]
        a = there.index(select[choose])  # del 2在there[]內的index
        del there[a]
        if "人" in there:
            a = there.index("人")
            del there[a]
            here.append("人")
        here.append(select[choose])
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

            print("換右邊")
        else:
            a = there.index(select[choose])  # del 2在there[]內的index
            del there[a]
            if "人" in there:
                a = there.index("人")
                del there[a]
                here.append("人")
            here.append(select[choose])

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
        output2lab(Gameover(here, there)+"\n你輸了 請隨便按一個Button")
        print(Gameover(here, there))
        des = 1

        return 0
    
    if des != 1:
        print("1:菜 2:羊 3:狼 4:人 選擇:")


# ---------------------start-----------------------
wolf = Button(win, text="狼", bg="yellow", fg="black", command=lambda: keep(3))
sheep = Button(win, text="羊", bg="lightblue",
               fg="black", command=lambda: keep(2))
vegetable = Button(win, text="菜", bg="lightgreen",
                   fg="black", command=lambda: keep(1))
human = Button(win, text="人", bg="white", fg="black", command=lambda: keep(4))
wolf.place(x=80, y=60)
sheep.place(x=140, y=60)
vegetable.place(x=200, y=60)
human.place(x=260, y=60)
lab.place(x=250, y=90)

win.mainloop()
