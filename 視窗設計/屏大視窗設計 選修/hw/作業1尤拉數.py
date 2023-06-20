# 題目: 求出e 當末數就是1/n! <0.000001 時 break

total = 1
while(total > 0.000001):
    userInput = input("input number:")
    e = 1
    for k in range(1, int(userInput)):
        n = 1
        for i in range(1, k+1):
            n *= i
            total = 1/n

        if total >= 0.000001:
            e += total

    print(e)
