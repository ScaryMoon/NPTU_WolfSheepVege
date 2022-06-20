import random
count, fin, ans = 0, 0, 0
compairShape = ""
storeNum = []
temp4shape = []
temp4Num = []

colorrr = {"♠": 1, "♥": 2, "♦": 3, "♣": 4}
dictionary4fight = {1: "同花大順", 2: "鐵支",  3: "葫蘆", 4: "同花",
                    5: "順子",  6: "三條", 7: "2對", 8: "1對",  9: "散牌"}
# ♠
# ♥
# ♦
# ♣
# -------------------------function-------------------------


def choiceShape(a):
    global Player1
    shapeChoice = [1, 2, 3, 4]
    color = {1: "♠", 2: "♥", 3: "♦",  4: "♣"}
    asd = color[random.choice(shapeChoice)]

    number = random.randint(2, 14)
    changeNumber = {10: "T", 11: "J", 12: "Q", 13: "K", 14: "A"}
    if number >= 10:
        A = changeNumber[number]
    else:
        A = number
    if ((str(asd)+str(A)) not in a) & ((str(asd)+str(A))not in Player1):
        return asd+str(A)
    return choiceShape(a)


def Sortcard(cardsort):
    array = []
    test = ["T", "J", "Q", "K", "A"]
    changeNumber = {"T": 10, "J": 11, "Q": 12, "K": 13, "A": 14}
    for i in range(len(cardsort)):
        if cardsort[i] in test:
            array.append(int(changeNumber[cardsort[i]]))
        else:
            array.append(int(cardsort[i]))

    array = sorted(array)
    return array


def compair(number, shape):
    global count, fin, compairShape
    count = 0
    compairShape = "♠"
    # return  = ""
    if number[0]+4 == number[1]+3 == number[2]+2 == number[3]+1 == number[4]:
        if (shape[0] == shape[1] == shape[2] == shape[3] == shape[4]):
            fin = number[4]
            compairShape = shape[2]
            return 1
        else:
            fin = number[4]
            return 5
    elif (number[0] == number[1] == number[2] == number[3]) | (number[1] == number[2] == number[3] == number[4]):
        fin = number[3]
        return 2
    elif (number[0] == number[1] == number[2] & number[2] != number[3] == number[4]) | (number[0] == number[1] != number[2] & number[2] == number[3] == number[4]):
        fin = number[2]
        return 3
    elif(shape[0] == shape[1] == shape[2] == shape[3] == shape[4]):
        compairShape = shape[2]
        return 4
    elif (number[0] == number[1] == number[2]) | (number[1] == number[2] == number[3]) | (number[2] == number[3] == number[4]):
        fin = number[2]
        return 6
    elif (number[0] == number[1]) | (number[1] == number[2]) | (number[2] == number[3]) | (number[3] == number[4]):
        for i in range(len(number)-1):
            if number[i] == number[i+1]:
                count += 1
                fin = number[i]
        if count == 2:
            return 7
        else:
            return 8
    else:
        return 9

# //    what cards r u get?


def GETcard(putShape):
    global storeNum
    global temp4Num
    global temp4shape
    storeNum = []
    temp4shape = []
    temp4Num = []

    for i in range(5):
        putShape = choiceShape(storeNum)
        storeNum.append(putShape)
    # print(storeNum)
    return storeNum


def fight():  # 對子? 順? 盧?
    global storeNum
    global temp4Num
    global temp4shape
    # //   sort cards for compair
    for j in range(len(storeNum)):
        temp4Num.append(storeNum[j][1])
    temp4Num = Sortcard(temp4Num)
    # print(temp2store)

    # //     store Shape for compair
    for k in range(len(storeNum)):
        temp4shape.append(storeNum[k][0])
    # print(temp2shape)

    # //     define element 2 compair

    ans = compair(temp4Num, temp4shape)
    return ans


# ↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓ Ｍａｉｎ ↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓
Player1 = ""  # 防止重複
Player2 = ""  # 防止重複
P1 = []
P2 = []
print("My cards   : ", end="")
P1.append(GETcard(Player1))
P1.append(fight())
P1.append(fin)
P1.append(compairShape)
print(P1[0])
print("得到       :", dictionary4fight[P1[1]])
# if (P1[1] == 7) | (P1[1] == 8):

print("enemy cards: ", end="")
P2.append(GETcard(Player2))
P2.append(fight())
P2.append(fin)
P2.append(compairShape)
print(P2[0])
print("得到       :", dictionary4fight[P2[1]])


if P1[1] < P2[1]:       # 桐花順>盧
    print("種類 Player1:大", "Player2小")
    print("Player1 win")
elif P1[1] > P2[1]:
    print("種類 Player1:小", "Player2大")
    print("Player2 win")
else:                   # 順 vs 順 先number
    if P1[2] > P2[2]:
        print("同種牌 數字Player1:", P1[2], "Player2:", P2[2])
        print("Player1 win")
    elif P1[2] < P2[2]:
        print("同種牌 數字Player1:", P1[2], "Player2:", P2[2])
        print("Player2 win")
    else:               # 比較 花色
        if colorrr[P1[3]] < colorrr[P2[3]]:
            print("同種同數 花色Player1:", P1[3], "Player2:", P2[3])
            print("Player1 win")
        else:
            print("同種同數 花色Player1:", P1[3], "Player2:", P2[3])
            print("Player2 win")
