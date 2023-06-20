import random
storeNum = []
temp2store = []
temp2shape = []
count = 0
# ♠
# ♥
# ♦
# ♣
# -------------------------function-------------------------


def choiceShape(a):
    
    shapeChoice = ["h", "s", "c", "d"]
    color = {"h": "♥", "s": "♠", "c": "♣", "d": "♦"}
    asd = color[random.choice(shapeChoice)]
    number = random.randint(10, 14)
    
    changeNumber = {10: "T", 11: "J", 12: "Q", 13: "K", 14: "A"}
    if number >= 10:
        A = changeNumber[number]
    else:
        A = number
    if (str(asd)+str(A)) not in a:
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
    global count
    # return  = ""
    if number[0]+4 == number[1]+3 == number[2]+2 == number[3]+1 == number[4]:
        if (shape[0] == shape[1] == shape[2] == shape[3] == shape[4]):
            return "同花大順"
        else:
            return "順子"
    elif (number[0] == number[1] == number[2] == number[3]) | (number[1] == number[2] == number[3] == number[0]):
        return "鐵支"
    elif (number[0] == number[1] == number[2] & number[2] != number[3] == number[4]) | (number[0] == number[1] != number[2] & number[2] == number[3] == number[4]):
        return "葫蘆"
    elif(shape[0] == shape[1] == shape[2] == shape[3] == shape[4]):
        return "同花"
    elif (number[0] == number[1] == number[2]) | (number[1] == number[2] == number[3]) | (number[2] == number[3] == number[4]):
        return "三條"
    elif (number[0] == number[1]) | (number[1] == number[2]) | (number[2] == number[3]) | (number[3] == number[4]):
        for i in range(len(number)-1):
            if number[i] == number[i+1]:
                count += 1
        return str(count)+"對"
    else:
        return "散牌"


# ↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓ Ｍａｉｎ ↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓

# //    what cards r u get?
putShape=""
for i in range(5): 
    putShape = choiceShape(storeNum)
    storeNum.append(putShape)
print(storeNum)
# //   sort cards for compair
for j in range(len(storeNum)):
    temp2store.append(storeNum[j][1])
temp2store = Sortcard(temp2store)
# print(temp2store)

# //     store Shape
for k in range(len(storeNum)):
    temp2shape.append(storeNum[k][0])
# print(temp2shape)


# //     define element 2 compair
print(compair(temp2store, temp2shape))


