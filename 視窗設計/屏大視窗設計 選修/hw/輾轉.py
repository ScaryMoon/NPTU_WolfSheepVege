a = int(input("a="))
b = int(input("b="))
if a % b == 0:
    print(b)
else:
    d = a % b
    while d != 0:
        a = b
        b = d
        d = a % b

    print(b)
