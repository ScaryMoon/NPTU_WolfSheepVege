import random

# pocker = [
#     "♠A", "♠2", "♠3", "♠4", "♠5", "♠6", "♠7", "♠8", "♠9", "♠10", "♠J", "♠Q", "♠K",
#     "♥A", "♥2", "♥3", "♥4", "♥5", "♥6", "♥7", "♥8", "♥9", "♥10", "♥J", "♥Q", "♥K",
#     "♦A", "♦2", "♦3", "♦4", "♦5", "♦6", "♦7", "♦8", "♦9", "♦10", "♦J", "♦Q", "♦K",
#     "♣A", "♣2", "♣3", "♣4", "♣5", "♣6", "♣7", "♣8", "♣9", "♣10", "♣J", "♣Q", "♣K"
# ]
# ------------------
pocker2 = [
    "♠A", "♠2", "♠8", "♠9", "♠10", "♠J", "♠Q", "♠K",
    "♥A", "♥2", "♥8", "♥9", "♥10", "♥J", "♥Q", "♥K",
    "♦A", "♦2", "♦8", "♦9", "♦10", "♦J", "♦Q", "♦K",
    "♣A", "♣2", "♣8", "♣9", "♣10", "♣J", "♣Q", "♣K"
]
# ------------------
randlist = []
for i in range(5):
    randlist.append(int(random.uniform(1, len(pocker2))))

output_5list = []
for j in randlist:
    output_5list.append(pocker2[j])


print(output_5list)  # 隨機五個

# 整理以便找 爐  # 個數字的ascii
sort_list = []
for k in range(len(output_5list)):
    if output_5list[k][1] == "J":
        sort_list.append(11)  # sort list
    elif len(output_5list[k]) == 3:
        sort_list.append(10)  # sort list
    elif output_5list[k][1] == "Q":
        sort_list.append(12)  # sort list
    elif output_5list[k][1] == "K":
        sort_list.append(13)  # sort list
    elif output_5list[k][1] == "A":
        sort_list.append(14)  # sort list
    elif output_5list[k][1] == "2":
        sort_list.append(15)  # sort list
    else:
        sort_list.append(int(output_5list[k][1]))
sort_list.sort()
print(sort_list)

j = 0

cout = ""
# --------小順--------
for p in range(4, 1, -1):
    if sort_list[p-2]+2 == sort_list[p-1]+1 == sort_list[p]:
        cout = "小順"
# --------順--------
if sort_list[j]+4 == sort_list[j+1]+3 == sort_list[j+2]+2 == sort_list[j+3]+1 == sort_list[j+4]:
    cout = "順"
# --------爐---------
if (sort_list[j] == sort_list[j+1] == sort_list[j+2] != sort_list[j+3] & sort_list[j+3] == sort_list[j+4]) | (
        sort_list[j] == sort_list[j+1] != sort_list[j+2] & sort_list[j+2] == sort_list[j+3] == sort_list[j+4]):
    cout = "盧"
# --------鐵支-------
if sort_list[j] == sort_list[j+1] == sort_list[j+2] == sort_list[j+3] | sort_list[j+1] == sort_list[j+2] == sort_list[j+3] == sort_list[j+4]:
    cout = "鐵支"

print(cout)


# print(ord("0"))=48
# print(ord("9"))=57
# print(ord("A"))=65 - ?=1 ans=64
# print(ord("J"))=74
