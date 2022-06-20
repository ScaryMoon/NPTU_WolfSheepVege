here = ["菜", "羊", "狼", "人"]
there = []
print("目前:", here, "~~~~~~~~~~", there)


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


lastStep = [4]
# clearStep1=["羊", "人", "狼", "羊", "菜", "人", "羊"]
# clearStep2=["羊", "人", "菜", "羊", "狼", "人", "羊"]
clearStep1 = [2, 4, 3, 2, 1, 4, 2]
clearStep2 = [2, 4, 1, 2, 3, 4, 2]
turned = 0
while(True):
    choose = int(input("1:菜 2:羊 3:狼 4:人 選擇:"))  # 選什麼
    select = {1: "菜", 2: "羊", 3: "狼", 4: "人"}
    lastStep.append(choose)  # 前一次選的   Ex2

    # 正解
    if (((choose == clearStep1[0]) | (choose == clearStep2[0])) & (turned == 0)):  # Ex2
        if select[choose] not in here:
            a = len(lastStep)
            del lastStep[a-1]
            print("此地無", select[choose])
            continue
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
            continue
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
        continue
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
        continue
    print("目前:", here, "~~~~~~~~~~", there)
    # win Game
    if here == []:
        print("恭喜你成功")
        break
    # Gameover
    if Gameover(here, there) == "請繼續":
        continue
    else:
        print(Gameover(here, there))
        break

# resource
# opposite={"菜":1, "羊":2 ,"狼":3, "人":4}
